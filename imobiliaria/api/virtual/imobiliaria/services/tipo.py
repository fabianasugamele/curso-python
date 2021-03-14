from configs.db import db
from entities.tipo import Tipo

class ServiceTipo():
    def save(request):
        tipo = Tipo(request.json['tipo'])
        db.session.add(tipo)
        db.session.commit()