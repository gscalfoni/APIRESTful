from pydantic import BaseModel, Field

class Product(BaseModel):
    nome: str
    descricao: str
    preco: float = Field(..., gt=0)
    quantidade: int = Field(..., ge=0)




