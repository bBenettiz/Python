from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

# Definição do DAG
with DAG(
    dag_id="benetti_dag_test",
    start_date=datetime(2021, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["teste", "benetti"],
) as dag:
    
    # Tarefa inicial
    start = EmptyOperator(task_id="inicio")

    # Tarefa final
    end = EmptyOperator(task_id="fim")

    # Dependência
    start >> end
