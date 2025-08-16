from datetime import datetime, timedelta, timezone

import jwt

from authentication.adapters.incoming.config import settings


def create_access_token(user: str) -> str:
    expiration = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode = {"nbf": datetime.now(timezone.utc), "exp": expiration, "sub": str(user)}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
