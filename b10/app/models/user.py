# MODEL + DTO
from config.database import Base
from sqlalchemy import  Column, Integer,String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Mapped
from pydantic import BaseModel
from datetime import datetime

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default= func.now()) # timestamp
    orders:Mapped[list["Order"]] = relationship(back_populates="user")


class ListUserDTO(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        from_attributes= True