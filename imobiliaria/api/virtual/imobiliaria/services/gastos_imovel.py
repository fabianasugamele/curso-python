from configs.db import db
from entities.gastos_imovel import GastosImovel

class ServiceGastosImovel():
    def save(request):
        gastos_imovel = GastosImovel(request.json['conta_luz'], request.json['conta_agua'], request.json['condominio'], request.json['propaganda_venda'])
        db.session.add(gastos_imovel)
        db.session.commit()