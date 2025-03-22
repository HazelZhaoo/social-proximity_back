from pydantic import BaseModel
from models.Database import Base
from sqlalchemy import Boolean, Column, Integer, String

class UserModel(Base):
    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    
class UserViewModel(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_active: bool = True
    
class UserCreateRequest(BaseModel):
    username: str
    email: str
    
class UserCreateResponse(BaseModel):
    user_id: str
    username: str
    email: str
    