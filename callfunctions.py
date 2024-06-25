import pandas as pd

import roughcode

todasApuestas = {}
path = r"C:\Users\MV310485\Documents\Personal\AlgoApuestas\Goles.xlsx"

dataExtracted = roughcode.dataExtraction(path, "Alaves", "Almeria")

roughcode.apuestasMitades(dataExtracted, todasApuestas)
print(todasApuestas)

