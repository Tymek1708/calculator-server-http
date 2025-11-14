# from fastapi import status
# from fastapi.encoders import jsonable_encoder
# from starlette.responses import JSONResponse
#
# from src.model.models import CalcOut, CalcIn
# from src.services.calc import calc
#
# def build_calc_out(request: CalcIn) -> JSONResponse:
#     result = calc(request.op, request.num1, request.num2)
#     response = CalcOut(result=result)
#     headers= {"Content-Type" : "application/problem+json"}
#     return JSONResponse(content=jsonable_encoder(response), headers=headers, status_code=status.HTTP_200_OK)