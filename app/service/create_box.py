from app.domain.box import Box
from app.infrastructure.db.repositories.box_repository import BoxRepository



class BoxService:
    def __init__(
        self,
        box_repository: BoxRepository
    ):
        self._box_repository = box_repository

    async def create_box(
        self,
        name: str
    )-> Box:
        box = Box(
            name=name
        )
        return self._box_repository.create(box)