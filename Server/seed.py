# To run this seed file, run `python -m Server.seed` from the root directory.

from .app import create_app
# Import db from the models package, and each model from its specific file
from .models import db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

app = create_app()

def seed_database():
    with app.app_context():
        print("Clearing database...")
        # Use the class names for queries
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()

        print("Seeding restaurants...")
        # Use the class names to create instances
        restaurants = [
            Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201"),
            Restaurant(name="Pizzana", address="11712 San Vicente Blvd, Los Angeles, CA 90049"),
            Restaurant(name="Frank Pepe Pizzeria Napoletana", address="157 Wooster St, New Haven, CT 06511")
        ]
        db.session.add_all(restaurants)
        db.session.commit()

        print("Seeding pizzas...")
        pizzas = [
            Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Mozzarella"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni"),
            Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Fresh Mozzarella, Basil"),
            Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Mozzarella, Bell Peppers, Onions, Olives")
        ]
        db.session.add_all(pizzas)
        db.session.commit()

        print("Seeding restaurant-pizza associations...")
        associations = [
            RestaurantPizza(price=15, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=18, restaurant_id=1, pizza_id=3),
            RestaurantPizza(price=20, restaurant_id=2, pizza_id=2),
            RestaurantPizza(price=22, restaurant_id=2, pizza_id=4),
            RestaurantPizza(price=17, restaurant_id=3, pizza_id=1),
            RestaurantPizza(price=19, restaurant_id=3, pizza_id=2),
            RestaurantPizza(price=30, restaurant_id=1, pizza_id=2) 
        ]
        db.session.add_all(associations)
        db.session.commit()
        
        print("Seeding complete!")

if __name__ == '__main__':
    seed_database()
