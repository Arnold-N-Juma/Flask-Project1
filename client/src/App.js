import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [restaurants, setRestaurants] = useState([]);
  const [pizzas, setPizzas] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    async function fetchData() {
      try {
        const responseRestaurants = await axios.get('http://127.0.0.1:5000/restaurants');
        const responsePizzas = await axios.get('http://127.0.0.1:5000/pizzas');

        setRestaurants(responseRestaurants.data);
        setPizzas(responsePizzas.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData();
  }, []);

  const handleDeleteRestaurant = async (restaurantId) => {
    try {
      await axios.delete(`http://127.0.0.1:5000/restaurants/${restaurantId}`);

      setRestaurants((prevRestaurants) => prevRestaurants.filter((restaurant) => restaurant.id !== restaurantId));
    } catch (error) {
      console.error('Error deleting restaurant:', error);
    }
  };

  const filteredRestaurants = (restaurants || []).filter((restaurant) =>
    restaurant.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const filteredPizzas = (pizzas || []).filter((pizza) => pizza.name.toLowerCase().includes(searchQuery.toLowerCase()));

  return (
    <div className="container">
      <h1>Pizza Restaurants</h1>

      <input
        type="text"
        placeholder="Search for restaurants or pizzas"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />

      <ul>
        {filteredRestaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <h2>{restaurant.name}</h2>
            <p>{restaurant.address}</p>
            <button onClick={() => handleDeleteRestaurant(restaurant.id)}>Delete Restaurant</button>
            <ul>
              {(restaurant.pizzas || []).map((pizza) => (
                <li key={pizza.id}>
                  <strong>{pizza.name}</strong> - {pizza.ingredients}
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>

      <h1>Pizzas</h1>
      <ul>
        {filteredPizzas.map((pizza) => (
          <li key={pizza.id}>
            <strong>{pizza.name}</strong> - {pizza.ingredients}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

