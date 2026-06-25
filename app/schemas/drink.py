from pydantic import BaseModel, Field
from enum import Enum
from app.schemas.enums import DrinkTemperature, Season, Weather, Mood
from datetime import datetime


class DrinkCategory(str, Enum):
    COCKTAIL = "cocktail"
    BEER = "beer"
    WINE = "wine"
    SPIRITS = "spirits"
    LIQUEUR = "liqueur"

    # Coffee based
    COFFEE = "coffee"

    # Tea based
    TEA = "tea"

    # Chocolate based
    HOT_CHOCOLATE = "hot_chocolate"

    # Juice & fruit
    JUICE = "juice"
    SMOOTHIE = "smoothie"
    MILKSHAKE = "milkshake"

    # Soft drinks
    SOFT_DRINK = "soft_drink"
    ENERGY_DRINK = "energy_drink"
    SPORTS_DRINK = "sports_drink"

    # Water
    WATER = "water"
    SPARKLING_WATER = "sparkling_water"

    # Other
    MOCKTAIL = "mocktail"


# campos: name, description, category, alcoholic, temperature, ingredients, origin, season, moods, weather, create_at
class DrinkCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    description: str = Field(
        ..., min_length=10, max_length=500, description="Descripcion de la bebida"
    )
    category: DrinkCategory = Field(..., description="Categoría de la bebida")
    alcoholic: bool = Field(..., description="Indica si la bebida contiene alcohol")
    temperature: DrinkTemperature
    ingredients: list[str] = Field(
        ..., min_length=1, description="Lista de ingredientes de la bebida"
    )
    origin: str = Field(..., min_length=2, max_length=50)
    season: list[Season]
    moods: list[Mood]
    weather: list[Weather]


## el create_at va en el response
class DrinkResponse(DrinkCreate):  # hereda de drink create asi no repite codigo
    id: str = Field(alias="_id")
    created_at: datetime

    model_config = {"populate_by_name": True}
