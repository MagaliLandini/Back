from api_config import db


class Vehiculo(db.Model):
    __tablename__ = "vehiculo"
    patente = db.Column(db.String(10), primary_key=True)
    categoria_vehiculo = db.Column(db.String(50))
    anio_fabricacion = db.Column(db.Integer)
    nombre_propietario =db.Column(db.String(50))
    domicilio_propietario =db.Column(db.String(50))
