def aplicar_desconto(valor, desconto):
    if desconto < 0 or desconto > 100:
        raise ValueError("Desconto inválido")
    return valor - (valor * desconto / 100)