from abc import ABC, abstractmethod
from app.domain.box import Box
from app.infrastructure.db.repositories.box_repository import BoxRepository

class BoxBaseService(ABC):
    @abstractmethod
    async def create_box(name :str)->Box:
        pass


class BoxService():
    def __init__(
        self,
        box_repository: BoxRepository
    ):
        self._box_repository = box_repository

    async def create_box(self, name: str)->Box:
        box = Box(
            name=name
        )
        return await self._box_repository.create(box)