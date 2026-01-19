# Bảng posts
from config.database import Base
from sqlalchemy import ForeignKey,Column, Integer, String
from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="posts")

# DTO của model.
class PostDTO(BaseModel):
	id: int
	title: str

	class Config:
		from_attributes = True