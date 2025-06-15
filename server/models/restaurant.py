from server.app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')
    
    def to_dict(self, include_pizzas=False):
        data = {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }
        
        if include_pizzas:
            data['restaurant_pizzas'] = [rp.to_dict(include_relations=True) for rp in self.restaurant_pizzas]
        
        return data
    
    def __repr__(self):
        return f'<Restaurant {self.name}>'