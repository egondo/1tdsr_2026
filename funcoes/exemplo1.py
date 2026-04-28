def aumento_ruim(valor, percentual):
    novo_valor = (1 + percentual/100) * valor
    print(novo_valor)

def aumento(valor: float, percentual: float) -> float:
    novo_valor = (1 + percentual/100) * valor
    return novo_valor


novo_preco = aumento(350, 15) #aplicando 15% de aumento sobre 350
print(novo_preco) #colocar em campo texto da minha interface gráfica (janela ou formulario html)