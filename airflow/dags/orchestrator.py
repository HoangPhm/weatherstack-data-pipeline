from airflow import DAGS

dag = DAG(
    dag_id='weather-api-orchestrator',
    default_args=default_args,
    schedule=...
)