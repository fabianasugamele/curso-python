from configs.db import db
from sqlalchemy import inspect

class EnderecoImovel(db.Model):
    __tablename__ = 'enderecos_imovel'
    id = db.Column('id', db.Integer, primary_key = True)
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.Integer())
    complemento = db.Column(db.String(12))
    cep = db.Column(db.Integer())
    cidade = db.Column(db.String(45))
    uf = db.Column(db.String(2))

    def set_logradouro(self,logradouro):
        self.logradouro = logradouro

    def set_numero(self,numero):
        self.numero = numero

    def set_complemento(self,complemento):
        self.complemento = complemento 

    def set_cep(self,cep):
        self.cep = cep

    def set_cidade(self,cidade):
        self.cidade = cidade

    def set_uf(self,uf):
        self.uf = uf                      

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }    