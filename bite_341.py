from pydantic import BaseModel, PositiveInt
from fastapi import FastAPI, HTTPException
from typing import Any
import tracemalloc
#from main import app
from datetime import datetime

EXPECTED_FOOD1 = {
    "id": 1,
    "name": "egg",
    "serving_size": "piece",
    "kcal_per_serving": 78,
    "protein_grams": 6.2,
    "fibre_grams": 0,
}
EXPECTED_FOOD2 = {
    "id": 2,
    "name": "oatmeal",
    "serving_size": "100 grams",
    "kcal_per_serving": 336,
    "protein_grams": 13.2,
    "fibre_grams": 10.1,
}

class Food (BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float

class User(BaseModel):
    id: int
    username: str
    password: str

class FoodEntry(BaseModel):
    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float

    @property
    def total_calories(self):
        return self.number_servings * self.food.kcal_per_serving
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.password = get_password_hash(data['password'])

app = FastAPI()
foods: dict [int, Food] = {}

@app.post("/")
async def create_food(food:Food):
    foods[food.id] = food
    return food
print(create_food(EXPECTED_FOOD1))

@app.get('/', response_model=list[Food])
async def get_root():
    return foods.values()
print(get_root())


@app.get('/{item}')
async def get_item(item:int):
    return(foods[item])
print(get_item(2))
print(get_item(1))

#Create the update and delete endpoints here

@app.put('/{food_id}')
async def update_food(food_id:int, food:Food):
    if food_id not in foods:
        raise HTTPException(status_code=404, detail='Food not found')
    foods[food_id] = food
    return food

@app.delete('/{food_id}')
async def delete_food(food_id:int):
    if food_id not in foods:
        raise HTTPException(status_code=404, detail='Food not found')
    del foods[food_id]
    return {'OK': True}



'''external_data = {
    'id': 123,
    'name': 'banana',
    'serving_size': '1 banana',
    'kcal_per_serving' : 90,
    'protein_grams' : 1.3,
    'fibre_grams': 3.1,
}

food = Food(**external_data)

print(food.id)
#> 123
print(food.model_dump())'''
