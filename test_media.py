import pytest
from media import calcular_media

def test_media_notas_diferentes():
    media_notas_diferentes = calcular_media([4, 6, 8])
    assert media_notas_diferentes == 6

def test_media_notas_iguais():
    media_notas_diferentes = calcular_media([9, 9, 9])
    assert media_notas_diferentes == 9

def test_media_nota_unica():
    media_nota_unica = calcular_media([9])
    assert media_nota_unica == 9

def test_media_nota_vazia():
    with pytest.raises(ValueError):
        calcular_media([])
    assert "Lista de notas vazias"