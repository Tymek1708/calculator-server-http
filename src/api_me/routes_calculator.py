# from fastapi import APIRouter, status
# from fastapi.encoders import jsonable_encoder
# from starlette.responses import JSONResponse
#
#
# from src.models_me import CalcOut, CalcIn, UnsupportedOpException, BadRequestException
# from src.services_me import operation_is_valid, div_by_zero
# from src.utils.operation_utils import calc
#
#
# router = APIRouter(prefix="/kalkulator", tags=["Kalkulator"])
#
# # Wyjątek - operacja nieobsługiwana
# @router.exception_handler(UnsupportedOpException)
# async def unsupported_exception_handler(request: CalcIn, exc: UnsupportedOpException) -> JSONResponse:
#     return JSONResponse(
#         status_code=501,
#         content={"title":"Not Implemented", "detail":f"Operation {exc.name} not supported.", "status_code":501}
#     )
#
# #Wyjątek - dzielenie przez 0
# @router.exception_handler(BadRequestException)
# async def bad_request_handler(request: CalcIn, exc: BadRequestException) -> JSONResponse:
#     return JSONResponse(
#         status_code=400,
#         content={"title":"Bad Request", "detail":f"Dividing by zero is not allowed.", "status_code":400}
#     )
#
