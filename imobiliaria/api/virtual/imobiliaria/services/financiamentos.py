from configs.db import db
from entities.financiamentos import Financiamentos

class ServiceFinanciamentos():
    def save(request):
        financiamentos = Financiamentos(request.json['banco'], request.json['quantidade_parcela'], request.json['porcetagem_entrada'])
        db.session.add(financiamentos)
        db.session.commit()