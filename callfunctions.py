import pandas as pd
import copy

import funciones as fx

path = r"/workspace/LaLigaAutoBetting/Goles.xlsx"
betsJornada = []
betsMatches = {}
pairs = []

fx.extraerEquipos(path, pairs)
print(pairs)
fx.apuestasJornada(path, pairs, betsJornada)
apuestasSimples = fx.process_bets(betsJornada)
apuestasSimplesAgrupadas = fx.group_random_pairs(apuestasSimples)
print(apuestasSimplesAgrupadas)
