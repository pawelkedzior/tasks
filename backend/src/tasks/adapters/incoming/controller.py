from typing import Annotated

from fastapi import Body

from app import app, tasks_service
from tasks.domain.model.task import Task


@app.get("/tasks")
async def get_all_tasks():
    return tasks_service.get_all_tasks()


@app.put("/tasks")
async def add_new_task(task: Annotated[Task, Body(embed=False)]):
    tasks_service.add_new_task(task)


@app.post("/tasks")
async def update_task(task: Task):
    tasks_service.update_task(task)


@app.delete("/tasks")
async def remove_task(task: Task):
    tasks_service.remove_task(task)
