from app import app, authService


@app.post("/auth/login")
async def login():
    authService.attempt_authentication()


@app.put("/auth/register")
async def register_new_user():
    authService.register_new_user()
