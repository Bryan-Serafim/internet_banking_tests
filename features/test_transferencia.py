import json
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from app import app

scenarios("transferencia.feature")


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def contexto():
    return {"resposta": None}


@given(parsers.parse("que a conta {conta:d} possui saldo de {saldo:f}"))
def saldo_inicial(client, conta, saldo):
    resp = client.get(f"/saldo/{conta}")
    assert resp.status_code == 200


@when(parsers.parse("a conta {origem:d} transfere {valor:f} para a conta {destino:d}"))
def executa_transferencia(client, contexto, origem, valor, destino):
    contexto["resposta"] = client.post(
        "/transferencia",
        data=json.dumps({"origem": origem, "destino": destino, "valor": valor}),
        content_type="application/json",
    )


@when(parsers.parse("a conta {origem:d} tenta transferir {valor:f} para a conta {destino:d}"))
def tenta_transferencia(client, contexto, origem, valor, destino):
    contexto["resposta"] = client.post(
        "/transferencia",
        data=json.dumps({"origem": origem, "destino": destino, "valor": valor}),
        content_type="application/json",
    )


@then("a transferência deve ser aceita")
def transferencia_aceita(contexto):
    assert contexto["resposta"].status_code == 200


@then("a transferência deve ser recusada por valor inválido")
def transferencia_recusada(contexto):
    assert contexto["resposta"].status_code == 422


@then(parsers.parse("o saldo da conta {conta:d} deve ficar em {saldo:f}"))
def verifica_saldo_ficar(client, conta, saldo):
    resp = client.get(f"/saldo/{conta}")
    assert resp.get_json()["saldo"] == saldo


@then(parsers.parse("o saldo da conta {conta:d} deve permanecer em {saldo:f}"))
def verifica_saldo_permanecer(client, conta, saldo):
    resp = client.get(f"/saldo/{conta}")
    assert resp.get_json()["saldo"] == saldo