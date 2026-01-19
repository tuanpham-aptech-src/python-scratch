from app.core.request.BaseAPIRequest import BaseAPIRequest
from app.core.models.Product import Product

class CreateProductRequest(BaseAPIRequest, Product):

    def validate(self):
        if self.price <= 0:
            raise SystemError()