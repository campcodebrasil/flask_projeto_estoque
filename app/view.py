from flask import jsonify, request
from app import app
from app.model import Produto, PessoaJuridica


@app.route('/produto/novo/', methods=['POST'])
def produto_novo():
  try:
    data = request.form
    
    prod = Produto(
      codigo = data['codigo'],
      descricao = data['descricao'],
      custo = data['custo']
    )
    prod.save()  
    resposta = {'msg': 'Sucesso!!!', 'obs': 'Produto Cadastro com Sucesso!!!'}
  except:
    resposta = {'msg': 'ERRO', 'obs': 'Falha ao cadastrar o Produto!!!'}   

  return jsonify(resposta)


@app.route('/produto/buscar/todos/')
def produto_buscar():
  obj = Produto.query.all()
  data = [{'id': o.id, 'codigo': o.codigo, 'descricao': o.descricao, 'custo': o.custo} for o in obj]
  resposta = {'msg': 'Sucesso', 'data': data}
  return jsonify(resposta)


@app.route('/pj/novo/', methods=['POST'])
def pj_novo():
  try:
    data = request.form
    
    pj = PessoaJuridica(
      cnpj = data['cnpj'],
      nome = data['nome'],
      tipo = data['tipo']
    )
    pj.save()  
    resposta = {'msg': 'Sucesso!!!', 'obs': 'Pessoa Jurídica Cadastra com Sucesso!!!'}
  except Exception as e:
    resposta = {'msg': 'ERRO', 'obs': e.args[0]}   

  return jsonify(resposta)


@app.route('/pj/buscar/todos/')
def pj_buscar():
  obj = PessoaJuridica.query.all()
  data = [{'id': o.id, 'cnpj': o.cnpj, 'nome': o.nome, 'tipo': o.tipo} for o in obj]
  resposta = {'msg': 'Sucesso', 'data': data}
  return jsonify(resposta)

