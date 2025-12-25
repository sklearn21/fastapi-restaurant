from typing import List, Optional
from sqlalchemy.orm import Session
from app.schemas.menu import Dish
from app.repository import menu_repo

# We now rely on the repository and DB, so no in-memory list here.

class MenuService:
    @staticmethod
    def get_menu(db: Session) -> List[Dish]:
        # Repo returns SQLAlchemy models, we might want to convert to Pydantic if needed
        # But FastAPI handles ORM mode if configured.
        return menu_repo.get_menu(db)

    @staticmethod
    def add_dish(db: Session, dish: Dish) -> Dish:
        return menu_repo.add_dish(db, dish)

    @staticmethod
    def get_dish_by_name(db: Session, name: str) -> Optional[Dish]:
        # We need to implement this in repo if needed
        # For now, let's just do a simple query here or add to repo
        # The user's code for repo didn't include get_by_name, so I'll add a helper here or directly query
        from app.models.menu import Dish as DishModel
        return db.query(DishModel).filter(DishModel.name == name).first()
