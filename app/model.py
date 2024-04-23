from app import db

class BaseModel():
  id = db.Column(db.Integer, primary_key=True)

  def save(self):
    db.session.add(self)
    db.session.commit()


class Produto(BaseModel, db.Model):
  codigo = db.Column(db.Integer, unique=True, nullable=False)
  descricao = db.Column(db.String(200), nullable=False)
  custo = db.Column(db.Numeric(12, 2), nullable=False)


class PessoaJuridica(BaseModel, db.Model):
  cnpj = db.Column(db.Integer, unique=True, nullable=False)
  nome = db.Column(db.String(200), nullable=False)
  tipo = db.Column(db.Integer, nullable=False)

  def save(self):
    self.tipo = int(self.tipo)
    if self.tipo not in (1, 2, 3): raise Exception('Tipo inválido!!!')
    super().save()

