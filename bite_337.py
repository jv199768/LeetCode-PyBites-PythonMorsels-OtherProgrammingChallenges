from pydantic import BaseModel, PositiveInt


class Food (BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float


external_data = {
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
print(food.model_dump())
