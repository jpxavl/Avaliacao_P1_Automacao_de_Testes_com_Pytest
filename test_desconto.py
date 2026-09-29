import pytest
from desconto import aplicar_desconto

def test_desconto_valido():
    desconto_valido = aplicar_desconto(100, 20)
    assert desconto_valido == 80

def test_desconto_0():
    desconto_0 = aplicar_desconto(100, 0)
    assert desconto_0 == 100

def test_desconto_100():
    desconto_100 = aplicar_desconto(100, 100)
    assert desconto_100 == 0

def test_desconto_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)
    assert "Desconto inválido"