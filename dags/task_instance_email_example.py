from datetime import timedelta
from airflow.decorators import task, dag
from airflow.operators.email import EmailOperator
from airflow.model import TaskInstance


default_args = {
    "owner": 'my name',
    "depends_on_past": False,
    "email": ["my_email@email.com"],
    "email_on_failure": True,
    "email_on_success": True,
    "retires": 3,
}


@dag(
    dag_id = "TI_example",
    default_args = default_args,
    description = "some stuff here.",
    start_date = timedelta(days=-1),
    schedule_interval = None,
    catchup = False,
)
def TI_example():

    @task(
        retries = 3,
        retry_delay = timedelta(minutes=2),
        provide_context = True
    )
    def task1() -> dict:
        try_num = TaskInstance.try_number
        max_tries = TaskInstance.max_tries
        print(f"Current Task try attempt: {try_num}/{max_tries}")
        return {
            "try_attempt": try_num,
            "max_tries": max_tries
        }
    
    @task
    def task2(task1_xcom: dict):
        try_attempt = task1_xcom["try_attempt"]
        max_tries = task1_xcom["max_tries"]

        print(try_attempt)
        print(max_tries)

    t1 = task1()
    t2 = task2(t1)

    t1 >> t2

run = TI_example()

