from fastapi import APIRouter, HTTPException
from app.schemas.menu import Dish
from app.services.menu_service import MenuService

router = APIRouter()

@router.get("/", response_model=dict)
def get_menu():
    return {"menu": MenuService.get_menu()}

@router.post("/", response_model=dict)
def add_dish(dish: Dish):
    added_dish = MenuService.add_dish(dish)
    return {"status": "Success", "added": added_dish}

@router.get("/{dish_name}", response_model=Dish)
def get_dish(dish_name: str):
    dish = MenuService.get_dish_by_name(dish_name)
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found on our menu")
    return dish
