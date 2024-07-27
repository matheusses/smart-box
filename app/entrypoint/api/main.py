from app.entrypoint.api.v1 import router as v1_router
from fastapi import FastAPI


app = FastAPI()
app.include_router(v1_router)