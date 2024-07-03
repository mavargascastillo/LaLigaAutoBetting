import classes.data_handler as dh
import funciones2 as fx

path = r"/workspace/LaLigaAutoBetting/Goles.xlsx"
data = dh.DataHandler(path)

matchpairs = data.extract_enfrentamientos()
apuestas_jornada = fx.bets_jornada(path, matchpairs)

print(apuestas_jornada)