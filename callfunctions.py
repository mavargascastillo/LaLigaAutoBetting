from roughcode import dataExtraction, apuestasMitades
import pandas as pd

todasApuestas = []
path = r"C:\Users\MV310485\Documents\Personal\AlgoApuestas\Goles.xlsx"
dataExtracted = dataExtraction(path, "Alaves", "Almeria")

apuestasMitades(dataExtracted, todasApuestas)
print(todasApuestas)


