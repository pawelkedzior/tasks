import jwt
from fastapi import HTTPException, Request, status
from jwt import InvalidTokenError

from app import app
from authentication.adapters.incoming.config import settings


@app.middleware("http")
async def authorise(request: Request, call_next):
    if "auth" not in request.base_url and not verify_token(
        request.headers.get("Authorization")
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return await call_next(request)


def verify_token(token: str) -> bool:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload.get("sub") is not None
    except InvalidTokenError:
        return False
