from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores =[
  {
    "id": 0,
    "nome": "Rafael",
    "habilidades":["Python","Flask"]
  },
  {
    'id': 1,
    'nome':'Galleani',
    'habilidades':['Python','Django']
  }
]

#Return dev by ID, Update and Delete Dev
@app.route('/dev/<int:id>', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
  if request.method == 'GET':
    try:
      response = desenvolvedores[id]
    except IndexError:
      message = f'Desenvolvedor de ID {id} não existe'
      response= {'status': 'error','message':message}
    except Exception:
      mensagem = 'Erro desconhecido. Procure o administrador da API'
      response= {'status': 404,'message':message}
    return jsonify(response)
 
  elif request.method == 'PUT':
    dados = json.loads(request.data)
    desenvolvedores[id] = dados
    return jsonify(dados)
 
  elif request.method == 'DELETE':
    desenvolvedores.pop(id)
    return jsonify({'status':'sucesso','mensagem':'Registro excluido'})


# Read the list of Dev and return all Dev
@app.route('/dev/',methods=['POST','GET'])
def devList():
  if request.nethod == 'POST':
    dados = json.loads(request.data)
    posicao = len(desenvolvedores)
    dados['id'] = posicao
    desenvolvedores.append(dados)
    return jsonify(desenvolvedores[posicao])
  elif request.method == 'GET':
    return jsonify(desenvolvedores)

if __name__ == '__main__':
  app.run(debug=True)