import classes.data_handler as dh
import betfunctions as fx


path = r"/workspace/LaLigaAutoBetting/Goles.xlsx"
data = dh.DataHandler(path)

matchpairs = data.extract_enfrentamientos()
apuestas_jornada = fx.bets_jornada(path, matchpairs)
apuestas_finales = fx.find_better_bet(apuestas_jornada)
combinadas_sin_cuota = fx.random_pairing(apuestas_finales)
combinadas_con_cuota = fx.calculate_combinadas(combinadas_sin_cuota)

print(combinadas_con_cuota)