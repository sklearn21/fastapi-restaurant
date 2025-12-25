from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException # Add this to your imports at the top!

app = FastAPI()

# This defines what a 'Dish' looks like
class Dish(BaseModel):
    name: str
    price: float
    category: str = "Main Course"

# Our temporary list to store dishes
menu_db = []

@app.get("/")
def home():
    return {"message": "Welcome to the Bistro API!"}

@app.get("/menu")
def get_menu():
    return {"menu": menu_db}

@app.post("/add-dish")
def add_dish(dish: Dish):
    menu_db.append(dish)
    return {"status": "Success", "added": dish}

@app.get("/menu/{dish_name}")
def get_dish(dish_name: str):
    # Search the list for a dish with a matching name
    for dish in menu_db:
        if dish.name.lower() == dish_name.lower():
            return dish
    
    # If not found, send a 404 Error
    raise HTTPException(status_code=404, detail="Dish not found on our menu")