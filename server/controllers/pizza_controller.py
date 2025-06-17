
from flask import jsonify
from server.models.pizza import Pizza

def init_pizza_routes(app):
    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        pizzas = Pizza.query.all()
        return jsonify([pizza.to_dict() for pizza in pizzas])