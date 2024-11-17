response_singup = {
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
    400:{
        "description": "Erro de credenciais",
            "content": {
                "application/json": {
                    "example": {
                        "Erro": "Usuário já existe",
                        "Código de Erro": 400
                        }
                    },
            },
    }
}

response_token = {
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
    401:{
        "description": "Usuário ou senha inválidos",
            "content": {
                "application/json": {
                    "example": {
                        "Erro": "Usuário ou senha inválidos",
                        "Código de Erro": 401
                        }
                    },
            },
        
    },

    }



