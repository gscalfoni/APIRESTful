put_exemples = {
    "normal": {
        "summary": "Exemplo normal",
        "description": "Endpoint funciona corretamente",
        "value": {
            "nome": "Caderno",
            "descricao": "Um caderno de 96 folhas",
            "preco": 10.30,
            "quantidade": 10
        }
    },
    "invalid": {
        "summary": "Exemplo inválido",
        "description": "Erro: Formatos não compatíveis",
        "value": {
            "nome": "Caderno",
            "descricao": "Um caderno de 96 folhas",
            "preco": 10.30,
            "quantidade": 10.5  # Valor inválido
        }
    }
}


tags_metadata = [
    {
        "name": "Produtos",
        "description": "CRUD básico para produtos",
    },
    {
        "name": "Root",
        "description" : ""
    }
]


response_getAll={
        200: {
            "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "_id" : "00000000000",
                        "nome": "Caderno",
                        "descricao": "Um caderno de 96 folhas",
                        "preco": 10.30,
                        "quantidade": 10
                        }
                    },
            },
        },
    }

response_creat = {
    201:{
        "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "id do produto criado": "00000000000000000000"
                        }
                    },
            },
    },
    422:{
        "description": "Error: Unprocessable Entity",
            "content": {
                "application/json": {
                    "example": {
                        "Erro": "Formatos não compatíveis",
                        "Código de Erro": 422
                        }
                    },
            },
        
    }
}

response_getID = {
    200:{
        "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "nome": "Lápis",
                        "descricao": "Lápis de sapo",
                        "preco": 5,
                        "quantidade": 37
                    }
                },
            },
    },
    422:{
        "description": "Error: Unprocessable Entity",
            "content": {
                "application/json": {
                    "example": {
                        "Erro": "Formatos não compatíveis",
                        "Código de Erro": 422
                        }
                    },
            },
        
    },
    404:{
        "description": "Erro de ID",
            "content": {
                "application/json": {
                    "example": {
                        "Erro": "ID não encontrado",
                        "Código de Erro": 404
                        }
                    },
            },
        
    }
}

response_exclude = {
    204:{
        "description": "Sucesso, item excluido",
            "content": {
                "application/json": {
                },
            },
    },
    422:{
        "description": "Error: Unprocessable Entity",
            "content": {
                "application/json": {
                    "example": {
                        "Erro": "Formatos não compatíveis",
                        "Código de Erro": 422
                        }
                    },
            },
        
    },
    404:{
        "description": "Erro de ID",
            "content": {
                "application/json": {
                    "example": {
                        "Erro": "ID não encontrado",
                        "Código de Erro": 404
                        }
                    },
            },
        
    }
}

response_filter = {
    200:{
        "description": "Sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "_id" : 000000000000000000,
                        "nome": "Lápis",
                        "descricao": "Lápis de sapo",
                        "preco": 5,
                        "quantidade": 37
                    }
                },
            },
    },
    400:{
        "description": "Error: Bad Request",
            "content": {
                "application/json": {
                    "example": {
                        "Erro": "O mínimo deve ser menor que o máximo",
                        "Código de Erro": 400
                        }
                    },
            },
        
    },
    422:{
        "description": "Error: Unprocessable Entity",
            "content": {
                "application/json": {
                    "example": {
                        "Erro": "Formatos não compatíveis",
                        "Código de Erro": 422
                        }
                    },
            },
        
    }
}
