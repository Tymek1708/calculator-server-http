# # metoda do generowania JSONa z problem details
# from fastapi.encoders import jsonable_encoder
# from starlette.responses import JSONResponse
# from .error import Result, ErrorResponse
#
#
# def build_problem_details(result: Result) -> JSONResponse:
#     response = ErrorResponse(status= result.value['status_code'], title= result.value['title'], detail=result.value['detail'])
#     headers = {"Content-Type": "application/problem+json"}
#     return JSONResponse(status_code=response.status, headers=headers, content=jsonable_encoder(response))