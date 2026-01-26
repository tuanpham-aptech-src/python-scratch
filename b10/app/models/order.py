# MODEL + DTO
from config.database import Base
from sqlalchemy import  Column, Integer,String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.types import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from pydantic import BaseModel
from datetime import datetime
from enum import Enum

# new / processing / completed / cancelled

class Status(Enum):
    NEW = 'new'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class Order(Base):
    __tablename__= 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    note = Column(String(256), nullable=True)
    status  = Column(SqlEnum(Status), nullable=False, default='new')
    created_at = Column(DateTime, nullable=False, default= func.now()) # timestamp

    # relationship method
    user: Mapped["User"] = relationship(back_populates="orders")
    items:Mapped[list["OrderItem"]] = relationship(back_populates="order")



class ListOrderDTO(BaseModel):
    id: int
    note: str
    status: str
    created_at: datetime

    class Config:
        from_attributes= True