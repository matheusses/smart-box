from typing import Optional
from dataclasses import dataclass
from sqlalchemy.orm import Session
from src.app.infrastructure.db.engine import get_db
from src.app.infrastructure.db.models.user import UserModel
from src.app.infrastructure.db.ports import UserInterface

@dataclass
class UserDatabaseRepository(UserInterface):

    __database: Session = next(get_db())

    def create(self, name: str, age: int) -> UserModel:
        db_user = UserModel(
            name = name,
            age = age,
        
        )
        self.__database.add(db_user)
        self.__database.commit()
        self.__database.refresh(db_user)
        return db_user

    # TODO - filter and pagination
    def list(self, text_search: Optional[str] = None,
                    page: Optional[str] = 1) -> list[UserModel]:
        return [user.to_dict() for user in self.__database.query(UserModel).all() ]
    
    def get(self, user_id: int) -> UserModel:
        return self.__database.query(UserModel).filter(UserModel.id == user_id).first()
    
    def delete(self, user_id: int) -> bool:
        self.__database.query(UserModel).filter(UserModel.id == user_id).delete()
        self.__database.commit()
        return True