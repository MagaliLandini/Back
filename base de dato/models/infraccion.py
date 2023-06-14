from api_config import db


class Infraccion(db.Model):
    __tablename__ = "infraccion"
    numero_infraccion = db.Column(db.Integer, primary_key=True)
    fecha_infraccion = db.Column(db.Integer)
    observaciones = db.Column(db.String(200))
    tipo_infraccion= db.Column(db.String(50))
    patente =db.Column(db.String(10), db.ForeignKey("vehiculo.patente"))
    vehiculo = db.relationship("Vehiculo",backref ='infraccion')
    numero =db.Column(db.Integer, db.ForeignKey("registro.numero"))
    registro = db.relationship("Registro",backref ='infraccion')

  



	#CONSTRAINT infraccion_frkey FOREIGN KEY (patente) 
	#REFERENCES vehiculo (patente),
	#CONSTRAINT infraccion_frkey FOREIGN KEY (numero) 
	#REFERENCES registro (numero)

