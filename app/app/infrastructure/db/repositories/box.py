from asyncio.log import logger
from datetime import datetime
from typing import Optional
from abc import ABC, abstractmethod
from app.domain.box import Box
from app.domain.exceptions.application import ApplicationError
from sqlalchemy import JSON, bindparam, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncEngine



class BoxRepository(ABC):

    @abstractmethod
    def create(self, box: Box) -> Box:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Box | None:
        pass

    @abstractmethod
    def list(self, text_search: Optional[str] = None) -> list[Box]:
        pass

    @abstractmethod
    def delete(self, box_id: int) -> bool:
        pass



class BoxPostgresRepository(BoxRepository):

    def __init__(self, db: AsyncEngine):
        self.db = db

    async def create(self, box: Box) -> Box:
        try:
            stmt = text(
                """
                INSERT INTO
                box(
                    name,
                    created_at
                    
                    )
                VALUES (
                    :name,
                    :created_at,
                    )
                RETURNING
                    id, name, created_at, updated_at
                """
            ).bindparams(
                name=box.name,
                created_at = datetime.now()
            )
            async with self.db.connect() as conn:
                result = await conn.execute(stmt)
                row = result.one()
                return Box.model_validate(dict(row._mapping))

        except SQLAlchemyError as e:
            message = "Fail to insert quote in database"
            logger.error(message)
            raise ApplicationError(message, cause=e) from e


    async def get_by_id(self, id: int) -> Box | None:
        try:
            stmt = text(
                """
                SELECT
                    id, name, created_at, updated_at
                FROM
                    box
                WHERE
                    id = :id;
                """
            ).bindparams(id=id)

            async with self.db.connect() as conn:
                result = await conn.execute(stmt)
                box_row = result.fetchone()

                if box_row is None:
                    return None

                return Box(**box_row._mapping)

        except SQLAlchemyError as e:
            message = "Fail to get quote by uuid in database"
            logger.exception(message)
            raise ApplicationError(message, cause=e) from e            
        
    async def list(self, text_search: Optional[str] = None):
        try:
            stmt = text(
                """
                SELECT
                    id, name, created_at, updated_at
                FROM
                    box
                WHERE
                    name is null or (name is not null and name = :text_search);
                """
            ).bindparams(text_search=text_search)
            async with self.db.connect() as conn:
                result = await conn.execute(stmt)
                rows = await result.fetchall()
                return [Box(**row._mapping) for row in rows]
        except SQLAlchemyError as e:
            message = "Failed to get configuration set"
            logger.exception(message)
            raise ApplicationError(message, cause=e) from e


    async def delete(self, box_id: int) -> bool:
            query = """
                DELETE FROM box WHERE id = :box_id
            """
            stmt = text(query).bindparams(box_id=box_id)
            
            try:
                async with self.db.connect() as conn:
                    await conn.execute(stmt)
                    await conn.commit()  
                    return True
            except SQLAlchemyError as e:
                message = f"Failed to delete box with id {box_id}"
                logger.exception(message)
                raise ApplicationError(message, cause=e) from e


