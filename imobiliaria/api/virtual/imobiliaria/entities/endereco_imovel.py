from configs.db import db

class EnderecoImovel(db.Model):
    __tablename__ = 'endereco_imovel'
    id = db.Column('id', db.Integer, primary_key = True)
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.Integer(100))
    complemento = db.Column(db.String(12))
    cep = db.Column(db.Integer(10))
    cidade = db.Column(db.String(45))
    uf = db.Column(db.String(2))


    def __init__(self, logradouro, numero, complemento, cep, cidade, uf):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf