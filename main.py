from fastapi import FastAPI
from pydantic import BaseModel

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