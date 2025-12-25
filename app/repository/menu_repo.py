from sqlalchemy.orm import Session
from app.models.menu import Dish

def get_menu(db: Session):
    return db.query(Dish).all()

def add_dish(db: Session, dish_data):
    # dish_data is expected to be a Pydantic model
    db_dish = Dish(**dish_data.model_dump())
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish
