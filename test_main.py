import pytest
from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnaW8ifQ.rORfFaoNyN_ZOk1guQ6lxijVMsoFG2BpfcPYOv3wgIw"
auth = {"Authorization": f"Bearer {token}"}
id = "673a85d377d2e8d617eeb880" # esse id só é valido na primeira vez que é testado, caso use-o uma segunda vez, a maioria dos testes falhará

def test_price():
    response = client.get("/produtos/preco?min=2&max=7", headers=auth)
    assert response.status_code == 200

def test_filter_by_price_invalid():
    response = client.get("/produtos/preco?min=10&max=7", headers=auth)
    assert response.status_code == 400


def test_qtd():
    response = client.get("/produtos/qtd?min=5&max=21", headers=auth)
    assert response.status_code == 200

def test_filter_by_qtd_invalid():
    response = client.get("/produtos/qtd?min=21&max=20", headers=auth)
    assert response.status_code == 400

def test_get_all():
    response = client.get("/produtos", headers=auth)
    assert response.status_code == 200

def test_get_one():
    response = client.get(f"/produtos/{id}", headers=auth)
    assert response.status_code == 200

def test_get_one_not_found():
    id = "0"
    response = client.get(f"/produtos/{id}", headers=auth)
    assert response.status_code == 404

def test_create():
    new_product = {
        "nome": "Produto Teste",
        "descricao" : "Apenas teste",
        "preco": 50.0,
        "quantidade": 10
    }
    response = client.post("/produtos", json=new_product, headers=auth)
    assert response.status_code == 201

def test_create_invalid():
    new_product = {
        "nome": "Produto Teste",
        "descricao" : "Apenas teste",
        "preco": 50.0,
        "quantidade": 10.3
    }
    response = client.post("/produtos", json=new_product, headers=auth)
    assert response.status_code == 422

def test_update(): 
    updated_product = {
        "nome": "Teste produto atualizado",
        "descricao" : "Teste atualizado",
        "preco": 60.0,
        "quantidade": 20
    }
    response = client.put(f"/produtos/{id}", json=updated_product, headers=auth)
    assert response.status_code == 200

def test_delete():
    response = client.delete(f"/produtos/{id}", headers=auth)
    assert response.status_code == 204

def test_delete_product_not_found():
    id = "0"
    response = client.delete(f"/produtos/{id}", headers=auth)
    assert response.status_code == 404
