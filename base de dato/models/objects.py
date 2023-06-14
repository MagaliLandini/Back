"""lalala"""
from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    # Int
    String
)
from models.departamento import Departamento as DepartamentoModel
from models.persona import Persona as PersonaModel
from models.vehiculo import Vehiculo as VehiculoModel
from models.registro import Registro as RegistroModel
from models.infraccion import Infraccion as InfraccionModel

class Persona(SQLAlchemyObjectType):
    class Meta:
        model = PersonaModel
    name = String(description='representa el nombre de la persona')

class Departamento(SQLAlchemyObjectType):
    class Meta:
        model = DepartamentoModel
        # exclude_fields = ('fk_persona')

class Vehiculo(SQLAlchemyObjectType):
    class Meta:
        model = VehiculoModel

class Registro(SQLAlchemyObjectType):
    class Meta:
        model = RegistroModel
class Infraccion(SQLAlchemyObjectType):
    class Meta:
        model = InfraccionModel

# class User(SQLAlchemyObjectType):
#     class Meta:
#         model = UserModel