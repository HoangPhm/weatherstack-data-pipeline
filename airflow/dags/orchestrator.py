import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount

sys.path.append('/opt/airflow/api-request')
from insert_records import main

default_args = {
    'description': 'A DAG to orchestrate Data',
    'start_date': datetime(2026, 8, 8),
    'catchup': False,
}

dag = DAG(
    dag_id='weatherstack-api-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=main
    )

    task2 = DockerOperator(
        task_id = 'transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:latest',
        command='run --select stg_weather_data',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/workspaces/weatherstack-data-pipeline/dbt/my_project/',
                target='/usr/app', type='bind'),
            Mount(source='/workspaces/weatherstack-data-pipeline/dbt/profiles.yml',
                target='/root/.dbt/profiles.yml', type='bind'),
        ],
        network_mode='weatherstack-data-pipeline_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )

    task1 >> task2