from configs.db import db
from entities.proprietarios import Proprietarios

class ServiceProprietarios():
    def save(request):
        proprietarios = Proprietarios(request.json['nome'], request.json['data_nascimento'], request.json['id_documentos_proprietario'], request.json['estado_civil'], request.json['data_compra'], request.json['profissao'])
        db.session.add(proprietarios)
        db.session.commit()