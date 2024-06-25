import pandas as pd

import funciones

todasApuestas = {}
path = r"C:\Users\MV310485\Documents\Personal\AlgoApuestas\Goles.xlsx"

dataExtracted = funciones.dataExtraction(path, "Alaves", "Almeria")

funciones.apuestasMitades(dataExtracted, todasApuestas)
print(todasApuestas)

