from models.usuario import UsuarioModel
from flask_restful import Resource, request
from base_de_datos import conexion
from dtos.usuario import UsuarioRequestDTO
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

class UsuariosController(Resource):
    def get(self):
        usuarios = conexion.session.query(UsuarioModel).all()
        dto = UsuarioRequestDTO()
        resultado = dto.dump(usuarios,many=True)

        return resultado

    def post(self):
        data=request.json
        print(data)
        dto = UsuarioRequestDTO()
        try:
            dataValidada = dto.load(data)
            print(dataValidada)
            nuevoUsuario = UsuarioModel(**dataValidada)
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            return {
                'message' : 'Usuario Insertado'
            }, 201
        
        except ValidationError as error:
            return {
                'message':'Error al crear al usuario',
                'error':error.args
            },400
        
        except IntegrityError as error:
            return {
                'message':'Error al crear el usuario',
                'error':'El usuario ya existe'
            },400
        
        except Exception as error:
            return {
                'message':'Error al crear el usuario',
                'error': error.args
            },400

class UsuarioController(Resource):
    def put(self, id):
        # SELECT * FROM usuarios WHERE id = '...'
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = id).first()
        if not usuarioEncontrado:
            return {
                'message': 'El usuario a actualizar no existe'
            }, 404
        
        data = request.get_json()
        dto = UsuarioRequestDTO()
        try:
            dataValidada = dto.load(data)
            # UPDATE usuarios SET nombre='...', apellido='...' ... WHERE id = '...';
            usuarioActualizados = conexion.session.query(UsuarioModel).filter_by(id=id).update(dataValidada)

            print(usuarioActualizados)

            conexion.session.commit()

            return {
                'message': 'Usuario actualizado exitosamente'
            }
        except ValidationError as error:
            return {
                'message': 'Error al actualizar el usuario',
                'content': error.args
            }
        
        except IntegrityError as error:
            errorTexto: str = error.args[0]
            columna = errorTexto.split('la llave')[1]
            if columna.find('correo'):
                return {
                    'message': 'Error al actualizar el usuario',
                    'content': 'Usuario con ese correo ya existe'
                }
            elif columna.find('nombre'):
                return {
                    'message': 'Error al actualizar el usuario',
                    'content': 'Usuario con ese nombre ya existe'
                }

    def delete(self, id):
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        if not usuarioEncontrado:
            return {
                'message': 'El usuario no existe'
            }, 404
        
        # DELETE FROM usuarios WHERE id ='...';
        usuarioBorrados = conexion.session.query(UsuarioModel).filter_by(id=id).delete()
        print(usuarioBorrados)
        conexion.session.commit()

        return {
            'message': 'Usuario eliminado exitosamente'
        }

    def get(self, id):
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        if not usuarioEncontrado:
            return {
                'message': 'El usuario no existe'
            }, 404
        
        dto = UsuarioRequestDTO()
        usuarioConvertido = dto.dump(usuarioEncontrado)

        return {
            'content': usuarioConvertido
        }    