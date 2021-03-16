from configs.db import db
from entities.endereco_imovel import EnderecoImovel

class ServiceEnderecoImovel():
    def save(request):
        endereco_imovel = EnderecoImovel(request.json['logradouro'], request.json['numero'], request.json['complemento'], request.json['cep'], request.json['cidade'], request.json['uf'])
        db.session.add(endereco_imovel)
        db.session.commit()

