from pydantic import BaseModel, Field
from bson import ObjectId


## campos: name, description, category, alcoholic, temperature, ingredients, origin, season, moods, weather, create_at
class Drink(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    description: str
    category: str
    alcoholic: bool
    temperature: str
    ingredients: str
    origin: str
    season: str
    moods: str
    weather: str
    create_at: str

    model_config = {
        "arbitrary_types_allowed": True,
        "populate_by_name": True,
    }  ## config para que me deje usar objectId
