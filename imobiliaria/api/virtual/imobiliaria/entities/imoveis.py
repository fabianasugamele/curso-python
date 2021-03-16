from configs.db import db

class imoveis(db.Model):
    __tablename__ = 'imoveis'
    id = db.Column('id', db.Integer, primary_key = True)
    id_tipo = db.Column(db.Integer(10))
    id_endereco = db.Column(db.Integer(10))
    id_proprietario = db.Column(db.Integer(10))
    id_gastos = db.Column(db.Integer(10))


    def __init__(self, id_tipo, id_endereco, id_proprietario, id_gastos):
        self.id_tipo = id_tipo
        self.id_endereco = id_endereco
        self.id_proprietario = id_proprietario
        self.id_gastos = id_gastos