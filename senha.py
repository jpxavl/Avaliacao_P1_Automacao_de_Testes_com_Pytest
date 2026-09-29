def senha_valida(senha):
    if len(senha) < 8:
        return False
    return any(c.isdigit() for c in senha)