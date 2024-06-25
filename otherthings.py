mas05_2aMitad = 0
    1er equipo
        ultimos5partidos: goles 2a parte
        if >= 2/5:
            +0.5 a mas05_2a_parte
        elif >= 3/5:
            +1 a mas05_2a_parte
        elif >= 4/5:
            +1.5 a mas05_2a_parte
        else:
            break
    2o equipo
    ultimos5partidos: goles 2a parte
    if >= 2/5:
        +0.5 a mas05_2a_parte
    elif >= 3/5:
        +1 a mas05_2a_parte
    elif >= 4/5:
        +1.5 a mas05_2a_parte
    else:
        break
todasApuestas.append(mas05_2aMitad)
menos15_1aMitad = 0
    if (goles1aMitad1erEquipo + goles1aMitad2oEquipo) <= 1/5:
        + 1.5 a menos15_1aMitad 
    elif (goles1aMitad1erEquipo + goles1aMitad2oEquipo) <= 2/5:
        + 1 a menos15_1aMitad
    elif (goles1aMitad1erEquipo + goles1aMitad2oEquipo) <= 3/5:
        + 0.5 a menos15_1aMitad
    else:
        break
todasApuestas.append(menos_1aMitad)        

def golesPartido(self):
    mas15_Partido = 0
        if (1erEquipo_TotalGoles + 2oEquipo_TotalGoles) >= 2:
            +1 a mas15_Partido
        elif (1erEquipo_TotalGoles + 2oEquipo_TotalGoles) >= 9/5:
            + 0.5 a mas15_Partido
    todasApuestas.append(mas15_Partido)
    mas25_Partido = 0
        if 
    todasApuestas.append(mas25_Partido)

def listResults(self, todasApuestas):
    for apuesta in todasApuestas:
    print(f"{variablename}: {variablevalue}")

golesEquipos = dataExtraction(path, "Alaves", "Almeria")