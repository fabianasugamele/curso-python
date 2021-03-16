from configs.db import db
from vendas import Vendas

class ServiceProprietarios():
    def save(request):
        vendas = Vendas(request.json['valor_imovel'], request.json['id_cliente'], request.json['id_financiamentos'], request.json['id_imovel'])
        db.session.add(vendas)
        db.session.commit()