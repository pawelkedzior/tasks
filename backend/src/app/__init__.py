from fastapi import FastAPI

from authentication.adapters.outgoing.memory import InMemoryUserRepository
from authentication.domain.service.auth import AuthenticationService

app = FastAPI()
user_repository = InMemoryUserRepository()
auth_service = AuthenticationService(user_repository)
