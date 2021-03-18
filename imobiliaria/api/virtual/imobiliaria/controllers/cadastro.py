from services.tipo import ServiceTipo
from services.endereco_imovel import ServiceEnderecoImovel
from services.documentos_proprietarios import ServiceDocumentosProprietario
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



modelEndereco = app.model('Endereço do Imovel', 
				  {'logradouro': fields.String(required = True, 
    					  				 description="logradouro do imóvel", 
    					  				 help="O logradouro não pode estar vazio"),
                    'numero':   fields.String(required = True, 
    					  				 description="numero do imóvel", 
    					  				 help="O numero não pode estar vazio"),
                    'complemento': fields.String(required = False, 
    					  				 description="complemento do imóvel", 
    					  				 help="O complemento não pode estar vazio"),
                    'cep':   fields.String(required = True, 
    					  				 description="cep do imóvel", 
    					  				 help="O cep não pode estar vazio"),
                    'cidade':   fields.String(required = True, 
    					  				 description="cidade do imóvel", 
    					  				 help="A cidade não pode estar vazio"),
                    'uf':   fields.String(required = True, 
    					  				 description="uf do imóvel", 
    					  				 help="O uf não pode estar vazio")})

modelDocumento = app.model('Documentos do Proprietário', 
				  {'cpf': fields.String(required = True, 
    					  				 description="CPF do proprietário", 
    					  				 help="O CPF não pode estar vazio"),
                    'rg':   fields.String(required = True, 
    					  				 description="RG do proprietário", 
    					  				 help="O RG não pode estar vazio"),
                    'titulo_eleitoral': fields.String(required = False, 
    					  				 description="titulo do proprietário", 
    					  				 help="O titulo não pode estar vazio")})

@name_space.route("/endereco/")
class EnderecoClass(Resource):

    @app.doc(responses={ 200: 'OK', 404: 'Not Found', 500: 'Mapping Key Error' })
    def get(self):
        enderecos = ServiceEnderecoImovel.find_all()
        enderecoArray = []
        for endereco in enderecos:
            enderecoArray.append(endereco.toDict())

        return jsonify(enderecoArray)
    
    @app.doc(responses={ 201: 'Created', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    @app.expect(modelEndereco)   
    def post(self):
        ServiceEnderecoImovel().save(request)
        return {"status":"Created"}, status.HTTP_201_CREATED
    
    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 404:'Not Found', 500: 'Mapping Key Error' })
    # @app.expect(model_deleted)
    def delete(self):
        ServiceEnderecoImovel().delete(request)
        return {"status":"Deleted"}, status.HTTP_200_OK        

@name_space.route("/proprietarios/documentos/")
class DocumentoClass(Resource):

    @app.doc(responses={ 200: 'OK', 404: 'Not Found', 500: 'Mapping Key Error' })
    def get(self):
        documentos_proprietario = ServiceDocumentosProprietario.find_all()
        documentosArray = []
        for documentos in documentos_proprietario:
            documentosArray.append(documentos.toDict())

        return jsonify(documentosArray)
    
    @app.doc(responses={ 201: 'Created', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    @app.expect(modelDocumento)   
    def post(self):
        ServiceDocumentosProprietario().save(request)
        return {"status":"Created"}, status.HTTP_201_CREATED
    
    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 404:'Not Found', 500: 'Mapping Key Error' })
    # @app.expect(model_deleted)
    def delete(self):
        ServiceDocumentosProprietario().delete(request)
        return {"status":"Deleted"}, status.HTTP_200_OK        

