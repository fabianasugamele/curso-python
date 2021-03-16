from configs.db import db

class DocumentosProprietario(db.Model):
    __tablename__ = 'documentos_proprietario'
    id = db.Column('id', db.Integer, primary_key = True)
    cpf = db.Column(db.String(11))
    rg = db.Column(db.String(9))
    titulo = db.Column(db.String(12))

    def __init__(self, cpf, rg, titulo_eleitoral):
        self.cpf = cpf
        self.rg = rg
        self.titulo = titulo_eleitoral