from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.services import operation_is_valid, div_by_zero
from src.model import CalcIn, UnsupportedOpException, BadRequestException
from src.utils import build_calc_out

router = APIRouter()

@router.put("/kalkulator")
async def calc_op(request: CalcIn) -> JSONResponse:
    op = request.op
    # Operacja nieobsługiwana
    if not operation_is_valid(op):
        raise UnsupportedOpException(name=op)

    # Dzielenie przez 0
    if div_by_zero(op, request.num2):
        raise BadRequestException(name="Bad request")

    return build_calc_out(request)