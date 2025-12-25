from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.menu import Dish, MenuList, DishResponse
from app.services.menu_service import MenuService
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=MenuList)
def get_menu(db: Session = Depends(get_db)):
    menu_items = MenuService.get_menu(db)
    # FastAPI will convert the list of SQLAlchemy objects to MenuList -> List[Dish]
    return {"menu": menu_items}

@router.post("/", response_model=DishResponse)
def add_dish(dish: Dish, db: Session = Depends(get_db)):
    added_dish = MenuService.add_dish(db, dish)
    return {"status": "Success", "added": added_dish}

@router.get("/{dish_name}", response_model=Dish)
def get_dish(dish_name: str, db: Session = Depends(get_db)):
    dish = MenuService.get_dish_by_name(db, dish_name)
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found on our menu")
    return dish
