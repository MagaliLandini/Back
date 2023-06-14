from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,Date,
)
from api_config import (
    db,
)

from .objects import (
    Persona,Vehiculo,Registro,Infraccion
)
from .persona import Persona as PersonaModel
from .vehiculo import Vehiculo as VehiculoModel
from .infraccion import Infraccion as InfraccionModel
from .registro import Registro as RegistroModel

class createPersona(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    persona = Field(lambda: Persona)

    def mutate(self, info, name, last_name, email=None):
        persona = PersonaModel(name=name, last_name=last_name, email=email)

        db.session.add(persona)
        db.session.commit()

        return createPersona(persona=persona)

class updatePersona(Mutation):
    class Arguments:
        persona_id = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    persona = Field(lambda: Persona)

    def mutate(self, info, persona_id, email=None, name=None, last_name=None):
        persona = PersonaModel.query.get(persona_id)
        if persona:
            if email:
                persona.email = email
            if name:
                persona.name = name
            if last_name:
                persona.last_name = last_name
            db.session.add(persona)
            db.session.commit()

        return updatePersona(persona=persona)


class deletePersona(Mutation):
    class Arguments:
        persona_id = Int(required=True)

    persona = Field(lambda: Persona)

    def mutate(self, info, persona_id):
        persona = PersonaModel.query.get(persona_id)
        if persona:
            db.session.delete(persona)
            db.session.commit()

        return deletePersona(persona=persona)

class createVehiculo(Mutation):
    class Arguments:
        patente = String(required=True)
        categoria_vehiculo = String(required=True)
        anio_fabricacion = Int(required=True)
        nombre_propietario = String(required=True)
        domicilio_propietario = String(required=True)
    
    vehiculo = Field(lambda: Vehiculo)

    def mutate(self, info, patente, categoria_vehiculo, anio_fabricacion,nombre_propietario,domicilio_propietario):
        vehiculo = VehiculoModel(patente=patente, categoria_vehiculo=categoria_vehiculo, anio_fabricacion=anio_fabricacion,nombre_propietario=nombre_propietario,domicilio_propietario=domicilio_propietario)

        db.session.add(vehiculo)
        db.session.commit()

        return createVehiculo(vehiculo=vehiculo)
    
class updateVehiculo(Mutation):
    class Arguments:
        patente = String(required=True)
        categoria_vehiculo = String()
        anio_fabricacion = Int()
        nombre_propietario = String()
        domicilio_propietario = String()

    vehiculo = Field(lambda: Vehiculo)

    def mutate(self, info, patente, categoria_vehiculo=None, anio_fabricacion=None,nombre_propietario=None,domicilio_propietario=None):
        vehiculo = VehiculoModel.query.get(patente)
        if vehiculo:
            if categoria_vehiculo:
                vehiculo.categoria_vehiculo = categoria_vehiculo
            if anio_fabricacion:
                vehiculo.anio_fabricacion = anio_fabricacion
            if nombre_propietario:
                vehiculo.nombre_propietario = nombre_propietario
            if domicilio_propietario:
                vehiculo.domicilio_propietario = domicilio_propietario

        db.session.add(vehiculo)
        db.session.commit()

        return updateVehiculo(vehiculo=vehiculo)


class deleteVehiculo(Mutation):
    class Arguments:
        patente = String(required=True)

    vehiculo = Field(lambda: Vehiculo)

    def mutate(self, info, patente):
        vehiculo = VehiculoModel.query.get(patente)
        if vehiculo:
            db.session.delete(vehiculo)
            db.session.commit()

        return deleteVehiculo(vehiculo=vehiculo)
    
class createRegistro(Mutation):
    class Arguments:
        numero = Int(required=True)
        nombre_chofer = String(required=True)
        domicilio_chofer = String(required=True)
        edad = Int(required=False)
        grupo_sanguineo = String(required=True)
        categoria = String(required=True)
        fecha_emision = Date(required=True)
        fecha_vencimiento = Date(required=True)
        

    
    registro = Field(lambda: Registro)

    def mutate(self, info, numero, nombre_chofer, domicilio_chofer,edad,grupo_sanguineo,categoria,fecha_emision,fecha_vencimiento):
        resgitro = RegistroModel(numero=numero, nombre_chofer=nombre_chofer, domicilio_chofer=domicilio_chofer,edad=edad,grupo_sanguineo=grupo_sanguineo,categoria=categoria,fecha_emision=fecha_emision,fecha_vencimiento=fecha_vencimiento)

        db.session.add(resgitro)
        db.session.commit()

        return createRegistro(registro=resgitro)
    
class updateRegistro(Mutation):
    class Arguments:
        numero = Int(required=True)
        nombre_chofer = String()
        domicilio_chofer = String()
        edad = Int()
        grupo_sanguineo = String()
        categoria = String()
        fecha_emision = Date()
        fecha_vencimiento = Date()

    registro = Field(lambda: Registro)

    def mutate(self, info, numero, nombre_chofer=None, domicilio_chofer=None,edad=None,grupo_sanguineo=None, categoria = None, fecha_emision = None, fecha_vencimiento =None ):
        registro = RegistroModel.query.get(numero)
        if registro:
            if nombre_chofer:
                registro.nombre_chofer = nombre_chofer
            if domicilio_chofer:
                registro.domicilio_chofer = domicilio_chofer
            if edad:
                registro.edad = edad
            if grupo_sanguineo:
                registro.grupo_sanguineo = grupo_sanguineo
            if categoria:
                registro.categoria = categoria
            if fecha_emision:
                registro.fecha_emision = fecha_emision
            if fecha_vencimiento:
                registro.fecha_vencimiento = fecha_vencimiento

        db.session.add(registro)
        db.session.commit()

        return updateRegistro(registro=registro)


class deleteRegistro(Mutation):
    class Arguments:
        numero = Int(required=True)

    registro = Field(lambda: Registro)

    def mutate(self, info, numero):
        registro = RegistroModel.query.get(numero)
        if registro:
            db.session.delete(registro)
            db.session.commit()

        return deleteRegistro(registro=registro)

class createInfraccion(Mutation):
    class Arguments:
        numero_infraccion = Int(required=True)
        fecha_infraccion = Int(required=True)
        tipo_infraccion= String(required=True)
        observaciones = String(required=False)
        patente = String(required=True)
        numero = Int(required=True)
        
    infraccion = Field(lambda: Infraccion)

    def mutate(self, info,tipo_infraccion,numero_infraccion, fecha_infraccion, observaciones,patente,numero):
        infraccion = InfraccionModel(tipo_infraccion=tipo_infraccion,numero_infraccion=numero_infraccion, fecha_infraccion=fecha_infraccion, observaciones=observaciones,patente=patente,numero=numero)

        db.session.add(infraccion)
        db.session.commit()

        return createInfraccion(infraccion=infraccion)
    
class updateInfraccion(Mutation):
    class Arguments:
        numero_infraccion = Int(required=True)
        fecha_infraccion = Int(required=True)
        tipo_infraccion= String(required=True)
        observaciones = String()
        patente = String()
        numero = Int()

    infraccion = Field(lambda: Infraccion)

    def mutate(self, info,tipo_infraccion, numero_infraccion, fecha_infraccion=None, observaciones=None,patente=None,numero=None):
        infraccion = InfraccionModel.query.get(numero_infraccion)
        if infraccion:
            if tipo_infraccion:
                infraccion.tipo_infraccion= tipo_infraccion
            if fecha_infraccion:
                infraccion.fecha_infraccion = fecha_infraccion
            if observaciones:
                infraccion.observaciones = observaciones
            if patente:
                infraccion.patente = patente
            if numero:
                infraccion.numero = numero

        db.session.add(infraccion)
        db.session.commit()

        return updateInfraccion(infraccion=infraccion)


class deleteInfraccion(Mutation):
    class Arguments:
        numero_infraccion = Int(required=True)

    infraccion = Field(lambda: Infraccion)

    def mutate(self, info, numero_infraccion):
        infraccion = InfraccionModel.query.get(numero_infraccion)
        if infraccion:
            db.session.delete(infraccion)
            db.session.commit()

        return deleteInfraccion(infraccion=infraccion)
class Mutation(ObjectType):
    create_persona = createPersona.Field()
    create_vehiculo = createVehiculo.Field()
    create_registro = createRegistro.Field()
    create_infraccion = createInfraccion.Field()
    update_persona = updatePersona.Field()
    update_vehiculo = updateVehiculo.Field()
    update_registro = updateRegistro.Field()
    update_Infraccion = updateInfraccion.Field()
    delete_persona = deletePersona.Field()
    delete_vehiculo = deleteVehiculo.Field()
    delete_registro = deleteRegistro.Field()
    delete_infraccion = deleteInfraccion.Field()