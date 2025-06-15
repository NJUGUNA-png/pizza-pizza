# Pizza Restaurant API

A Flask REST API for managing pizza restaurants with SQLAlchemy and MVC architecture.

## Quick Start

```bash
# Install dependencies
pipenv install flask flask-sqlalchemy flask-migrate
pipenv shell

# Setup database
export FLASK_APP=server/app.py
flask db init && flask db migrate -m "Initial migration" && flask db upgrade

# Seed data and run
python server/seed.py
python server/app.py
```

Server runs at `http://127.0.0.1:5000`

## API Endpoints

### Restaurants
- `GET /restaurants` - List all restaurants
- `GET /restaurants/<id>` - Get restaurant with pizzas (404 if not found)
- `DELETE /restaurants/<id>` - Delete restaurant (204 success, 404 if not found)

### Pizzas
- `GET /pizzas` - List all pizzas

### Restaurant-Pizza Relationships
- `POST /restaurant_pizzas` - Create relationship

**Request:**
```json
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Validation:** Price must be 1-30

## Project Structure

```
server/
├── app.py              
├── config.py           
├── models/             
│   ├── restaurant.py
│   ├── pizza.py
│   └── restaurant_pizza.py
├── controllers/       
└── seed.py            
```

## Models

**Restaurant:** id, name, address  
**Pizza:** id, name, ingredients  
**RestaurantPizza:** id, price (1-30), restaurant_id, pizza_id

Deleting a restaurant cascades to remove all its restaurant-pizza relationships.

## Testing

Import `challenge-1-pizzas.postman_collection.json` into Postman for pre-configured API tests.