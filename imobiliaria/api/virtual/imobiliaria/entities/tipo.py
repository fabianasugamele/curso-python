
from configs.db import db
from sqlalchemy import inspect


class Tipo(db.Model):
    __tablename__ = 'tipos_imovel'
    id = db.Column('id', db.Integer, primary_key = True)
    tipo = db.Column(db.String(45))

    def set_tipo(self,tipo):
        self.tipo = tipo

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }       