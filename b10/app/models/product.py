# MODEL + DTO
from config.database import Base
from sqlalchemy import  Column, Integer,String, DateTime
from sqlalchemy.sql import func
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.types import Enum as SqlEnum
from enum import Enum

class Status(Enum):
    ACTIVE = 'active'
    DEACTIVE = 'deactive'

class Product(Base):
    __tablename__= 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)
    price = Column(Integer, nullable=False, default=0)
    stock_qty = Column(Integer, nullable=False, default=0)
    status  = Column(SqlEnum(Status), nullable=False, default='active')
    created_at = Column(DateTime, nullable=False, default= func.now()) # timestamp


class ListProductDTO(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes= True


class CreateProductDTO(BaseModel):
    name: str
    price: int
    stock_qty: int


class RestockProductDTO(BaseModel):
    stock_qty: int