#crie as funcoes logo no começo do seu projeto

def secret_word(secret: str, chutes: str) -> str:
    resp = ''
    for c in secret:
        if c in chutes:
            resp = resp + c + ' '
        else:
            resp = resp + '_ '
    return resp

def acertou(palavra) -> bool:
    if '_' in palavra:
        return False
    return True

def enforcado(erros) -> bool:
    if erros >= 6:
        return True
    return False


#para separar as funcoes do programa principal, fazemos o seguinte:
if __name__ == "__main__":
    palavra = "Uganda"
    letras_chutadas = ''
    erros = 0
    segredo = secret_word(palavra, letras_chutadas)
    while not enforcado(erros) and not acertou(segredo):
        print(segredo)
        print(f"erros: {erros}")
        letra = input('Letra: ')
        letras_chutadas = letras_chutadas + letra
        segredo = secret_word(palavra, letras_chutadas)
        #Como eu sei se a letra digitada é um acerto ou um erro?
        #Como resolvo o problema das letras maiúsculas
        #O que fazer com palavras compostas?