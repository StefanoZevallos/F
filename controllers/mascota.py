from base_de_datos import conexion
from models.mascota import MascotaModel
from flask_restful import Resource, request
from dtos.mascota import MascotaRequestDTO

class MascotasController(Resource):

    def post(self):
        body = request.get_json()
        dto = MascotaRequestDTO()
        try:
            dto.load(body)
            return {
                'message':'Mascota creada exitosamente'
            },201
        except Exception as e:
            return {
                'message':'Error al crear la mascota',
                'content': e.args
            },400