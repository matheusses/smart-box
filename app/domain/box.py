from datetime import datetime
from pydantic import BaseModel


class Box(BaseModel):
    id: int 
    name: str
    created_at: datetime
    update_at: datetime | None = None
    