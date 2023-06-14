from api_config import db


class Registro(db.Model):
    __tablename__ = "registro"
    numero = db.Column(db.Integer, primary_key=True)
    nombre_chofer = db.Column(db.String(50))
    domicilio_chofer = db.Column(db.String(50))
    edad =db.Column(db.Integer)
    grupo_sanguineo =db.Column(db.String(5))
    categoria = db.Column(db.String(10))
    fecha_emision = db.Column(db.Date)
    fecha_vencimiento = db.Column(db.Date)
    