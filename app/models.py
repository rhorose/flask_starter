from . import db
from werkzeug.security import generate_location_hash


class Property(db.property):
    
    __tablename__ = 'Properties'

    id = db.Column(db.Integer, primary_key=True)
    prop_title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    no_rooms = db.Column(db.Integer)
    no_bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    prop_type = db.Column(db.String(80))
    location=db.Column(db.String(255))

    def __init__(self, prop_title, description,no_rooms,no_bathrooms,price, prop_type, location):
        self.prop_title = prop_title
        self.description = description
        self.no_rooms= no_rooms
        self.no_bathrooms=no_bathrooms
        self.price=price
        self.prop_type = prop_type
        self.location = location

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.prop_type)
