import json

jogos = [
    {
        "titulo": "Minecraft",
        "plataforma": ["PC", "XBox", "PS"],
        "genero": "Aventura",
        "desenvolvedor": "Mojang"
    },
    {
        "titulo": "The Last of Us",
        "plataforma": ["PC", "PS"],
        "genero": "Ação",
        "desenvolvedor": "Naughty Dog"
    }
]

with open("biblioteca_jogos.json", mode="w") as arq:
    json.dump(jogos, arq, indent=4)

print("Arquivo gravado")