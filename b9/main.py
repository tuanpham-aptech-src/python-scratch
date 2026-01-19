from fastapi import FastAPI, Depends
from app.core.api.Response import SuccessResponse, BadRequestResponse, NotFoundResponse
from config.database import Base, engine, SessionLocal

from app.core.models.post import Post, PostDTO
from app.core.models.user import User, UserDTO

from sqlalchemy.orm import Session, selectinload, joinedload
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

# api lấy danh sách user
@app.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).filter().all() # đây là data trả từ Db.
    users_dto = [] # chuẩn hóa toàn bộ data về chung một dạng
    # query = 1 (users) + 1 (posts)
    for user in users:
        users_dto.append(UserDTO.model_validate(user))
    return SuccessResponse(message='Get list users success!',data={"users": users_dto}).response()

@app.get("/eager-selectinload")
def home(db: Session = Depends(get_db)):
    users = (
        db.query(User)
        .options(selectinload(User.posts))
        .all()
    )

    users_dto = []
    for user in users:
        users_dto.append(UserDTO.model_validate(user))
    return SuccessResponse(message='Get list users success!',data={"users": users_dto}).response()

@app.get("/eager-joinedload")
def home(db: Session = Depends(get_db)):
    users = (
        db.query(User)
        .options(joinedload(User.posts))
        .all()
    )

    users_dto = []
    for user in users:
        users_dto.append(UserDTO.model_validate(user))
    return SuccessResponse(message='Get list users success!',data={"users": users_dto}).response()


@app.post('/seed-users')
def seed_user(db: Session = Depends(get_db)):
    users = [
        User(name='Nguyễn Văn A', yob= 2006),
        User(name='Trần Văn B', yob= 2006),
        User(name='Võ Ngọc C', yob= 2006)
    ]

    db.add_all(users)
    db.commit()
    return SuccessResponse(message='Seed users success!').response()

@app.post('/seed-posts')
def seed_post(db: Session = Depends(get_db)):
    users = db.query(User).filter().all()
    posts = []
    for user in users:
        posts.append(
            Post(title=f"Post đầu tiên của user {user.id}", author_id=user.id)
            )
        posts.append(
            Post(title=f"Post thứ hai của user {user.id}", author_id=user.id)
            )

    db.add_all(posts)
    db.commit()
    return SuccessResponse(message='Seed posts success!').response()

@app.post("/seed-total")
def seed_post(db: Session = Depends(get_db)):
    # seed 1 user + 2 post tương ứng
    user = User(name="Tào Thao", yob = 2006)
    db.add(user)
    db.commit()
    post = Post(title="Post này tạo total", author_id=user.id)
    db.add(post)
    db.commit()

    return SuccessResponse(message='Seed total success!').response()

Base.metadata.create_all(bind=engine)

# python object to json

# DTO = Data - Object
# ORM = Models -> Object

# ENUM





# 2026-01-19 20:50:33,057 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2026-01-19 20:50:33,059 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.yob AS users_yob
# FROM users
# 2026-01-19 20:50:33,062 INFO sqlalchemy.engine.Engine [generated in 0.00341s] {}
# 2026-01-19 20:50:33,070 INFO sqlalchemy.engine.Engine SELECT posts.id AS posts_id, posts.title AS posts_title, posts.author_id AS posts_author_id
# FROM posts
# WHERE %(param_1)s = posts.author_id
# 2026-01-19 20:50:33,075 INFO sqlalchemy.engine.Engine [generated in 0.00582s] {'param_1': 1}
# 2026-01-19 20:50:33,084 INFO sqlalchemy.engine.Engine SELECT posts.id AS posts_id, posts.title AS posts_title, posts.author_id AS posts_author_id
# FROM posts
# WHERE %(param_1)s = posts.author_id
# 2026-01-19 20:50:33,085 INFO sqlalchemy.engine.Engine [cached since 0.01636s ago] {'param_1': 2}
# 2026-01-19 20:50:33,086 INFO sqlalchemy.engine.Engine SELECT posts.id AS posts_id, posts.title AS posts_title, posts.author_id AS posts_author_id
# FROM posts
# WHERE %(param_1)s = posts.author_id
# 2026-01-19 20:50:33,086 INFO sqlalchemy.engine.Engine [cached since 0.0174s ago] {'param_1': 3}
# 2026-01-19 20:50:33,087 INFO sqlalchemy.engine.Engine SELECT posts.id AS posts_id, posts.title AS posts_title, posts.author_id AS posts_author_id
# FROM posts
# WHERE %(param_1)s = posts.author_id
# 2026-01-19 20:50:33,087 INFO sqlalchemy.engine.Engine [cached since 0.01811s ago] {'param_1': 6}

# 4 users = 1(users) + 4(posts) = n + 1 
# n users = 1(users) + n(posts)

# joinonload
# 1 - join các table với nhau

# selectonload
# 1 (users) + 1(posts)


# 2026-01-19 20:59:35,221 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.yob AS users_yob
# FROM users

# 2026-01-19 20:59:35,223 INFO sqlalchemy.engine.Engine SELECT posts.author_id AS posts_author_id, posts.id AS posts_id, posts.title AS posts_title
# FROM posts
# WHERE posts.author_id IN (%(primary_keys_1)s, %(primary_keys_2)s, %(primary_keys_3)s, %(primary_keys_4)s, %(primary_keys_5)s, %(primary_keys_6)s, %(primary_keys_7)s, %(primary_keys_8)s, %(primary_keys_9)s, %(primary_keys_10)s)

# 2026-01-19 21:01:18,622 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.yob AS users_yob, posts_1.id AS posts_1_id, posts_1.title AS posts_1_title, posts_1.author_id AS posts_1_author_id
# FROM users LEFT OUTER JOIN posts AS posts_1 ON users.id = posts_1.author_id