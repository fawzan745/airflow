from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.models.param import Param

from csv_to_sqlite_pipeline.tasks.extract import import_choose_extraction, from_csv, from_json
from csv_to_sqlite_pipeline.tasks.load import import_to_sqlite

with DAG(
    "extract_load_dag",
    params={
        "file_path": Param("Data/files.csv", description="Parameter lokasi file akan di extract (csv/json)"),
        "extract_type": Param("csv", description="Jenis file yang akan di extract (csv/json)")
    }
) as dag:
    start_task = EmptyOperator(task_id="start_task")

    # Branching for extract type
    choose_extract_task = BranchPythonOperator(
        task_id="choose_extract_task",
        python_callable=choose_extraction
    )

    # Task untuk extract data csv
    extract_from_csv = PythonOperator(
        task_id="extract_from_csv",
        python_callable=from_csv
    )

    # Task untuk extract data json 
    extract_from_json = PythonOperator(
        task_id="extract_from_json",
        python_callable=from_json
    )

    # Task untuk load data ke sqlite
    load_to_sqlite = PythonOperator(
        task_id="load_to_sqlite",
        python_callable=import_to_sqlite,
        trigger_rule="one_success"
    )

    end_task = EmptyOperator(task_id="end_task")

    start_task >> choose_extract_task >> [extract_from_csv, extract_from_json] >> load_to_sqlite >> end_task