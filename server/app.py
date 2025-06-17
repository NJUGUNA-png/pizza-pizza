
from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

@app.route('/')
def home():
    return "Pizza Restaurant API"

if __name__ == '__main__':
    app.run(debug=True)
from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.controllers.restaurant_controller import init_restaurant_routes
from server.controllers.pizza_controller import init_pizza_routes
from server.controllers.restaurant_pizza_controller import init_restaurant_pizza_routes

app = create_app()


init_restaurant_routes(app)
init_pizza_routes(app)
init_restaurant_pizza_routes(app)

@app.route('/')
def home():
    return "Pizza Restaurant API"

if __name__ == '__main__':
    app.run(debug=True)