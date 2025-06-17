from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate

from .models import db 

from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    db.init_app(app)
    migrate.init_app(app, db)

    # --- Routes ---
    @app.route('/')
    def home():
        return "<h1>Pizza Restaurant API</h1>"

    @app.route('/restaurants', methods=['GET'])
    def get_restaurants():
        restaurants = Restaurant.query.all()
        restaurants_data = [r.to_dict() for r in restaurants]
        return make_response(jsonify(restaurants_data), 200)

    @app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
    def restaurant_by_id(id):
        restaurant = db.session.get(Restaurant, id)
        
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)

        if request.method == 'GET':
            restaurant_data = restaurant.to_dict()
            restaurant_data['pizzas'] = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
            return make_response(jsonify(restaurant_data), 200)

        elif request.method == 'DELETE':
            db.session.delete(restaurant)
            db.session.commit()
            return make_response('', 204)

    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        pizzas = Pizza.query.all()
        pizzas_data = [p.to_dict() for p in pizzas]
        return make_response(jsonify(pizzas_data), 200)

    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        if not isinstance(price, int) or not (1 <= price <= 30):
            return make_response(jsonify({"errors": ["Price must be between 1 and 30"]}), 400)
        
        pizza = db.session.get(Pizza, pizza_id)
        restaurant = db.session.get(Restaurant, restaurant_id)

        if not pizza or not restaurant:
            return make_response(jsonify({"errors": ["Validation errors"]}), 400)

        new_rp = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        
        db.session.add(new_rp)
        db.session.commit()
        
        response_data = new_rp.pizza.to_dict()
        
        return make_response(jsonify(response_data), 201)

    return app
