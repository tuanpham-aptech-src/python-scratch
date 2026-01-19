from app.core.api.BaseAPIResponse import BaseAPIResponse
class SuccessResponse(BaseAPIResponse):
    status_code:int = 200

class BadRequestResponse(BaseAPIResponse):
    status_code:int = 400

class NotFoundResponse(BaseAPIResponse):
   status_code:int = 404

# class UnauthorizedResponse(BaseAPIResponse):
#     def __init__(self,  message, data=None):
#         super().__init__(403, message, data)