import pandas as pd

import funciones as fx

path = r"C:\Users\MV310485\Documents\Personal\AlgoApuestas\Goles.xlsx"
betsJornada = []
betsMatches = {}
pairs = []

fx.extraerEquipos(path, pairs)
fx.apuestasJornada(path, pairs, betsMatches, betsJornada)