from configs.db import db
from entities.endereco_imovel import EnderecoImovel

class ServiceEnderecoImovel():
    
    @staticmethod
    def save(request):
        endereco_imovel = EnderecoImovel()
        endereco_imovel.set_logradouro(request.json['logradouro'])
        endereco_imovel.set_numero(request.json['numero'])
        endereco_imovel.set_complemento(request.json['complemento'])
        endereco_imovel.set_cep(request.json['cep'])
        endereco_imovel.set_cidade(request.json['cidade'])
        endereco_imovel.set_uf(request.json['uf'])

        db.session.add(endereco_imovel)
        db.session.commit()

    def find_all():
        return EnderecoImovel.query.all()

    @staticmethod
    def delete(request):
        obj = EnderecoImovel.query.filter_by(id=request.json['id']).one()
        db.session.delete(obj)
        db.session.commit()