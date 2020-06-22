import pandas as pd
import numpy as np
from data_cleaning import *

def games(game):
    datos= extraerdatos()
    game_1= datos[(datos["Name"] == f'{game}')]
    
    return game_1



