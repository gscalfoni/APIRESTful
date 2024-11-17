from fastapi import FastAPI, Request, Depends
from pymongo.mongo_client import MongoClient
from routes import produtos, users

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from routes.users import get_current_user

app = FastAPI(
    title="FastAPI - APIRESTful",
    description="""API RESTful desenvolvida com FastAPI e Atlas MongoDB para o gerenciamento de produtos, incluindo uma autenticação básica para o acesso dos endpoints""",
    )    


#Atlas MongoDB conection
uri = "mongodb+srv://Username:RL6wMc7Htct82yaS@cluster0.5h9vq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


PROTECTED = [Depends(get_current_user)]
app.include_router(produtos.router,
                   dependencies=PROTECTED)

app.include_router(users.router)


@app.get("/", tags=["Root"])
async def read_root():
    return {"Funcinou!!"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({
            "Erro": "Formatos não compatíveis",
            "Código de Erro": 422
        }),
    )
