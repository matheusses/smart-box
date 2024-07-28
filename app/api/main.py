from app.api.v1 import router as box_router
from fastapi import FastAPI


app = FastAPI()
app.include_router(box_router)
