from configs.db import db
from sqlalchemy import inspect

class Proprietarios(db.Model):
    __tablename__ = 'proprietarios'
    id = db.Column('id', db.Integer, primary_key = True)
    nome = db.Column(db.String(11))
    data_nascimento = db.Column(db.Date())
    id_documentos_proprietario = db.Column(db.String())
    estado_civil = db.Column(db.String())
    data_compra = db.Column(db.Date())
    profissao = db.Column(db.String())


    def set_nome(self,nome):
        self.nome = nome

    def set_data_nascimento(self,data_nascimento):
        self.data_nascimento = data_nascimento

    def set_id_documentos_proprietario (self,id_documentos_proprietario ):
        self.id_documentos_proprietario  = id_documentos_proprietario  
    
    def set_estado_civil (self,estado_civil ):
        self.estado_civil  = estado_civil
    
    def set_data_compra (self,data_compra ):
        self.data_compra  = data_compra 
    
    def set_profissao (self,profissao ):
        self.profissao  = profissao 
            

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }   