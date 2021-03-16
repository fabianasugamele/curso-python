from configs.db import db

class Vendas(db.Model):
    __tablename__ = 'vendas'
    id = db.Column('id', db.Integer, primary_key = True)
    valor_imovel = db.Column(db.Integer())
    id_cliente = db.Column(db.Integer())
    id_financiamento = db.Column(db.Integer())
    id_imovel = db.Column(db.Integer())

    def __init__(self, valor_imovel, id_cliente, id_financiamento, id_imovel):
        self.valor_imovel = valor_imovel
        self.id_cliente = id_cliente
        self.id_financiamento = id_financiamento
        self.id_imovel = id_imovel