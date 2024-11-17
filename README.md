# FastAPI - APIRESTful

API RESTful desenvolvida com FastAPI e Atlas MongoDB para o gerenciamento de produtos, incluindo uma autenticação básica para o acesso dos endpoints

Para clonar este repositório, use o seguinte comando:
`git clone hhttps://github.com/gscalfoni/APIRESTful.git
`

Abra um novo terminal do Visual Studio Code na pasta principal do projeto ('APIRESTful'), e crie uma maquina virtual (.venv). O módulo venv já vem instalado a partir do Python 3.3.

Crie a venv com `python -m venv venv`. Para ativar o ambiente virtual:

- Windows: `venv\Scripts\activate`
OBS: Caso aconteça o erro `"Cannot be loaded because running scripts is disabled on this system”`, abra o PowerShell e rode ` PS C:\>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`. Acredito que isso resolverá o problema.

- Linux: `source venv/bin/activate`

Para instalar as depêndencias após a ativação da máquina virtual, rode `pip install -r requirements.txt`

Em seguida, para rodar a API, digite `uvicorn main:app --reload`

Vá para o link gerado ou para o link da documentação da API(http://127.0.0.1:8000/docs), onde é possível ver todos os endpoints e fazer testes ali mesmo.


