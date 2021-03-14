
from configs.db import db

class Tipo(db.Model):
    __tablename__ = 'tipos_imovel'
    id = db.Column('id', db.Integer, primary_key = True)
    tipo = db.Column(db.String(45))

    def __init__(self, tipo):
        self.tipo = tipo