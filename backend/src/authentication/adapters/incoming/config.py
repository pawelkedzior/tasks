import os

from dotenv import load_dotenv

load_dotenv()


class JWTSettings:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"


settings: JWTSettings = JWTSettings()
