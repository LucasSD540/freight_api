from fastapi import APIRouter
from schemas import FreightRequest, FreightResponse
from services import calculate_freight

router = APIRouter(prefix="/freight")

@router.post("/calculate/", response_model=FreightResponse)
def calculate(request: FreightRequest):
  return calculate_freight(request)
