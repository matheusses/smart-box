from app.entrypoint.api.v1 import box_router
from fastapi import FastAPI


app = FastAPI()
app.include_router(box_router)
