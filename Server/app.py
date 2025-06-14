from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate

from config import Config
from models import db
from models.Restaurant import Restaurant
from models.Pizza import Pizza
from models.RestaurantPizza import RestaurantPizza

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app, db)
    
    @app.route('/')
    def home():
        return "<h1>Pizza Restaurant API</h1>"

    @app.route('/restaurants', methods=['GET'])
    def get_restaurants():
        restaurants = Restaurant.query.all()
        restaurants_data = [r.to_dict(rules=('-restaurant_pizzas',)) for r in restaurants]
        return make_response(jsonify(restaurants_data), 200)

    @app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
    def restaurant_by_id(id):
        restaurant = db.session.get(Restaurant, id)
        
        if not restaurant:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)

        if request.method == 'GET':
            restaurant_data = restaurant.to_dict(rules=('-restaurant_pizzas',))
            restaurant_data['pizzas'] = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
            return make_response(jsonify(restaurant_data), 200)

        elif request.method == 'DELETE':
            db.session.delete(restaurant)
            db.session.commit()
            return make_response('', 204)

    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        pizzas = Pizza.query.all()
        pizzas_data = [p.to_dict(rules=('-restaurant_pizzas',)) for r in pizzas]
        return make_response(jsonify(pizzas_data), 200)

    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.get_json()
        try:
            new_rp = RestaurantPizza(
                price=data.get('price'),
                pizza_id=data.get('pizza_id'),
                restaurant_id=data.get('restaurant_id')
            )
            db.session.add(new_rp)
            db.session.commit()
            
            pizza_data = new_rp.pizza.to_dict(rules=('-restaurant_pizzas',))
            return make_response(jsonify(pizza_data), 201)

        except ValueError as e:
            return make_response(jsonify({"errors": [str(e)]}), 400)
        except Exception:
            return make_response(jsonify({"errors": ["Validation errors"]}), 400)
 
    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555, debug=True)
