# enum z wszystkimi błędami
from enum import Enum
from fastapi import status

class Result(Enum):
    UNSUPPORTED_EXCEPTION = {
        "status_code": status.HTTP_501_NOT_IMPLEMENTED,
        "title": "Not Implemented",
        "detail": "Operation not supported."
    }
    BAD_REQUEST = {
        "status_code": status.HTTP_400_BAD_REQUEST,
        "title": "Bad Request",
        "detail": "Dividing by zero is not allowed"
    }