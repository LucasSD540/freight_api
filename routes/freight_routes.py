from fastapi import APIRouter
from app.schemas import FreightRequest, FreightResponse
from app.services import calculate_freight

router = APIRouter(prefix="/freight")

@router.post("/calculate/", response_model=FreightResponse)
def calculate(request: FreightRequest):
  return calculate_freight(request)
