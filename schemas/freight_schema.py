from pydantic import BaseModel

class FreightRequest(BaseModel):
    cep_origem: str
    cep_destino: str
    peso_total: float
    valor_pedido: float

class FreightResponse(BaseModel):
    valor_frete: float
    prazo_dias: int
