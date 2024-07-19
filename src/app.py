"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure #La importación se hace al revés. Se importa "desde...el archivo x"
#from models import Person

#Configuración de Flask que nos configura el servidor. 
app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Creamos una instancia de la estructura que tiene datastructures.py.
# Concretamente llama a la class FamilyStructure, que tiene el init para que la clase pueda crearse. 
# Le pasamos "Jackson" porque es el valor que recibe la clase en last_name. 
jackson_family = FamilyStructure("Jackson")

# Permite que los errores se vean como un objeto Json
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Inicialización de la ruta /members
# Dentro crea la función que crea una variable "members" que recibe lo que se obtiene de get_all_members (devuelve members
# que es un array) Luego en el response devuelve la lista de members 

@app.route('/members', methods=['GET'])
def handle_hello():    
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    return jsonify(response_body), 200



# Creamos la ruta en la api y el servicio que va a recibir los datos
# necesarios para crear un nuevo miembro. Le quitamos el dato id, porque
# lo vamos a generar nosotros (en la función de _generateId. )
# Guardamos los datos recibidos en new_member
@app.route('/members', methods=['POST'])
def add_member():
    new_member = request.json
    member = jackson_family.add_member(new_member)
    if (member):
        return jsonify ({'Mensaje' : 'nuevo miembro añadido'}), 200
    return jsonify ({'Error' : 'error al añadir'}), 400


# ------- ENDPOINT PARA BORRAR A UN MIEMBRO ---------
@app.route ('/member/<int:member_id>', methods = ['DELETE'])
def delete_member(member_id):
    delete_member = request.json #???????????????????
    miembro_borrado = jackson_family.delete_member(member_id)
    if (miembro_borrado):
        return jsonify ({'Mensaje' : 'miembro borrado'}), 200
    return jsonify ({'Error' : 'error al borrar miembro'}), 400


# ------- ENDPOINT PARA MOSTRAR A UN MIEMBRO ---------
@app.route ('/mostrar/<int:member_id>', methods = ['GET'])
def mostrar (member_id):
    member =  jackson_family.get_member(member_id)
    if (member):
        response_body = {'Miembro' : member}
        return (response_body), 200
    return jsonify ({'Error' : 'el miembro indicado no existe'}), 400



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
