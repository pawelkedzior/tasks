from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from authentication.adapters.outgoing.memory import InMemoryUserRepository
from authentication.domain.port.incoming import AuthService
from authentication.domain.port.outgoing import UserRepository
from authentication.domain.service.auth import AuthenticationService
from tasks.adapters.outgoing.memory import InMemoryTaskRepository
from tasks.domain.port.incoming import TaskService
from tasks.domain.port.outgoing import TaskRepository
from tasks.domain.service.tasks import TasksService

print("Starting API...")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend origin here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_repository: UserRepository = InMemoryUserRepository()
auth_service: AuthService = AuthenticationService(user_repository)
tasks_repository: TaskRepository = InMemoryTaskRepository()
tasks_service: TaskService = TasksService(tasks_repository)
import authentication.adapters.incoming.controller
import tasks.adapters.incoming.controller

print("API started")
