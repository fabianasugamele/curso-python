from configs.db import db

class GastosImovel(db.Model):
    __tablename__ = 'gastos_imoveis'
    id = db.Column('id', db.Integer, primary_key = True)
    conta_luz = db.Column(db.Numeric(11))
    conta_agua = db.Column(db.Numeric(9))
    condominio = db.Column(db.Numeric())
    propaganda_venda = db.Column(db.Numeric(12))


    def __init__(self, conta_luz, conta_agua, condominio, propaganda_venda):
        self.conta_luz = conta_luz
        self.conta_agua = conta_agua
        self.condominio = condominio
        self.propaganda_venda = propaganda_venda