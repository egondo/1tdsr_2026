from flask import Flask, request, jsonify
import enquete

app = Flask(__name__)

@app.route("/api/v1/hello", methods=["GET"])
def hello():
    return "Ola Mundo!"

@app.route("/api/v1/perguntas", methods=["GET"])
def get_perguntas():
    return enquete.perguntas, 200


@app.route("/api/v1/perguntas/tipo/<tipo>", methods=["GET"])
def get_perguntas_tipo(tipo):
    lista = []
    for perg in enquete.perguntas:
        if perg['tipo'] == tipo:
            lista.append(perg)
    return lista, 200

@app.route("/api/v1/perguntas", methods=['POST'])
def insere_pergunta():
    perg = request.json
    enquete.perguntas.append(perg)
    return perg, 200




app.run(debug=True)