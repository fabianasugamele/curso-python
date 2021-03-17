from services.tipo import ServiceTipo
from flask import request, jsonify
from app import app
from flask_restplus import Resource, fields
from flask_api import status


name_space = app.namespace('cadastro', description='APIs para o cadastro')
model = app.model('Tipo do Imovel', 
				  {'tipo': fields.String(required = True, 
    					  				 description="Tipo do imóvel", 
    					  				 help="O tipo não pode estar vazio")})
# model_deleted = app.model('Tipo do Imovel', 
# 				  {'id': fields.Integer(required = True, 
#     					  				 description="Id do tipo do imóvel", 
#     					  				 help="O id do tipo não pode estar vazio")})                                           

@name_space.route("/tipo/")
class TipoClass(Resource):

    @app.doc(responses={ 200: 'OK', 404: 'Not Found', 500: 'Mapping Key Error' })
    def get(self):
        tipos = ServiceTipo.find_all()
        tiposArray = []
        for tipo in tipos:
            tiposArray.append(tipo.toDict())

        return jsonify(tiposArray)
    
    @app.doc(responses={ 201: 'Created', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    @app.expect(model)   
    def post(self):
        ServiceTipo().save(request)
        return {"status":"Created"}, status.HTTP_201_CREATED
    
    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 404:'Not Found', 500: 'Mapping Key Error' })
    # @app.expect(model_deleted)
    def delete(self):
        ServiceTipo().delete(request)
        return {"status":"Deleted"}, status.HTTP_200_OK
