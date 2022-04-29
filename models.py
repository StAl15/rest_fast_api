from typing import Optional, List #подсказка типов
from uuid import UUID, uuid4 
from pydantic import BaseModel #Проверка данных и управление настройками с использованием аннотаций типа Python.
from enum import Enum #Базовый класс для создания перечислимых констант. 

class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
    
    
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
    
class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]