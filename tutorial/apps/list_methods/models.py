from django.db import models
from .utils import start_game
# Create your models here.

# fruits = [
#     {"name": "Ford", "weight": "1200", "color": "red"},
#     {"name": "Nissan", "weight": "1300", "color": "yellow"},
#     {"name": "Toyota", "weight": "1400", "color": "blue"},
#     {"name": "Nissan", "weight": "1500", "color": "black"},
#     {"name": "BMW", "weight": "1600", "color": "white"}
# ]
players = ["John", "Deo", "Genre", "David", "Raina"]
scores = [100, 15, 17, 28, 43]
game = {"players": players, "scores": scores}
start_game(game)



