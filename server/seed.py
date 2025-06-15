#!/usr/bin/env python3

from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    app = create_app()
    
    with app.app_context():
       
        print("Clearing existing data...")
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()
        
       
        print("Creating restaurants...")
        restaurants = [
            Restaurant(name="Mario's Pizza", address="123 Main St, New York, NY"),
            Restaurant(name="Luigi's Pizzeria", address="456 Oak Ave, Brooklyn, NY"),
            Restaurant(name="Kiki's Pizza", address="789 Pine Rd, Queens, NY"),
            Restaurant(name="Tony's Italian", address="321 Elm St, Manhattan, NY"),
        ]
        
        for restaurant in restaurants:
            db.session.add(restaurant)
        
       
        print("Creating pizzas...")
        pizzas = [
            Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni"),
            Pizza(name="Supreme", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni, Sausage, Bell Peppers, Onions, Mushrooms"),
            Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Mozzarella, Ham, Pineapple"),
            Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Mozzarella, Bell Peppers, Onions, Mushrooms, Olives, Tomatoes"),
            Pizza(name="Meat Lovers", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni, Sausage, Bacon, Ham"),
        ]
        
        for pizza in pizzas:
            db.session.add(pizza)
        
       
        db.session.commit()
        
       
        print("Creating restaurant-pizza relationships...")
        restaurant_pizzas = [
            # Mario's Pizza
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=1),  # Margherita
            RestaurantPizza(price=15, restaurant_id=1, pizza_id=2),  # Pepperoni
            RestaurantPizza(price=18, restaurant_id=1, pizza_id=3),  # Supreme
            
            # Luigi's Pizzeria
            RestaurantPizza(price=11, restaurant_id=2, pizza_id=1),  # Margherita
            RestaurantPizza(price=16, restaurant_id=2, pizza_id=4),  # Hawaiian
            RestaurantPizza(price=14, restaurant_id=2, pizza_id=5),  # Veggie
            
            # Kiki's Pizza
            RestaurantPizza(price=13, restaurant_id=3, pizza_id=2),  # Pepperoni
            RestaurantPizza(price=20, restaurant_id=3, pizza_id=6),  # Meat Lovers
            RestaurantPizza(price=17, restaurant_id=3, pizza_id=3),  # Supreme
            
            # Tony's Italian
            RestaurantPizza(price=10, restaurant_id=4, pizza_id=1),  # Margherita
            RestaurantPizza(price=15, restaurant_id=4, pizza_id=5),  # Veggie
            RestaurantPizza(price=22, restaurant_id=4, pizza_id=6),  # Meat Lovers
        ]
        
        for rp in restaurant_pizzas:
            db.session.add(rp)
        
        db.session.commit()
        
        print("Seeding completed successfully!")
        print(f"Created {len(restaurants)} restaurants")
        print(f"Created {len(pizzas)} pizzas")
        print(f"Created {len(restaurant_pizzas)} restaurant-pizza relationships")

if __name__ == '__main__':
    seed_data()