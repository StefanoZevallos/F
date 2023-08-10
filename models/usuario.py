from sqlalchemy import Column,types
from base_de_datos import conexion

class UsuarioModel(conexion.Model):
    id = Column(type_=types.Integer , primary_key=True , autoincrement = True)
    nombre = Column(type_=types.Text , nullable=False)
    apellido = Column(type_=types.Text , nullable=False)
    correo = Column(type_=types.Text , unique=True , nullable=False)
    telefono = Column(type_=types.Text ,nullable=True)
    linkedinUrl = Column(name='linkedin_url',type_=types.Text)
    __tablename__ = 'usuarios'
