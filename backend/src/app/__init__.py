from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from authentication.adapters.outgoing.memory import InMemoryUserRepository
from authentication.domain.service.auth import AuthenticationService

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend origin here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_repository = InMemoryUserRepository()
auth_service = AuthenticationService(user_repository)
import authentication.adapters.incoming.controller
