# MODEL + DTO
from config.database import Base
from sqlalchemy import  Column, Integer,String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.types import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from pydantic import BaseModel
from datetime import datetime

class OrderItem(Base):
    __tablename__= 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey("orders.id"), nullable=False)
    product_id = Column(ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    snapshot_price = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default= func.now()) # timestamp

    # relationship method
    order: Mapped["Order"] = relationship(back_populates="items")
    # product: Mapped["Product"] = relationship(back_populates="order_items")



class ListOrderItemDTO(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    snapshot_price: int
    created_at: datetime

    class Config:
        from_attributes= True