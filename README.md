# FastAPI - APIRESTful

API RESTful desenvolvida com FastAPI e Atlas MongoDB para o gerenciamento de produtos, incluindo uma autenticação básica para o acesso dos endpoints

Para clonar este repositório, use o seguinte comando:
`git clone hhttps://github.com/gscalfoni/APIRESTful.git
`
Estrutura do projeto:
APIRESTFUL
 ┣ FASTAPIdoc
 ┃ ┣ productDOC.py
 ┃ ┣ userDOC.py
 ┣ models
 ┃ ┣ products.py
 ┃ ┣ users.py
 ┣ routes
 ┃ ┣ produtos.py
 ┃ ┣ users.py
 ┣ serializer
 ┃ ┣ product.py
 ┣ database.py
 ┣ main.py

Abra um novo terminal do Visual Studio Code na pasta principal do projeto ('APIRESTful'), e crie uma máquina virtual (.venv). O módulo venv já vem instalado a partir do Python 3.3.

Crie a venv com `python -m venv venv`. Para ativar o ambiente virtual:

- Windows: `venv\Scripts\activate`
OBS: Caso aconteça o erro `"Cannot be loaded because running scripts is disabled on this system”`, abra o PowerShell e rode ` PS C:\>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`. Acredito que isso resolverá o problema.

- Linux: `source venv/bin/activate`

As principais dependências usadas no projeto incluem:
- FastAPI - Framework para construir APIs rápidas e eficientes.
- PyMongo - Cliente MongoDB para Python.
- Uvicorn - Servidor ASGI para rodar a aplicação.
Para instalar as dependências após a ativação da máquina virtual, rode `pip install -r requirements.txt`

Em seguida, para rodar a API, digite `uvicorn main:app --reload`

Vá para o link gerado ou para o link da documentação da API(http://127.0.0.1:8000/docs), onde é possível ver todos os endpoints e fazer testes ali mesmo.

Os endpoints disponíveis são
- Produtos
-   GET /produtos - Listar todos os produtos.
-   POST /produtos - Criar um novo produto.
-   GET /produtos/{id} - Listar um produto.
-   PUT /produtos/{id} - Atualizar um produto.
-   DELETE /produtos/{id} - Deletar um produto.
- Users
-   POST /user/singup - Cria novo usuário.
-   POST /user/token - Gera um token de autenticação.

O acesso de todos os endpoints de produtos é apenas possível com a autenticação.


