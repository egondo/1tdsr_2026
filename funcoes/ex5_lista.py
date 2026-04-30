palavra = input("Palavra: ")
frase = input("Frase: ")

contador = 0
pos = frase.find(palavra, 0)
while pos != -1:
    contador = contador + 1
    pos = frase.find(palavra, pos + 1)

print(f"A {palavra} aparece {contador} vezes em '{frase}'")