"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planetas, Personajes, Vehiculos, Starships, Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Endpoints
# Obtener todos los usuarios

@app.route('/user', methods=['GET'])
def obtener_usuarios():

# Hago una consulta a la tabla usuarios para que traiga todos los usuarios
    users_query = User.query.all ()


# mapeamos para  convertir el array en un array de objetos

    results = list(map(lambda item: item.serialize(), users_query))
    print(results)

#    respondo si no hay usuarios 
    if results == [] :
        return jsonify ({"msg":"No hay usuarios"}), 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": results
    }

    return jsonify(response_body), 200


    # Obtener  un usuario

@app.route('/user/<int:usuario_id>', methods=['GET'])
def consulto_un_usuario(usuario_id):


    # Hago una consulta a la tabla usuarios para que traiga un usuario
    usuario_query = User.query.filter_by (id=usuario_id).first ()

    # Respondo si no existe el  usuario consultado

    if usuario_query is None :
        return jsonify ({"msg":"no existe usuario"}), 404

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": usuario_query.serialize()
    }

    # Responde mostrando el usuario consultado

    return jsonify(response_body), 200

# Obtener todos los planetas

@app.route('/planetas', methods=['GET'])
def obtener_planetas():

# Hago una consulta a la tabla usuarios para que traiga todos los planetas
    planetas_query = Planetas.query.all ()


# mapeamos para  convertir el array en un array de objetos

    results = list(map(lambda item: item.serialize(), planetas_query))
    print(results)

#    respondo si no hay planetas 
    if results == [] :
        return jsonify ({"msg":"No hay planetas"}), 404

    response_body = {
        "msg": "Hola, estos son los planetas ",
        "results": results
    }

    return jsonify(response_body), 200


    # Obtener  un planeta

@app.route('/planeta/<int:planeta_id>', methods=['GET'])
def consulto_un_planeta(planeta_id):


    # Hago una consulta a la tabla usuarios para que traiga un planeta
    planeta_query = Planetas.query.filter_by (id=planeta_id).first ()

    # Respondo si no existe el  planeta consultado

    if planeta_query is None :
        return jsonify ({"msg":"no existe este planeta"}), 404

    response_body = {
        "msg": "Hola, este es el planeta consultado ",
        "results": planeta_query.serialize()
    }

    # Responde mostrando el planeta consultado

    return jsonify(response_body), 200

# # Obtener todos los personajes

@app.route('/personajes', methods=['GET'])
def obtener_personajes():

# # Hago una consulta a la tabla Personajes para que traiga todos los personajes
    personajes_query = Personajes.query.all ()


# # mapeamos para  convertir el array en un array de objetos

    results = list(map(lambda item: item.serialize(), personajes_query))
    print(results)

# #    respondo si no hay personajes 
    if results == [] :
        return jsonify ({"msg":"No hay personajes"}), 404

    response_body = {
        "msg": "Hola, estos son los personajes ",
        "results": results
    }

    return jsonify(response_body), 200


# # Obtener  un personaje

@app.route('/personajes/<int:personaje_id>', methods=['GET'])
def consulto_un_personaje(personaje_id):


#     # Hago una consulta a la tabla personajes para que traiga un personaje
    personaje_query = Personajes.query.filter_by (id=personaje_id).first ()

#     # Respondo si no existe el  personaje consultado

    if personaje_query is None :
        return jsonify ({"msg":"no existe este personaje"}), 404

    response_body = {
        "msg": "Hola, este es el personaje consultado ",
        "results": personaje_query.serialize()
    }

#     # Responde mostrando el personaje consultado

    return jsonify(response_body), 200

# Obtener todos los vehiculos

@app.route('/vehiculos', methods=['GET'])
def obtener_vehiculos():

# Hago una consulta a la tabla vehiculos para que traiga todos los usuarios
    vehiculos_query = Vehiculos.query.all ()


# mapeamos para  convertir el array en un array de objetos

    results = list(map(lambda item: item.serialize(), vehiculos_query))
    print(results)

