from flask import jsonify, request, render_template
from app.models import User

def index():
    response = {'message':'Hola mundo API FLASK 🐍'}
    return jsonify(response)

#funcion que busca todo el listado de usuarios
def get_all_user():
    usuarios = User.get_all()
    list_usuarios= [User.serialize() for User in usuarios]
    return jsonify(list_usuarios)

#funcion que busca una pelicula


def get_user(iduser,idpass):
    user= User.get_by_user(iduser,idpass)
    if not user:
        return jsonify({'message': 'Usuario no registrado1'}), 404
    return jsonify(user.serialize())
    # return jsonify({'message':'Bienvenido'}), 201


def get_user2(iduser):
    user= User.get_by_id(iduser)
    if not user:
        return jsonify({'message': 'Usuario no registradossss'}), 404
    return jsonify(user.serialize()),205
    # return jsonify({'message': user.Nombre()}), 205




def create_user(): 
    data = request.json

    if not data or 'id_user' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    try:

        new_user = User(id_user=data['id_user'],email=data['email'],password=data['password'],
                        nombre=data['nombre'],apellido=data['apellido'],pais=data['pais'],
                        nacional=data['nacional'],phone=data['phone'],fechaN=data['fechaN'])
        new_user.save()
        return jsonify({'message':'Usuario registrado con exito'}), 201

    except Exception as e:
        # Manejar errores específicos como violación de unicidad
        return jsonify({'Error': str(e)}), 500
    


def find_user():
    data = request.json
    if not data or 'id_user' not in data or 'password' not in data:
        return jsonify({'error': 'Faltan datos requeridos'}), 400
    
    try:

        user = User.get_by_user(data['id_user'],data['password'])

        return jsonify({'message':'Bienvenido'}), 201
    except Exception as e:
        # Manejar errores específicos como violación de unicidad
        return jsonify({'Error': str(e)}), 500




def update_user(iduser):
    user = User.get_by_id(iduser)
    if not user:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    data = request.json
    user.nombre = data['nombre']
    # user.apellido = data['apellido']
    # user.pais = data['pais']
    # user.nacional = data['nacional']
    user.newsave()
    return jsonify({'message': 'Usuario successfully'}),201

def delete_user(iduser):
    user = User.get_by_id(iduser)
    if not user:
        return jsonify({'message': 'Movie not found'}), 404
    user.delete()
    return jsonify({'message': 'Movie deleted successfully'})