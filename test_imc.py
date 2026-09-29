import pytest
from imc import classificar_imc

def test_imc_abaixo():
    imc_abaixo = classificar_imc(18.0)
    assert imc_abaixo == "Abaixo do peso"

def test_imc_normal():
    imc_normal = classificar_imc(23.0)
    assert imc_normal == "Peso normal"

def test_imc_acima():
    imc_acima = classificar_imc(25.5)
    assert imc_acima == "Acima do peso"

def test_imc_valor_de_fronteira():
    imc_fronteira = classificar_imc(18.5)
    assert imc_fronteira == "Peso normal"