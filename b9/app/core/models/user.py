# Bảng users
from config.database import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.models.post import PostDTO
from typing import List


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    yob = Column(Integer, nullable=True)
    posts: Mapped[list["Post"]]	= relationship(back_populates="author")


# DTO của model.
class UserDTO(BaseModel):
	id: int
	name: str
	yob: int
	posts: List[PostDTO] = []

	class Config:
		from_attributes = True

# pydantic list relationship type define