from services.financiamentos import ServiceFinanciamentos

from flask import request, jsonify
from app import app
from flask_restplus import Resource, fields
from flask_api import status

name_space = app.namespace('venda', description='APIs para vendas')

modelFinanciamento = app.model('Financiamento do imóvel', 
				  {'banco': fields.String(required = True, 
    					  				 description="Banco do cliente", 
    					  				 help="O banco não pode estar vazio"),
                    'quantidade_parcelas':   fields.String(required = True, 
    					  				 description="Quantidade de parcelas do financiamento", 
    					  				 help="A quantidade não pode estar vazio"),
                    'porcetagem_entrada': fields.String(required = False, 
    					  				 description="porcentagem da entrada", 
    					  				 help="A porcentagem não pode estar vazio")})

@name_space.route("/financiamento/")
class FinanciamentoClass(Resource):

    @app.doc(responses={ 200: 'OK', 404: 'Not Found', 500: 'Mapping Key Error' })
    def get(self):
        financiamentos = ServiceFinanciamentos.find_all()
        financiamentosArray = []
        for financiamento in financiamentos:
            financiamentosArray.append(financiamento.toDict())

        return jsonify(financiamentosArray)
    
    @app.doc(responses={ 201: 'Created', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    @app.expect(modelFinanciamento)   
    def post(self):
        ServiceFinanciamentos().save(request)
        return {"status":"Created"}, status.HTTP_201_CREATED
    
    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 404:'Not Found', 500: 'Mapping Key Error' })
    # @app.expect(model_deleted)
    def delete(self):
        ServiceFinanciamentos().delete(request)
        return {"status":"Deleted"}, status.HTTP_200_OK