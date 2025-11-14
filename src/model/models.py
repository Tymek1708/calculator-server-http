from pydantic import BaseModel

class CalcIn(BaseModel):
    num1: float
    op: str
    num2: float

class CalcOut(BaseModel):
    result: float

class ErrorResponse(BaseModel):
    status: int
    title: str
    detail: str