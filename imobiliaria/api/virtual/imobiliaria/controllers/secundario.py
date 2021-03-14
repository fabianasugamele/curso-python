from app import app
from flask_restplus import Resource

name_space_secundario = app.namespace('secundario', description='Minha API Secundária')

@name_space_secundario.route("/")
class SecondClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}
