from app import db
from datetime import datetime

class BaseModel():
  id = db.Column(db.Integer, primary_key=True)

  def save(self):
    db.session.add(self)
    db.session.commit()


class Produto(BaseModel, db.Model):
  codigo = db.Column(db.Integer, unique=True, nullable=False)
  descricao = db.Column(db.String(200), nullable=False)
  custo = db.Column(db.Numeric(12, 2), nullable=False)
  qtde = db.Column(db.Integer, default=0)
  solicitacao_produto = db.relationship('SolicitacaoProduto', backref='produto', lazy=True)
  nf_produto = db.relationship('NotaFiscalProduto', backref='produto', lazy=True)
  movimentacao = db.relationship('Movimentacao', backref='produto', lazy=True)


class PessoaJuridica(BaseModel, db.Model):
  cnpj = db.Column(db.Integer, unique=True, nullable=False)
  nome = db.Column(db.String(200), nullable=False)
  tipo = db.Column(db.Integer, nullable=False)
  emitente_nf = db.relationship('NotaFiscal', backref='emitente', lazy=True)
  remetente_nf = db.relationship('NotaFiscal', backref='remetente', lazy=True)

  def save(self):
    self.tipo = int(self.tipo)
    if self.tipo not in (1, 2, 3): raise Exception('Tipo inválido!!!')
    super().save()


class Solicitacao(BaseModel, db.Model):
  data = db.Column(db.Date, default=datetime.utcnow)
  status = db.Column(db.Integer, default=1)
  natureza = db.Column(db.String(1), nullable=False) # E/S => Entrada/Saída
  solicitacao_produto = db.relationship('SolicitacaoProduto', backref='solicitacao', lazy=True)
  nota_fiscal = db.relationship('NotaFiscal', backref='solicitacao', lazy=True)

  def save(self):
    if self.natureza not in ('E', 'S'): raise Exception('Tipo inválido!!!')
    super().save()

  def iniciar_nf(self): pass

  def emitir_nf(self): pass


class SolicitacaoProduto(BaseModel, db.Model):
  solicitacao_id = db.Column(db.Integer, db.ForeignKey('solicitacao.id'))
  produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))  
  qtde_solicitada = db.Column(db.Integer, default=0)
  qtde_atendida = db.Column(db.Integer, default=0)


class NotaFiscal(BaseModel, db.Model):
  data = db.Column(db.Date, default=datetime.utcnow)
  emitente_id = db.Column(db.Integer, db.ForeignKey('pessoa_juridica.id'))
  remetente_id = db.Column(db.Integer, db.ForeignKey('pessoa_juridica.id'))
  solicitacao_id = db.Column(db.Integer, db.ForeignKey('solicitacao.id'))
  status = db.Column(db.Integer, default=1)
  natureza = db.Column(db.String(1), nullable=False) # E/S => Entrada/Saída
  nf_produto = db.relationship('NotaFiscalProduto', backref='nota_fiscal', lazy=True)
  movimentacao = db.relationship('Movimentacao', backref='nota_fiscal', lazy=True)

  def save(self):
    if self.natureza not in ('E', 'S'): raise Exception('Tipo inválido!!!')
    super().save()
  
  def emitir_nf(self): pass

  def finalizar_nf(self): pass

  def recusar_nf(self): pass

  def cancelar_nf(self): pass


class NotaFiscalProduto(BaseModel, db.Model):
  nf_id = db.Column(db.Integer, db.ForeignKey('nota_fiscal.id'))
  produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))  
  qtde_solicitada = db.Column(db.Integer, default=0)
  qtde_atendida = db.Column(db.Integer, default=0)


class Movimentacao(BaseModel, db.Model):
  data = db.Column(db.Date, default=datetime.utcnow)
  nf_id = db.Column(db.Integer, db.ForeignKey('nota_fiscal.id'))
  produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
  estoque_inicial = db.Column(db.Integer, nullable=False)
  qtde_movimentacao = db.Column(db.Integer, nullable=False)
  estoque_final = db.Column(db.Integer, nullable=False)
  observacao = db.Column(db.String(500), nullable=True) 
