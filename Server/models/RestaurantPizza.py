from . import db, SerializerMixin
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    
    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas')
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    
    @validates('price')
    def validate_price(self, key, price):
        if not isinstance(price, int) or not (1 <= price <= 30):
            raise ValueError("Price must be an integer between 1 and 30")
        return price
    
    def __repr__(self):
        return f'<RestaurantPizza Price: {self.price}>'
