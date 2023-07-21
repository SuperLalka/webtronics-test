import os


class Config:
    AUTHJWT_SECRET_KEY = os.getenv("AUTHJWT_SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
    AUTHJWT_ALGORITHM = os.getenv("AUTHJWT_ALGORITHM", "HS256")
    AUTHJWT_ACCESS_TOKEN_EXPIRE = os.getenv("AUTHJWT_ACCESS_TOKEN_EXPIRE", 30 * 60)
    AUTHJWT_REFRESH_TOKEN_EXPIRE = os.getenv("AUTHJWT_REFRESH_TOKEN_EXPIRE", 24 * 60 * 60)
    AUTHJWT_TOKEN_LOCATION = os.getenv("AUTHJWT_TOKEN_LOCATION", {"cookies"})
    AUTHJWT_COOKIE_CSRF_PROTECT = os.getenv("AUTHJWT_COOKIE_CSRF_PROTECT", False)

    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")

    DATABASE_URL = f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    DATABASE_URL_ASYNC = "postgresql+asyncpg://" + DATABASE_URL
    DATABASE_URL_SYNC = "postgresql://" + DATABASE_URL