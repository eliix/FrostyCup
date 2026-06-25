from enum import Enum


class DrinkTemperature(str, Enum):
    HOT = "hot"
    COLD = "cold"
    BOTH = "both"


class Season(str, Enum):
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"
    WINTER = "winter"


class Mood(str, Enum):
    SOCIAL = "social"
    CELEBRATORY = "celebratory"
    RELAXING = "relaxing"
    ENERGETIC = "energetic"
    FOCUSED = "focused"
    COMFORTING = "comforting"
    ROMANTIC = "romantic"


class Weather(str, Enum):
    SUNNY = "sunny"
    HOT = "hot"
    COLD = "cold"
    RAINY = "rainy"
    SNOWY = "snowy"
    WINDY = "windy"
    CLOUDY = "cloudy"
