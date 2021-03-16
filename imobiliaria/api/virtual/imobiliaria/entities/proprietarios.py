from configs.db import db

class Proprietarios(db.Model):
    __tablename__ = 'proprietarios'
    id = db.Column('id', db.Integer, primary_key = True)
    nome = db.Column(db.String(11))
    data_nascimento = db.Column(db.Date())
    id_documentos_proprietario = db.Column(db.String())
    estado_civil = db.Column(db.String())
    data_compra = db.Column(db.Date())
    profissao = db.Column(db.String())

    def __init__(self, nome, data_nascimento, id_documentos_proprietario, estado_civil, data_compra,profissao ):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.id_documentos_proprietario = id_documentos_proprietario
        self.estado_civil = estado_civil
        self.data_compra = data_compra
        self.profissao = profissao
