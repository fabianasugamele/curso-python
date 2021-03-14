from services.tipo import ServiceTipo
from flask import request
from app import app
from flask_restplus import Resource, fields
from flask_api import status


name_space = app.namespace('principal', description='Minhas APIs')
model = app.model('Tipo do Imovel', 
				  {'tipo': fields.String(required = True, 
    					  				 description="Tipo do imóvel", 
    					  				 help="O tipo não pode estar vazio")})

@name_space.route("/")
class MainClass(Resource):
    def get(self):
        return {
            "status": "Got new data"
        }
    
    @app.doc(responses={ 201: 'Created', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    @app.expect(model)   
    def post(self):
        ServiceTipo().save(request)
        return {"status":"Created"}, status.HTTP_201_CREATED
    
    def delete(self):
        return {
            "status": "Deleted new data"
        }
