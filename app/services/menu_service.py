from typing import List, Optional
from app.schemas.menu import Dish

# In-memory database
menu_db: List[Dish] = []

class MenuService:
    @staticmethod
    def get_menu() -> List[Dish]:
        return menu_db

    @staticmethod
    def add_dish(dish: Dish) -> Dish:
        menu_db.append(dish)
        return dish

    @staticmethod
    def get_dish_by_name(name: str) -> Optional[Dish]:
        for dish in menu_db:
            if dish.name.lower() == name.lower():
                return dish
        return None
