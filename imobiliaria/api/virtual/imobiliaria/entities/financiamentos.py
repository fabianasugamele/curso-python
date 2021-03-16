from configs.db import db

class Financiamentos(db.Model):
    __tablename__ = 'financiamentos'
    id = db.Column('id', db.Integer, primary_key = True)
    banco = db.Column(db.String(10))
    quantidade_parcelas = db.Column(db.String(10))
    porcetagem_entrada = db.Column(db.Float(100))
   


    def __init__(self, banco, quantidade_parcelas, porcetagem_entrada):
        self.banco = banco
        self.quantidade_parcelas = quantidade_parcelas
        self.porcetagem_entrada = porcetagem_entrada
      