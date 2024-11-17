def convertIdToString(product):
    return{
        "id": str(product["_id"]),
        "nome": product["nome"],
        "descricao": product["descricao"],
        "preco": product["preco"],
        "quantidade": product["quantidade"] 
    }

def listProducts(product_list):
    converted_list = []
    for product in product_list:
        converted_list.append(convertIdToString(product))
    return converted_list
