CREATE TABLE persona (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (150)
);

CREATE TABLE departamento (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	fk_persona integer,
	CONSTRAINT depto_frkey FOREIGN KEY (fk_persona) 
	REFERENCES persona (id)
);

CREATE TABLE vehiculo (
	patente VARCHAR(10) PRIMARY KEY,
	categoria_vehiculo VARCHAR (50) NOT NULL,
	anio_fabricacion integer,
	nombre_propietario VARCHAR(50) NOT NULL,
	domicilio_propietario VARCHAR (50) NOT NULL,
	
);

CREATE TABLE registro (
	numero integer PRIMARY KEY,
	nombre_chofer VARCHAR (50) NOT NULL,
	domicilio_chofer VARCHAR (50) NOT NULL,
	edad integer,
	grupo_sanguineo VARCHAR(5) NOT NULL,
	categoria VARCHAR(10) NOT NULL,
	fecha_emision DATE NOT NULL,
	fecha_vencimiento DATE NOT NULL,
	
);

CREATE TABLE infraccion (
	numero_infraccion serial PRIMARY KEY,
	tipo_infraccion VARCHAR (50) NOT NULL,
	fecha_infraccion integer,
	observaciones VARCHAR(200),
	patente VARCHAR (10),
	numero integer,
	CONSTRAINT infraccion_frkey FOREIGN KEY (patente) 
	REFERENCES vehiculo (patente),
	CONSTRAINT infraccion_frkey FOREIGN KEY (numero) 
	REFERENCES registro (numero)

	
);


INSERT INTO persona (name, last_name) VALUES ('Juan', 'Saldivia');


SELECT * FROM persona;

SELECT * FROM persona WHERE id = 2;

DELETE FROM persona WHERE id = 2;

UPDATE persona SET email = 'algo@algo.com' WHERE id = 15;

select * from departamento d join persona p on (d.fk_persona = p.id) where p.id =1;


mutation{
  createPersona(name: "Tito", lastName: "Ledesma", email: "asds@asd.asd"){
    persona{
      id
      name
      lastName
      email 
    }
  }
}