from flask import Flask, request, jsonify
import futebol_service as service


app = Flask(__name__)


#p1 = {"mandante": "Palmeiras", "visitante": "Santos", 
#        "gols_visitante": 1, "gols_mandante": 3}

@app.route("/partidas", methods={"POST"})
def cadastra_partida():
    try:
        partida = request.json
        service.cadastra_partida(partida)
        info = {"title": "Partida cadastrada com sucesso!", "status": 201} 
        return info, 201
    except Exception as erro:
        print(erro)
        info = {"title": "Erro cadastrando a partida", "status": 404}
        return info, 404


@app.route("/tabelas", methods={"GET"})
def recupera_tabela():
    try:
        dados = service.recupera_tabela()
        return dados, 200
    except erro as Exception:
        info = {"title": "Erro recuperando a tabela", "status": 404}
        return info, 404


app.run(debug=True)