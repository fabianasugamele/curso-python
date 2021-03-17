from app import app
from flask_restplus import Resource

name_space_secundario = app.namespace('venda', description='APIs para vendas')

@name_space_secundario.route("/")
class VendaClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}
