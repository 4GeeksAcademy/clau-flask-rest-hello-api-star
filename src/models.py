from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            "email": self.email
            # do not serialize the password, its a security breach
        }


class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(120), unique=True, nullable=False)
    mass = db.Column(db.String(120), unique=True, nullable=False)
    hair_color = db.Column(db.String(120), unique=True, nullable=False)
    skin_color = db.Column(db.String(120), unique=True, nullable=False)
    eye_color = db.Column(db.String(120), unique=True, nullable=False)
    birth_year = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<Personajes %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender

            # do not serialize the password, its a security breach
        }
    

class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(120), unique=True, nullable=False)
    gravity = db.Column(db.String(120), unique=True, nullable=False)
    rotation_period = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "created": self.created,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "rotation_period": self.rotation_period,

            # do not serialize the password, its a security breach
        }

class Vehiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    cargo_capacity = db.Column(db.String(120), unique=True, nullable=False)
    cost_in_credit = db.Column(db.String(120), unique=True, nullable=False)
    length = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=True, nullable=False)
    passengers = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<Vehiculos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "cargo_capacity": self.cargo_capacity,
            "cost_in_credit": self.cost_in_credit,
            "length": self.length,
            "model": self.model,
            "passengers": self.passengers,

            # do not serialize the password, its a security breach
        }
    
class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    cargo_capacity = db.Column(db.String(120), unique=True, nullable=False)
    cost_in_credit = db.Column(db.String(120), unique=True, nullable=False)
    length = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=True, nullable=False)
    passengers = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return '<Vehiculos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "cargo_capacity": self.cargo_capacity,
            "cost_in_credit": self.cost_in_credit,
            "length": self.length,
            "model": self.model,
            "passengers": self.passengers,

            # do not serialize the password, its a security breach
        }



class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    
    personajes_id = db.Column(db.Integer, db.ForeignKey('personajes.id'))
    planetas_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))
    vehiculos_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'))
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    user = db.relationship(User)
    personajes = db.relationship(Personajes)
    planetas = db.relationship(Planetas)
    vehiculos = db.relationship (Vehiculos)
    starships = db.relationship(Starships)

    


    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personajes_id": self.personajes_id,
            "planetas_id": self.planetas_id,
            "vehiculos_id": self.vehiculos_id,
            "starships_id": self.starships_id

            # do not serialize the password, its a security breach
        }