from app.api.v1.openapi.examples import BoxCreateRequestExample, BoxCreateResponseExample
from pydantic import BaseModel, ConfigDict

class BoxCreateRequest(BaseModel):
    model_config = ConfigDict(extra="ignore", json_schema_extra={})
    name : str



class BoxCreateResponse(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        json_schema_extra={},
    )
    name : str   

