import pandas as pd

import funciones as fx

path = r"/workspace/LaLigaAutoBetting/Goles.xlsx"
betsJornada = []
betsMatches = {}
pairs = []

fx.extraerEquipos(path, pairs)
print(pairs)
fx.apuestasJornada(path, pairs, betsJornada)
