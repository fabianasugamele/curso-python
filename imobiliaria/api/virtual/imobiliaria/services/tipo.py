from configs.db import db
from entities.tipo import Tipo

class ServiceTipo():

    def find_all():
        return Tipo.query.all()

    @staticmethod
    def save(request):
        tipo = Tipo()
        tipo.set_tipo(request.json['tipo'])
        db.session.add(tipo)
        db.session.commit()

    @staticmethod
    def delete(request):
        obj = Tipo.query.filter_by(id=request.json['id']).one()
        db.session.delete(obj)
        db.session.commit()  