#    respondo si no hay usuarios 
    if results == [] :
        return jsonify ({"msg":"No hay vehiculos"}), 404

    response_body = {
        "msg": "Hola, aquí está tu lista de vehículos ",
        "results": results
    }

    return jsonify(response_body), 200


    # Obtener  un vehiculo

@app.route('/vehiculos/<int:vehiculo_id>', methods=['GET'])
def consulto_un_vehiculo(vehiculo_id):


    # Hago una consulta a la tabla Vehiculos para que traiga un vehiculos
    vehiculo_query = User.query.filter_by (id=vehiculo_id).first ()

    # Respondo si no existe el  vehiculo consultado

    if vehiculo_query is None :
        return jsonify ({"msg":"no existe vehiculo"}), 404

    response_body = {
        "msg": "Hola, esta es tu lista de vehículos ",
        "results": vehiculo_query.serialize()
    }

    # Responde mostrando el vehiculo consultado

    return jsonify(response_body), 200

# Obtener todos los Starships

@app.route('/starships', methods=['GET'])
def obtener_starships():

# Hago una consulta a la tabla vehiculos para que traiga todos los usuarios
    starships_query = Starships.query.all ()


# mapeamos para  convertir el array en un array de objetos

    results = list(map(lambda item: item.serialize(), starships_query))
    print(results)

#    respondo si no hay starships 
    if results == [] :
        return jsonify ({"msg":"No hay naves"}), 404

    response_body = {
        "msg": "Hola, aquí está tu lista de naves ",
        "results": results
    }

    return jsonify(response_body), 200


    # Obtener  un starships

@app.route('/starships/<int:starship_id>', methods=['GET'])
def consulto_un_starship(starship_id):


    # Hago una consulta a la tabla starship para que traiga un vehiculos
    starship_query = Starships.query.filter_by (id=starship_id).first ()

    # Respondo si no existe el  starship consultado

    if starship_query is None :
        return jsonify ({"msg":"no existe starship"}), 404

    response_body = {
        "msg": "Hola, esta es tu lista de starship ",
        "results": starship_query.serialize()
    }

    # Responde mostrando el starships consultado

    return jsonify(response_body), 200

# Obtener todos los Favoritos

@app.route('/favoritos', methods=['GET'])
def obtener_favoritos():

# Hago una consulta a la tabla favoritos para que traiga todos los favoritos
    favoritos_query =Favoritos.query.all ()


# mapeamos para  convertir el array en un array de objetos

    results = list(map(lambda item: item.serialize(), favoritos_query))
    print(results)

#    respondo si no hay favoritos 
    if results == [] :
        return jsonify ({"msg":"No hay favoritos"}), 404

    response_body = {
        "msg": "Hola, aquí está tu lista de favoritos ",
        "results": results
    }

    return jsonify(response_body), 200


    # Obtener  un favorito para un usuario

@app.route('/users/<int:id>/favoritos', methods=['GET'])
def consulto_un_favorito(id):

    # Hago una consulta a la tabla favorito para que traiga un favorito
    favoritos_query = Favoritos.query.filter_by (user_id=id)
    response = list(map(lambda user:user.serialize(), favoritos_query))

    # Respondo si no existe el  favorito consultado

    if response == [] :
        return jsonify ({"msg":"no hay ningun favorito"}), 404

    response_body = {
        "msg": "Hola, esta es tu lista de starship ",
        "results": response
    }

    # Responde mostrando el favoritos consultado

    return jsonify(response_body), 200


#   Agregar planeta a favorito

@app.route('/favoritos/planetas/<int:planetas_id>', methods=['POST'])
def crear_planeta_favorito(planetas_id):
    request_body = request.get_json(force=True)
    nuevo_planeta_favorito=Favoritos(user_id= request_body["user_id"], planetas_id=planetas_id)
    db.session.add(nuevo_planeta_favorito)
    db.session.commit()


    request_body = {
        "msg": "planeta agregado a favorito"
    }
    
    return jsonify(request_body), 200
    














# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
