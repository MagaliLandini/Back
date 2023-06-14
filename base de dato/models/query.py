from graphene import (
    ObjectType,
    String,
    Boolean,
    List,
    Int,Date
)
from .persona import Persona as PersonaModel
from .objects import Persona, Departamento,Vehiculo, Registro, Infraccion
from .departamento import Departamento as DepartamentoModel
from .vehiculo import Vehiculo as VehiculoModel
from .registro import Registro as RegistroModel
from .infraccion import Infraccion as InfraccionModel

class Query(ObjectType):
    personas = List(lambda: Persona, last_name=String(), id=Int(), has_email=Boolean(), order_by_name=Boolean())
    departamentos = List(lambda: Departamento)
    vehiculo = List(lambda: Vehiculo,patente=String(), categoria_vehiculo=String(),anio_fabricacion=Int(),nombre_propietario=String(),domicilio_propietario=String())
    registro = List (lambda:Registro,numero=Int(),nombre_chofer=String(),domicilio_chofer=String(),edad=Int(),grupo_sanguineo=String(),categoria=String(),fecha_emision=Date(),fecha_vencimiento=Date())
    infraccion = List (lambda : Infraccion,numero_infraccion=Int(),fecha_infraccion=Int(),observaciones=String(),patente=String())

    def resolve_personas(self, info, id=None, last_name=None, has_email=None, order_by_name=None):
        query = Persona (info=info)
        if id:
            query = query.filter(PersonaModel.id==id)
        if last_name:
            query = query.filter(PersonaModel.last_name==last_name)
        if has_email is not None:
            if has_email:
                query = query.filter(PersonaModel.email != None)
            else:
                query = query.filter(PersonaModel.email == None)
        if order_by_name:
            query = query.order_by(PersonaModel.name)
        return query.all()
    
    def resolve_departamentos(self, info):
        query = Departamento.get_query(info=info)
        return query.all()
    
    def resolve_vehiculo(self, info, patente=None, categoria_vehiculo=None, anio_fabricacion=None, nombre_propietario=None,domicilio_propietario=None):
        query = Vehiculo.get_query(info=info)
        if patente:
            query= query.filter(VehiculoModel.patente==patente)
        if categoria_vehiculo:
            query=query.filter(VehiculoModel.categoria_vehiculo==categoria_vehiculo)
        if anio_fabricacion:
            query= query.filter(VehiculoModel.anio_fabricacion==anio_fabricacion)
        if nombre_propietario:
            query= query.filter(VehiculoModel.nombre_propietario==nombre_propietario)
        if domicilio_propietario:
            query= query.filter(VehiculoModel.domicilio_propietario==domicilio_propietario)
        return query.all()
    
    def resolve_registro(self, info,numero=None,nombre_chofer=None,domicilio_chofer=None,edad=None,grupo_sanguineo=None,categoria=None,fecha_emision=None,fecha_vencimiento=None):
        query = Registro.get_query (info=info)
        if numero:
            query=query.filter(RegistroModel.numero==numero)
        if nombre_chofer:
            query=query.filter(RegistroModel.nombre_chofer==nombre_chofer)
        if edad:
            query=query.filter(RegistroModel.edad==edad)
        if grupo_sanguineo:
            query=query.filter(RegistroModel.grupo_sanguineo==grupo_sanguineo)
        if fecha_emision:
            query=query.filter(RegistroModel.fecha_emision==fecha_emision)
        if fecha_vencimiento:
            query=query.filter(RegistroModel.fecha_vencimiento==fecha_vencimiento)
        return query.all()
    
    def resolve_infraccion(self, info,numero_infraccion=None,fecha_infraccion=None,observaciones=None,patente=None):
        query = Infraccion.get_query (info=info)
        if numero_infraccion:
            query=query.filter(InfraccionModel.numero_infraccion==numero_infraccion)
        if fecha_infraccion:
            query=query.filter(InfraccionModel.fecha_infraccion==fecha_infraccion)
        if patente:
            query:query.filter(InfraccionModel.patente==patente)
        return query.all()
