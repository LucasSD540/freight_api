from app.schemas.freight_schema import FreightRequest, FreightResponse

def calculate_distance(cep_origem: str, cep_destino: str) -> int:
    if cep_origem[:3] == cep_destino[:3]:
        return 10
    elif cep_origem[:2] == cep_destino[:2]:
        return 50
    else:
        return 300


def calculate_freight(request: FreightRequest) -> FreightResponse:
  distance = calculate_distance(request.cep_origem, request.cep_destino)

  base = 5.0
  km_cost = 0.1
  weight_cost = 2.0

  freight_value = base + (distance * km_cost) + (request.peso_total * weight_cost)

  if distance == 10:
      time = 3
  elif distance == 50:
      time = 8
  elif distance == 300:
      time = 15
  else:
      time = 20

  return FreightResponse(valor_frete=round(freight_value, 2), prazo_dias=time)
