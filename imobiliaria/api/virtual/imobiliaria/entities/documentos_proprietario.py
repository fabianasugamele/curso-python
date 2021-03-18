from configs.db import db
from sqlalchemy import inspect

class DocumentosProprietario(db.Model):
    __tablename__ = 'documentos_proprietario'
    id = db.Column('id', db.Integer, primary_key = True)
    cpf = db.Column(db.String(11))
    rg = db.Column(db.String(9))
    titulo_eleitoral = db.Column(db.String(12))

    def set_cpf(self,cpf):
        self.cpf = cpf

    def set_rg(self,rg):
        self.rg = rg

    def set_titulo(self,titulo):
        self.titulo_eleitoral = titulo 
            

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }    