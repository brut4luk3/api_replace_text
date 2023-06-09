from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route('/api/replace_text', methods=['POST'])

def replace_text():
    dados = request.get_json()
    texto = dados['texto']
    item_para_substituir = dados['item_para_substituir']
    item_substituto = dados['item_substituto']
    parcial = dados['CasoParcialQuantidade']
    modo = dados['modo']

    if modo == 'completo':
        novo_texto = texto.replace(item_para_substituir, item_substituto)

        response = {
            'result': novo_texto
        }
        return jsonify(response), 200

    elif modo == 'parcial':
        novo_texto = texto.replace(item_para_substituir, item_substituto, parcial)

        response = {
            'result': novo_texto
        }
        return jsonify(response), 200

    else:
        response = {
            'Erro': 'Modo de operação inválido! Modos aceitos: completo ou parcial (caso parcial, insira a quantidade em CasoParcialQuantidade.'
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run()