from pydantic import BaseModel, Json
from typing import Any

class CalcIn(BaseModel):
    num1: float
    op: str
    num2: float

class CalcOut(BaseModel):
    result: float

class UnsupportedOpException(Exception):
    def __init__(self, name: str):
        self.name = name

class BadRequestException(Exception):
    def __init__(self, name: str):
        self.name = name