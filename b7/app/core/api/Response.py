from app.core.api.BaseAPIResponse import BaseAPIResponse

class SuccessResponse(BaseAPIResponse):
    def __init__(self, message, data=None):
        super().__init__(200, message, data)

class BadRequestResponse(BaseAPIResponse):
    def __init__(self,  message, data=None):
        super().__init__(400, message, data)

class NotFoundResponse(BaseAPIResponse):
    def __init__(self,  message, data=None):
        super().__init__(404, message, data)

class UnauthorizedResponse(BaseAPIResponse):
    def __init__(self,  message, data=None):
        super().__init__(403, message, data)