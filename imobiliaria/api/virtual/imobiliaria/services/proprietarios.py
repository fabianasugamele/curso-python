from configs.db import db
from entities.proprietarios import Proprietarios


class ServiceProprietarios():
    @staticmethod
    def save(request):
        proprietarios = Proprietarios()
        proprietarios.set_nome(request.json['nome'])
        proprietarios.set_data_nascimento(request.json['data_nascimento'])
        proprietarios.set_id_documentos_proprietario(request.json['id_documentos_proprietario'])
        proprietarios.set_estado_civil(request.json['estado_civil'])
        proprietarios.set_data_compra(request.json['data_compra'])
        proprietarios.set_profissao(request.json['profissao'])


    
        db.session.add(proprietarios)
        db.session.commit()

    def find_all():
        return Proprietarios.query.all()

    @staticmethod
    def delete(request):
        obj = Proprietarios.query.filter_by(id=request.json['id']).one()
        db.session.delete(obj)
        db.session.commit()