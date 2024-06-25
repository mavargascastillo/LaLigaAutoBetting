apuestasPartido = {'Over 0.5 1st Half': 2.0, 'Under 1.5 1st Half': 0.5, 'Over 0.5 2nd Half': 1.5}

apuestaCombinada = {}
better_bet = max(apuestasPartido, key=apuestasPartido.get)
quoteApuesta = 1.37 #falta construir dataset de quotes y programar la recogida de informacion
apuestaCombinada[better_bet] = quoteApuesta
print(apuestaCombinada)
