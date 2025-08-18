from app import app, auth_service
from authentication.domain.model.user import User


@app.post("/auth/login")
async def login(user: User):
    return auth_service.attempt_authentication(user)


@app.post("/auth/register")
async def register_new_user(user: User):
    auth_service.register_new_user(user)
