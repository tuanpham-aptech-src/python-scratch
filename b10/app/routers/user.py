from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from config.database import get_db
from app.models.user import User

router = APIRouter(prefix="/users", tags=['users'])

@router.get("")
def get_all(search = "",db:Session = Depends(get_db)):
    query = db.query(User)
    if search:
        # sử dụng or_: or_(s1, s2, ....)
        query = query.filter(or_(
            User.name.ilike(f"%{search}%"),
            User.email.ilike(f"%{search}%")
        )) # gán lại giá trị sau khi update
    # like, ilike
    users = query.all()
    
    return {
            "message": "Danh sách người dùng",
            "users": users
            }

@router.get("/{user_id}")
def get_all(user_id,db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first() # filter_by
    
    return {
            "message": "Chi tiết người dùng",
            "user": user
            }

@router.post("/seed")
def seed_users(db:Session = Depends(get_db)):
    users = []

    # thêm từng đối tượng vào list users
    for i in range(10):
        users.append(User(name=f"Người dùng thứ {i+1}", email=f"userexample_{i+1}@gmail.com"))

    db.add_all(users) # dùng add_all để thêm 1 list users
    db.commit()
    return {
            "message": "Seed user thành công",
            }