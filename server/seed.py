import random
from faker import Faker
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

pizza_names = [
    "Margherita",
    "Pepperoni",
    "Vegetarian",
    "Hawaiian",
    "BBQ Chicken",
    "Supreme",
    "Mushroom Delight",
    "Meat Lovers",
    "Four Cheese",
    "Pesto Paradise",
    "Buffalo Chicken",
    "Veggie Delight",
    "Spinach and Feta",
    "Chicken Alfredo",
    "Vegan Feast",
    "White Pizza",
    "Seafood Sensation",
    "Capricciosa",
    "Quattro Stagioni",
    "Truffle Tremor"
]
addresses = [
    "123 Main Street, Cityville, State 12345",
    "456 Elm Avenue, Townburg, State 67890",
    "789 Oak Lane, Villagetown, State 13579",
    "101 Pine Road, Hamletville, State 24680",
    "202 Cedar Street, Suburbia, State 98765",
    "303 Maple Drive, Countryside, State 43210",
    "404 Birch Court, Meadowville, State 56789",
    "505 Redwood Avenue, Hilltop, State 12345",
    "606 Spruce Lane, Lakeside, State 67890",
    "707 Willow Road, Riverside, State 13579",
    "808 Sycamore Street, Mountainview, State 24680",
    "909 Juniper Lane, Beachtown, State 98765",
    "210 Cedar Street, Skyline, State 43210",
    "321 Birch Court, Highlands, State 56789",
    "432 Elm Avenue, Valleyview, State 12345",
    "543 Pine Road, Harbor, State 67890",
    "654 Oak Lane, Lakeshore, State 13579",
    "765 Maple Drive, Hillside, State 24680",
    "876 Redwood Avenue, Summit, State 98765",
    "987 Spruce Lane, Bayview, State 43210"
]
pizza_ingredients = [
    "Dough",
    "Tomato Sauce",
    "Cheese",
    "Pepperoni",
    "Mushrooms",
    "Green Peppers",
    "Onions",
    "Olives",
    "Bacon",
    "Ham",
    "Pineapple",
    "BBQ Chicken",
    "Artichokes",
    "Spinach",
    "Feta Cheese",
    "Sausage",
    "Salami",
    "Tomatoes",
    "Anchovies",
    "Jalapeños"
]

pizza_prices = [8.99, 9.99, 10.49, 11.99, 12.99, 13.49, 14.99, 15.49, 16.99, 17.49, 18.99, 19.49, 20.99, 21.49, 22.99, 23.49, 24.99, 25.49, 26.99, 27.49, 28.99]

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    restaurants = []
    for n in range(50):
        restaurant = Restaurant(name=fake.name(), address=random.choice(addresses))
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit()

    pizzas = []
    for i in range(50):
        pizza = Pizza(
            name=random.choice(pizza_names),
            ingredients=random.choice(pizza_ingredients)
        )
        pizzas.append(pizza)
        db.session.add(pizza)
        db.session.commit()

    restaurant_pizzas = []
    for i in range(50):
      pizza = random.choice(pizzas)
      restaurant = random.choice(restaurants)

      restaurant_pizza = RestaurantPizza(
        price = random.randint(1, 30),
        restaurant_id=restaurant.id,
        pizza_id=pizza.id
     )

      restaurant_pizzas.append(restaurant_pizza)
      db.session.add(restaurant_pizza)

      db.session.commit()

