
from flask import jsonify, request
from server import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

def init_restaurant_pizza_routes(app):
    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.get_json()
        
        
        required_fields = ['price', 'pizza_id', 'restaurant_id']
        if not all(field in data for field in required_fields):
            return jsonify({"errors": ["Missing required fields"]}), 400
        
        
        price = data['price']
        if not isinstance(price, int) or price < 1 or price > 30:
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
        
        
        restaurant = Restaurant.query.get(data['restaurant_id'])
        pizza = Pizza.query.get(data['pizza_id'])
        
        if not restaurant or not pizza:
            return jsonify({"errors": ["Restaurant or Pizza not found"]}), 404
        
        
        try:
            restaurant_pizza = RestaurantPizza(
                price=price,
                pizza_id=data['pizza_id'],
                restaurant_id=data['restaurant_id']
            )
            
            db.session.add(restaurant_pizza)
            db.session.commit()
            
            return jsonify(restaurant_pizza.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"errors": [str(e)]}), 400