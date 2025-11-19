# metoda do generowania JSONa z problem details
from fastapi.encoders import jsonable_encoder
from fastapi import status
from starlette.responses import JSONResponse

from .error import Result
# from ..model import CalcIn, CalcOut, ErrorResponse


from src.model.models import CalcIn, CalcOut, ErrorResponse


def build_problem_details(result: Result) -> JSONResponse:
    response = ErrorResponse(status = result.value['status_code'], title = result.value['title'], detail=  result.value['detail'])
    headers = {"Content-Type": "application/problem+json"}
    return JSONResponse(status_code = response.status, headers = headers, content = jsonable_encoder(response))

def build_calc_out(result: float) -> JSONResponse:
    response = CalcOut(result = result)
    headers = {"Content-Type" : "application/problem+json"}
    return JSONResponse(content = jsonable_encoder(response), headers = headers, status_code = status.HTTP_200_OK)