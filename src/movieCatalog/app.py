from fastapi import FastAPI

from .api import router

app = FastAPI(
    title='Movie catalog'
)

app.include_router(router)
