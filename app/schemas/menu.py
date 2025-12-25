from typing import List
from pydantic import BaseModel

class Dish(BaseModel):
    name: str
    price: float
    category: str = "Main Course"
    # id might be useful to return now that we have DB
    id: int | None = None

    class Config:
        from_attributes = True

class MenuList(BaseModel):
    menu: List[Dish]

class DishResponse(BaseModel):
    status: str
    added: Dish
