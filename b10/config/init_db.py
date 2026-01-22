
from config.database import Base, engine
import app.models.user


Base.metadata.create_all(bind=engine)