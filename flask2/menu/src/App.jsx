import React, { useState, useEffect } from "react";
import axios from "axios";

const apiUrl = "http://127.0.0.1:6020/dish";

const RestaurantMenu = () => {
  const [dishes, setDishes] = useState([]);
  const [newDish, setNewDish] = useState({ name: "", calories: "", price: "" });
  const [editingDish, setEditingDish] = useState(null);

  useEffect(() => {
    fetchDishes();
  }, []);

  const fetchDishes = async () => {
    try {
      const response = await axios.get(apiUrl);
      setDishes(response.data);
    } catch (error) {
      console.error("Error fetching dishes:", error);
    }
  };

  const addDish = async () => {
    if (!newDish.name || !newDish.calories || !newDish.price) return;
    try {
      const response = await axios.post(apiUrl, newDish);
      setDishes([...dishes, response.data]);
      setNewDish({ name: "", calories: "", price: "" });
    } catch (error) {
      console.error("Error adding dish:", error);
    }
  };

  const updateDish = async () => {
    if (!editingDish) return;
    try {
      await axios.put(`${apiUrl}/${editingDish.id}`, editingDish);
      setDishes(
        dishes.map((dish) => (dish.id === editingDish.id ? editingDish : dish))
      );
      setEditingDish(null);
    } catch (error) {
      console.error("Error updating dish:", error);
    }
  };

  const deleteDish = async (id) => {
    try {
      await axios.delete(`${apiUrl}/${id}`);
      setDishes(dishes.filter((dish) => dish.id !== id));
    } catch (error) {
      console.error("Error deleting dish:", error);
    }
  };

  return (
    <div
      style={{
        fontFamily: "Arial",
        padding: "20px",
        maxWidth: "600px",
        margin: "auto",
      }}
    >
      <h2 style={{ textAlign: "center" }}>Restaurant Menu</h2>
      <div style={{ marginBottom: "20px" }}>
        <input
          type='text'
          placeholder='Dish Name'
          value={newDish.name}
          onChange={(e) => setNewDish({ ...newDish, name: e.target.value })}
          style={{ marginRight: "10px" }}
        />
        <input
          type='number'
          placeholder='Calories'
          value={newDish.calories}
          onChange={(e) => setNewDish({ ...newDish, calories: e.target.value })}
          style={{ marginRight: "10px" }}
        />
        <input
          type='number'
          placeholder='Price'
          value={newDish.price}
          onChange={(e) => setNewDish({ ...newDish, price: e.target.value })}
          style={{ marginRight: "10px" }}
        />
        <button
          onClick={addDish}
          style={{ padding: "5px 10px", cursor: "pointer" }}
        >
          Add
        </button>
      </div>
      {editingDish && (
        <div style={{ marginBottom: "20px" }}>
          <input
            type='text'
            value={editingDish.name}
            onChange={(e) =>
              setEditingDish({ ...editingDish, name: e.target.value })
            }
            style={{ marginRight: "10px" }}
          />
          <input
            type='number'
            value={editingDish.calories}
            onChange={(e) =>
              setEditingDish({ ...editingDish, calories: e.target.value })
            }
            style={{ marginRight: "10px" }}
          />
          <input
            type='number'
            value={editingDish.price}
            onChange={(e) =>
              setEditingDish({ ...editingDish, price: e.target.value })
            }
            style={{ marginRight: "10px" }}
          />
          <button
            onClick={updateDish}
            style={{ padding: "5px 10px", cursor: "pointer" }}
          >
            Update
          </button>
        </div>
      )}
      <ul style={{ listStyle: "none", padding: 0 }}>
        {dishes.map((dish) => (
          <li
            key={dish.id}
            style={{
              padding: "10px",
              borderBottom: "1px solid #ccc",
              display: "flex",
              justifyContent: "space-between",
            }}
          >
            <span>
              {dish.name} - {dish.calories} cal - ${dish.price}
            </span>
            <div>
              <button
                onClick={() => setEditingDish(dish)}
                style={{ marginRight: "5px", cursor: "pointer" }}
              >
                Edit
              </button>
              <button
                onClick={() => deleteDish(dish.id)}
                style={{ cursor: "pointer", color: "red" }}
              >
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RestaurantMenu;
