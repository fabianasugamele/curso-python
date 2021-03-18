from configs.db import db
from entities.financiamentos import Financiamentos

class ServiceFinanciamentos():
    @staticmethod
    def save(request):
        financiamentos = Financiamentos()
        financiamentos.set_banco(request.json['banco'])
        financiamentos.set_quantidade_parcelas(request.json['quantidade_parcelas'])
        financiamentos.set_porcetagem_entrada(request.json['porcetagem_entrada'])
    
        db.session.add(financiamentos)
        db.session.commit()

    def find_all():
        return Financiamentos.query.all()

    @staticmethod
    def delete(request):
        obj = Financiamentos.query.filter_by(id=request.json['id']).one()
        db.session.delete(obj)
        db.session.commit()