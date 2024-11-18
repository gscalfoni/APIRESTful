from fastapi import APIRouter, HTTPException, status, Body, Query
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId
from typing import Annotated, Optional

from database import collection
from models.products import Product
from serializer.product import listProducts, convertIdToString
from FASTAPIdoc.productDOC import put_exemples, response_getAll, response_creat, response_getID, response_exclude, response_filter

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)


@router.get("/preco",
            responses=response_filter,
            status_code=status.HTTP_200_OK)
async def filter_by_price(min : float = Query(..., gt=0), max : float = Query(..., gt =0)):
    if min>max:
        raise HTTPException (status_code=400, detail={"Erro": "O mínimo deve ser menor que o máximo", "Código de erro": 400})
    list = listProducts(collection.find())
    filteredList  = []
    for produto in list:
            if produto["preco"] >= min and produto["preco"] < max:
                filteredList.append(produto)
    return(filteredList)

@router.get("/qtd",
            responses=response_filter,
            status_code=status.HTTP_200_OK)
async def filter_by_qtd( max : int, min : Optional[int] = Query(0, ge = 0)):
    if min>max:
        raise HTTPException (status_code=400, detail={"Erro": "O mínimo deve ser menor que o máximo", "Código de erro": 400})
    list = listProducts(collection.find())
    filteredList  = []
    for produto in list:
            if produto["quantidade"] > min and produto["quantidade"] <= max:
                filteredList.append(produto)
    return(filteredList)


@router.get("", 
         status_code=status.HTTP_200_OK,
         responses=response_getAll,
         description="Este endpoint retorna todos os produtos cadastrados")
async def get_All_Products():
    list = listProducts(collection.find())
    return list



@router.post("",
          status_code=status.HTTP_201_CREATED,
          responses=response_creat,
          description="Este endpoint cria um novo produto e retorna seu ID")
async def creat_Product(*,
                        product: Annotated[Product, Body(openapi_examples=put_exemples)]
    ):
    new_product = collection.insert_one(dict(product))
    return{
    "id do produto criado" : str(new_product.inserted_id),
    }



@router.get("/{id}",
         status_code=status.HTTP_200_OK, 
         response_model=Product,
         responses=response_getID,
         description="Este endpoint retorna apenas um produtos, encontrado a partir do seu ID") 
async def get_One_Product(id : str):
    try:
        productID = ObjectId(id)
        product = collection.find_one({"_id" : productID})
        return(convertIdToString(product))
    except Exception as e:
        raise HTTPException(status_code=404, detail={"Erro": "ID não encontrado", "Código de erro": 404})



@router.put("/{id}", 
         status_code=status.HTTP_200_OK,
         responses=response_getID,
         description="Este endpoint atualiza apenas um produto a partir do seu ID e retorna e produto atualizado")
async def update_Product(*,
                        id : str,
                        updateInfos: Annotated[Product, Body(openapi_examples=put_exemples)]
):
    try:
        productID = ObjectId(id)
        product = collection.find_one_and_update({"_id" : productID}, 
                                                    {"$set" : dict(updateInfos)},
                                                    return_document= ReturnDocument.AFTER)
        return(convertIdToString(product))          
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"Erro": "ID não encontrado", "Código de erro": 404})
    



@router.delete("/{id}", 
            status_code=status.HTTP_204_NO_CONTENT,
            responses= response_exclude,
            description="Este endpoint exclui apenas um produto a partir do seu ID e retorna o produto excluido")
async def delete_One_Product(id: str):
    try:
        productID = ObjectId(id)
        product = collection.find_one_and_delete({"_id" : productID})
        return({"Produto excluido com sucesso"})

    except Exception as e:
        raise HTTPException(status_code=404, detail={"Erro": "ID não encontrado", "Código de erro": 404})
    
