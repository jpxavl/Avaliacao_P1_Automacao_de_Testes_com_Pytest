import pytest
from senha import senha_valida

def test_senha_permitida():
    senha_permitida = senha_valida("cba54321")
    assert senha_permitida is True

def test_senha_curta():
    senha_curta = senha_valida("ab1234")
    assert senha_curta is False

def test_senha_sem_numero():
    senha_sem_numero = senha_valida("abcdefgh")
    assert senha_sem_numero is False

def test_senha_8():
    senha_8 = senha_valida("12345678")
    assert senha_8 is True