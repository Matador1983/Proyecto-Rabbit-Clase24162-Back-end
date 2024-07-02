from flask import Flask, request, jsonify
from app.database import init_app
from app.views import *
from flask_cors import CORS

#Crear una instancia de Flask
app = Flask(__name__)

init_app(app)

CORS(app)

#asociacion de rutas con vistas
app.route('/',methods=['GET'])(index)
app.route('/api/user/',methods=['GET'])(get_all_user) #Consultar usuario 
app.route('/api/user/',methods=['POST'])(create_user) #Crear usuario
app.route('/api/user/<int:iduser>/<string:idpass>', methods=['GET'])(get_user) #Consultar usuario
app.route('/api/user/<int:iduser>', methods=['GET'])(get_user2) #Consultar usuario
app.route('/api/user/<int:iduser>', methods=['PUT'])(update_user) #Modificar usuario
app.route('/api/user/<int:iduser>', methods=['DELETE'])(delete_user)

#Permite separa el codigo que se ejecuta cuando se corre el archivo
if __name__=='__main__':
    app.run(debug=True)