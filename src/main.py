from fastapi import FastAPI
from starlette.responses import JSONResponse

from src.model import CalcIn, UnsupportedOpException, BadRequestException

from src.utils import build_problem_details, Result
from src.api import calc_api

app = FastAPI(title = "Calculator API")
app.include_router(calc_api.router)

@app.get("/")
async def root():
    return {"info" : "Calculator API - available: PUT /kalkulator"}


# Wyjątek - operacja nieobsługiwana
@app.exception_handler(UnsupportedOpException)
async def unsupported_exception_handler(request: CalcIn, exc: UnsupportedOpException) -> JSONResponse:
    return build_problem_details(Result.UNSUPPORTED_EXCEPTION)

#Wyjątek - dzielenie przez 0
@app.exception_handler(BadRequestException)
async def bad_request_handler(request: CalcIn, exc: BadRequestException) -> JSONResponse:
    return build_problem_details(Result.BAD_REQUEST)