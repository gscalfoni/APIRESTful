from pydantic import BaseModel, Field

class User(BaseModel):
    nome_usuario: str
    senha: str




