from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Annotated
from passlib.context import CryptContext
from jose import jwt, JWTError

from database import user_collection
from models.users import User 
from FASTAPIdoc.userDOC import response_singup, response_token

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/user/token')



class CreateUser(BaseModel):
    nome_usuario : str
    senha : str

class Token(BaseModel):
    access_token : str
    type : str 


# Criação do token JWT
def create_access_token(user_name : str ):
    try:
        encode = {'sub' : user_name}
        return jwt.encode(encode, SECRET_KEY,algorithm=ALGORITHM)
    except Exception as e:
        raise HTTPException(status_code=500, detail="ERRO ao criar o Token")



@router.post("/singup", 
             status_code=status.HTTP_201_CREATED,
             responses = response_singup)
async def register_user(new_user: CreateUser):
    if user_collection.find_one({"nome_usuario": new_user.nome_usuario}):
        raise HTTPException(status_code=400, detail={
                        "Erro": "Usuário já existe",
                        "Código de Erro": 400
                        })

    create_user_model = User(
            nome_usuario = new_user.nome_usuario,
            senha = bcrypt_context.hash(new_user.senha)
    )
    user_collection.insert_one({"nome_usuario": create_user_model.nome_usuario, "senha": create_user_model.senha})
    return {"Sucesso": "Usuário criado com sucesso"}


@router.post("/token", 
             status_code=status.HTTP_200_OK,
             responses = response_token,
             response_model=Token)
async def login_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()] ):
    user = user_collection.find_one({"nome_usuario": form_data.username})
    if not user or not bcrypt_context.verify(form_data.password, user["senha"]):
        raise HTTPException(status_code=401, detail= {
                        "Erro": "Usuário ou senha inválidos",
                        "Código de Erro": 401})

    token = create_access_token(form_data.username)

    return {"access_token": token, "type": "bearer"}


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail={
                        "Erro": "Usuário não autenticado",
                        "Código de Erro": 401})
    except JWTError:
        raise HTTPException(status_code=401, detail={
                        "Erro": "Token inválido",
                        "Código de Erro": 401})

    user = user_collection.find_one({"nome_usuario": username})
    if user is None:
        raise HTTPException(status_code=404, detail={
                        "Erro": "Usuário não encontrado",
                        "Código de Erro": 401})
    return user
