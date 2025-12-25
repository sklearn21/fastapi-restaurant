from pydantic import BaseModel

class Dish(BaseModel):
    name: str
    price: float
    category: str = "Main Course"
