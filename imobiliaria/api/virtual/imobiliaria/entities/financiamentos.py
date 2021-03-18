from configs.db import db
from sqlalchemy import inspect

class Financiamentos(db.Model):
    __tablename__ = 'financiamentos'
    id = db.Column('id', db.Integer, primary_key = True)
    banco = db.Column(db.String(10))
    quantidade_parcelas = db.Column(db.String(10))
    porcetagem_entrada = db.Column(db.Float(100))
   

    def banco(self,banco):
        self.banco = banco

    def quantidade_parcelas(self,quantidade_parcelas):
        self.quantidade_parcelas = quantidade_parcelas

    def porcetagem_entrada(self,porcetagem_entrada):
        self.porcetagem_entrada = porcetagem_entrada 
            

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }  