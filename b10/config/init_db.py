
from config.database import Base, engine
import app.models.user
import app.models.product
import app.models.order
import app.models.order_item


Base.metadata.create_all(bind=engine)