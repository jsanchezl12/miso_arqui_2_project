from MServicio import create_app
from markupsafe import escape
from flask_restful import Api
from .vistas import VistaValidarPassword

app = create_app('default')
app_context = app.app_context()
app_context.push()


api = Api(app)

api.add_resource(VistaValidarPassword, '/validarPass')
