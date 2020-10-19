from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [

    {
     'id':'0',
     'nome': 'Filipe',
     'habilidades': ['Python', 'Flask']
     },
    {
     'id':'1',
     'nome': 'Fantini',
     'habilidades':['Python','Django']
    }
]
# Devolve um desenvolvedor pelo ID, também altera e deleta
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response=desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'Status':'Erro','Mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o adm da API'
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

#Lista de todos os desenvolvedores e permite registrar um novo dev
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores ():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)