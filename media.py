def calcular_media(notas):
    if not notas:
        raise ValueError("Lista de notas vazia")
    return sum(notas) / len(notas)