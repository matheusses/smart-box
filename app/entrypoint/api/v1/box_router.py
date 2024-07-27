from typing import Annotated
from app.core.container.app import Container
from app.entrypoint.api.dto.box import BoxCreateRequest, BoxCreateResponse
from app.entrypoint.api.openapi.examples import BoxCreateRequestExample
from app.service.create_box import BoxService
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends
from starlette import status


router = APIRouter()


@router.post(
    "",
    response_model=BoxCreateResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Returns box information with the external id."},
        status.HTTP_400_BAD_REQUEST: {"description": "Invalid request"},
    },
)
@inject
async def create_box(
    request: Annotated[
        BoxCreateRequest,
        Body(
            ...,
            openapi_examples={
                "box": {
                    "summary": "Register box",
                    "description": "Example demonstrating the box registration with "
                    "required input parameters.",
                    "value": {'name':'teste'},
                }
            },
        ),
    ],
    box_service: BoxService = Depends(Provide[Container.box_service]),
) -> BoxCreateResponse:
        quote = await box_service.create_box(
            name=request.name
        )
        return BoxCreateResponse(quote_uuid=quote.uuid, expected_total=quote.expected_total)
