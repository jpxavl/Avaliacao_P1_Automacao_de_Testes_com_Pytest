import pytest
from saque import sacar

def test_saque_valido():
    saque_valido = sacar(140, 40)
    assert saque_valido == 140 - 40

def test_saque_invalido():
    with pytest.raises(ValueError):
        sacar(100, 150)
    assert "Saldo insuficiente"