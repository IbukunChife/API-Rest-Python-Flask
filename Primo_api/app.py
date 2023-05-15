from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>', methods=['GET','POST'])
def home():
  return jsonify({'id':id, 'nome':'Olá', 'profissao':'dev'})

@app.route('/soma1/<int:valor1>/<int:valor2>')
def soma1(valor1,valor2):
  return jsonify({'soma': valor1 + valor2})

@app.route('/soma2', methods=['POST','GET','PUT'])
def soma2():
  if request.method == 'POST':
    dados = json.load(request.data)
    total = sum(dados['valores'])
  elif request.method == 'GET':
    total = 10+10
  return jsonify({"soma": total})


if __name__ == '__main__':
  app.run(debug=True)