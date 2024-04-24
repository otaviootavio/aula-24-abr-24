from flask_cors import CORS
from flask import Flask, jsonify
import random

app = Flask(__name__)
CORS(app)

# Lista de piadas
piadas = [
    "Por que o jacaré tirou o alligator? Porque ele não tinha nenhuma par de roupa!",
    "Qual o cúmulo da rapidez? O pneu furar e o cara sair correndo!",
    "Por que a galinha atravessou a rua? Para provar que ela não era frango de granja!",
    "Por que o peixe foi preso? Porque passou no sinal vermelho!",
    "Qual é o animal que mais gosta de estar na moda? O galo, porque só ele sabe dar pinta!",
    "Por que o livro de matemática cometeu suicídio? Porque tinha muitos problemas.",
    "O que a impressora disse para o papel? Esse é meu trabalho, mas sua vida está impressa em preto e branco."
]

@app.route('/piada', methods=['GET'])
def obter_piada():
    # Retorna uma piada aleatória
    return jsonify({'piada': random.choice(piadas)})

if __name__ == '__main__':
    app.run(debug=True)
