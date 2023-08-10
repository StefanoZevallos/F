from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.mascota import MascotaModel

class MascotaRequestDTO(SQLAlchemyAutoSchema):
    class Meta:
        model=MascotaModel
        include_fk=True