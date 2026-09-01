def adiciona_produto(produto: str, qtd: int, estoque: dict):
    if produto in estoque:
        estoque[produto] = estoque[produto] + qtd
    else:
        estoque[produto] = qtd

def venda_produto(produto: str, qtd: int, estoque: dict):
    if not produto in estoque:
        print(f"Produto {produto} não encontrado!")
    else:
        quantidade = estoque[produto]
        if quantidade >= qtd:
            estoque[produto] = estoque[produto] - qtd
            print(f"{qtd} peças de {produto} foram vendidas")
        else:
            print(f"{qtd} insuficiente do {produto} no estoque")

loja = {
    "lapiseira": 100,
    "borracha": 50,
    "caderno": 25,
    "caneta": 200
}

venda_produto("compasso", 10, loja)
adiciona_produto("compasso", 35, loja)
venda_produto("compasso", 10, loja)
