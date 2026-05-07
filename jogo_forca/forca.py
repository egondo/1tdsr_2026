#crie as funcoes logo no começo do seu projeto
import random

def secret_word(secret: str, chutes: str) -> str:
    resp = ''
    for c in secret:
        if c.lower() in chutes:
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

def sorteia_palavra() -> str:
    #representar um conjunto ou uma sequencia de estados norte americanos, sortear um desses estados para a palavra do jogo da Forca
    estados = ["North Dakota", "South Dakota", "New York", "California", "Florida", "Texas", "Massashusets", "Illinois", "Montana", "Nevada", "Utah", "Rhode Island", "Georgia", "Alaska", "Ohio", "Hawai", "Minessota", "Arizona", "Michigan", "Colorado", "Lousiana", "South Caroline", "North Caroline", "Washington", "Idaho", "Alabana", "Arkansas", "Connecticut", "Virginia"]

    pos = random.randint(0, len(estados))

    return estados[pos]

#para separar as funcoes do programa principal, fazemos o seguinte:
if __name__ == "__main__":
    palavra = sorteia_palavra()
    letras_chutadas = ' '
    erros = 0
    segredo = secret_word(palavra, letras_chutadas)
    while not enforcado(erros) and not acertou(segredo):
        print(segredo)
        print(f"erros: {erros}")
        letra = input('Letra: ').lower()
        letras_chutadas = letras_chutadas + letra
        segredo = secret_word(palavra, letras_chutadas)

        if not letra in palavra:
            erros = erros + 1
        
    if acertou(segredo):
        print(f"Parabéns, vc acertou {palavra}")
    else:
        print(f"Você foi enforcado a palavra é {palavra}")
