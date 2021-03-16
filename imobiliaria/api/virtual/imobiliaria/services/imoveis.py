from configs.db import db
from entities.imoveis import Imoveis

class ServiceImoveis():
    def save(request):
        imoveis = Imoveis(request.json['id_tipo'], request.json['id_endereco'], request.json['id_proprietario'], request.json['id_gastos'])
        db.session.add(imoveis)
        db.session.commit()