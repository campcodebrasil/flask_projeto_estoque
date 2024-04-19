from app import db


class Produto(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  codigo = db.Column(db.Integer, unique=True, nullable=False)
  descricao = db.Column(db.String(200), nullable=False)
  custo = db.Column(db.Numeric(12, 2), nullable=False)

  def save(self):
    db.session.add(self)
    db.session.commit()

