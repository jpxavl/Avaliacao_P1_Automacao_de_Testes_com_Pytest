import pytest
from frete import calcular_frete

def test_frete_10():
    frete_10 = calcular_frete(3)
    assert frete_10 == 10.0

def test_frete_20():
    frete_20 = calcular_frete(8)
    assert frete_20 == 20.0

def test_frete_35():
    frete_35 = calcular_frete(11)
    assert frete_35 == 35.0

def test_frete_10_fronteira():
    frete_10_fronteira = calcular_frete(5)
    assert frete_10_fronteira == 10.00

def test_frete_20_fronteira():
    frete_20_fronteira = calcular_frete(10)
    assert frete_20_fronteira == 20.0