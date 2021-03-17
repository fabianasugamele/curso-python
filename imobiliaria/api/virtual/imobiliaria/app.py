from configs.flask import flask_app
from flask_restplus import Api
app = Api(app = flask_app)

import controllers.cadastro
import controllers.venda