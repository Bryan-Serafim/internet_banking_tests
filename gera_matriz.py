import xml.etree.ElementTree as ET
import os

casos = {
    "test_transferencia_saldo_suficiente": ("TC-001", "transferencia com saldo suficiente", "REQ-01"),
    "test_saldo_conta_existente": ("TC-002", "consulta de saldo conta existente", "REQ-02"),
    "test_transferencia_saldo_igual_valor": ("TC-003", "transferencia com saldo exatamente igual ao valor", "REQ-01"),
    "test_recusar_transferencia_de_valor_zero": ("TC-004", "recusar transferencia de valor zero", "REQ-03"),
}

linhas = ["# Matriz de Rastreabilidade\n",
          "| ID | Caso de Teste | Requisito | Status |",
          "|---|---|---|---|"]

try:
    tree = ET.parse("report.xml")
    resultados = {}
    for tc in tree.getroot().iter("testcase"):
        nome = tc.get("name", "")
        falhou = tc.find("failure") is not None
        resultados[nome] = "FAILED" if falhou else "PASSED"
except Exception:
    resultados = {}

for nome, (id_, desc, req) in casos.items():
    status = resultados.get(nome, "NAO EXECUTADO")
    linhas.append(f"| {id_} | {desc} | {req} | {status} |")

print("\n".join(linhas))
