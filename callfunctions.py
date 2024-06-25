import pandas as pd
from roughcode import dataExtraction, apuestasMitades

todasApuestas = {}
path = r"C:\Users\MV310485\Documents\Personal\AlgoApuestas\Goles.xlsx"
dataExtracted = dataExtraction(path, "Alaves", "Almeria")

apuestasMitades(dataExtracted, todasApuestas)
print(todasApuestas)


