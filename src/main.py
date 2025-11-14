from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from models_me import CalcOut, CalcIn, UnsupportedOpException, BadRequestException
from services_me import operation_is_valid, div_by_zero
from utils.operation_utils import calc

app = FastAPI(title="Calculator API")

@app.get("/items/")
async def root():
    return {"info":"Calculator API - available: PUT /kalkulator"}


# Wyjątek - operacja nieobsługiwana
@app.exception_handler(UnsupportedOpException)
async def unsupported_exception_handler(request: CalcIn, exc: UnsupportedOpException) -> JSONResponse:
    return JSONResponse(
        status_code = 501,
        content = {
            "title" : "Not Implemented",
            "detail" : f"Operation {exc.name} not supported.",
            "status_code" : 501}
    )

#Wyjątek - dzielenie przez 0
@app.exception_handler(BadRequestException)
async def bad_request_handler(request: CalcIn, exc: BadRequestException) -> JSONResponse:
    return JSONResponse(
        status_code = 400,
        content = {"title" : "Bad Request",
                   "detail" : f"Dividing by zero is not allowed.",
                   "status_code" : 400}
    )


@app.put("/kalkulator")
async def calc_op(request: CalcIn) -> JSONResponse:
    op = request.op
    # Operacja nieobsługiwana
    if not operation_is_valid(op):
        raise UnsupportedOpException(name=op)

    # Dzielenie przez 0
    if div_by_zero(op, request.num2):
        raise BadRequestException(name="Bad request")

    result = CalcOut(result=calc(request.op, request.num1, request.num2))
    headers= {"Content-Type":"application/problem+json"}
    return JSONResponse(content=jsonable_encoder(result), headers=headers, status_code=status.HTTP_200_OK)