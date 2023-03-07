from prefect import task, flow
from time import sleep

@task
def task1(secs):
    sleep(secs)

@task
def task2(secs):
    sleep(secs)

@flow
def my_flow():
    task1(2)
    task2.submit(10)
    task2.submit(2)

my_flow()