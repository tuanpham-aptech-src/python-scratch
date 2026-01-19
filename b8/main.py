from fastapi import FastAPI, Depends
from app.core.api.Response import SuccessResponse, BadRequestResponse, NotFoundResponse
from config.database import Base, engine, SessionLocal
from app.core.models.user import User
from sqlalchemy.orm import Session
import json


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return SuccessResponse(message='Welcome to FastAPI!')

@app.post('/seed')
def seed_data(db: Session = Depends(get_db)):
    # Tạo nhanh một user

    # validate nếu cần
    # mở một session -> Depends sẽ lo
    user = User(name='Anh Tuấn', yob= 1996) # user chỉ là 1 object của User
    # lưu lại data vào db -> đóng session
    db.add(user)
    db.commit()
    db.refresh(user) # user sẽ được làm mới và là data từ database
    # trả response cho client
    return SuccessResponse(message='Seed user success!',data={"user": user}).response()


Base.metadata.create_all(bind=engine)

# python object to json

# DTO = Data Transfer Object