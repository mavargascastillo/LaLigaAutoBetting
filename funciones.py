import pandas as pd
import copy
import random


def dataExtraction(filepath, hometeam_name, awayteam_name):
    ''' Extraer informacion que va a ser utilizada en el resto de funciones '''
    
    df = pd.read_excel(filepath, header = [1,2])
    hometeam = df[f"{hometeam_name.title()}"]
    awayteam = df[f"{awayteam_name.title()}"]
    
    #hometeam goals 1st half in the last five matches
    hometeam_1stHalf = hometeam["1T"]
    hometeam_1stHalf_lastFive = hometeam_1stHalf.iloc[-5:].values.flatten()
    count_hometeam1stHalf = (hometeam_1stHalf_lastFive > 0).sum()

    #hometeam goals 2nd half in the last five matches
    hometeam_2ndHalf = hometeam["2T"]
    hometeam_2ndHalf_lastFive = hometeam_2ndHalf.iloc[-5:].values.flatten()
    count_hometeam2ndHalf = (hometeam_2ndHalf_lastFive > 0).sum()

    #hometeam total goals in the last five matches
    hometeam_TotalGoals = count_hometeam1stHalf + count_hometeam2ndHalf

    #awayteam goals 1st half in the last five matches
    awayteam_1stHalf = awayteam["1T"]
    awayteam_1stHalf_lastFive = awayteam_1stHalf.iloc[-5:].values.flatten()
    count_awayteam1stHalf = (awayteam_1stHalf_lastFive > 0).sum()

    #awayteam goals 1st half in the last five matches
    awayteam_2ndHalf = awayteam["2T"]
    awayteam_2ndHalf_lastFive = awayteam_2ndHalf.iloc[-5:].values.flatten()
    count_awayteam2ndHalf = (awayteam_2ndHalf_lastFive > 0).sum()

    #awayteam total goals in the last five matches
    awayteam_TotalGoals = count_awayteam1stHalf + count_awayteam2ndHalf

    return [
        count_hometeam1stHalf,
        count_hometeam2ndHalf,
        hometeam_TotalGoals,
        count_awayteam1stHalf,
        count_awayteam2ndHalf,
        awayteam_TotalGoals
    ]
  


def apuestasMitades(listFrom_DataExtracted, apuestasPartido):
    ''' Asigna un valor a las tres apuestas de mitades según los datos extraídos del DataSet de excel'''

    over05_1stHalf = 0
    under15_1stHalf = 0
    over05_2ndHalf = 0

    # Unpack the list for 1st half
    hometeam_1stHalf = listFrom_DataExtracted[0] #count_hometeam_1stHalf
    awayteam_1stHalf = listFrom_DataExtracted[3] #count_awayteam_1stHalf

    # Function to determine the score increment for the 1st half
    def calculate_increment_over05_1stHalf(count):
        if count >= 4:
            return 1.5
        elif count >= 3:
            return 1
        elif count >= 2:
            return 0.5
        else:
            return 0

    # Calculate increments for hometeam and awayteam
    over05_1stHalf += calculate_increment_over05_1stHalf(hometeam_1stHalf)
    over05_1stHalf += calculate_increment_over05_1stHalf(awayteam_1stHalf)
    apuestasPartido["Over 0.5 1st Half"] = over05_1stHalf

    def calculate_increment_under15_1stHalf(count):
        if count == 2:
            return 0.5
        elif count == 1:
            return 1
        elif count == 0:
            return 1.5
        else:
            return 0
    
    under15_1stHalf += calculate_increment_under15_1stHalf(hometeam_1stHalf)
    under15_1stHalf += calculate_increment_under15_1stHalf(awayteam_1stHalf)
    apuestasPartido["Under 1.5 1st Half"] = under15_1stHalf

    #Unpack list for 2nd half
    hometeam_2ndHalf = listFrom_DataExtracted[1] #count_hometeam_2ndHalf
    awayteam_2ndHalf = listFrom_DataExtracted[4] #count_awayteam_2ndHalfapues

    def calculate_increment_over05_2ndHalf(count):
        if count >= 4:
            return 1.5
        elif count >= 3:
            return 1
        elif count >= 2:
            return 0.5
        else:
            return 0
    
    over05_2ndHalf += calculate_increment_over05_2ndHalf(hometeam_2ndHalf)
    over05_2ndHalf += calculate_increment_over05_2ndHalf(awayteam_2ndHalf)
    apuestasPartido["Over 0.5 2nd Half"] = over05_2ndHalf



def extraerEquipos(filepath, paresPartidos):
    ''' Crear una lista con los pares de equipos de cada partido '''

    teamPairs = pd.read_excel(filepath, sheet_name = "calendario", header = [0,1], index_col = 0)
    for col in range(0, len(teamPairs.columns), 2):
        team1 = teamPairs.iloc[0, col]
        team2 = teamPairs.iloc[0, col+1]
        paresPartidos.append((team1, team2)) 



def apuestasJornada(filepath, paresPartidos, jornada):
    ''' Loop over the team pairs and apply the functions dataExtraction & apuestasMitades. It also appends all of
    the bets to a list
    paresPartidos = type(list) ; list of pairs ; teams that play against each other
    apuestasPartido = type(dictionary) ; will be filled with the three bets for each match
    jornada = type(list) ; will be filled with each apuestasPartido
    '''

    for team1, team2 in paresPartidos:
        TeamsData = dataExtraction(filepath, team1, team2)
        matchname = f"{team1} VS {team2}"
        #Crear nuevo diccionario para cada partido
        apuestasPartido = {"Match" : matchname} 
        #completar el diccionario de apuestas de un partido individual
        apuestasMitades(TeamsData, apuestasPartido)
        jornada.append(apuestasPartido)
        print(f'Processed data para el partido entre {team1} y {team2}: ')
        print(apuestasPartido)
        print('-----------------------------')  



def find_better_bet(dictBetsMatches, copiaDictBetsMatches, n=1):
    ''' Finds the highest ranked bet of a match and its corresponding quote and creates a dictionary with them'''

    apuestaSimple = {}
    better_bet = max(copiaDictBetsMatches, key=copiaDictBetsMatches.get)
    quoteApuesta = 1.37 #falta construir dataset de quotes y programar la recogida de informacion
    apuestaSimple[f"Match {n}"] = dictBetsMatches["Match"]
    apuestaSimple["Apuesta"] = better_bet
    apuestaSimple["Cuota"] = quoteApuesta
    return apuestaSimple

def random_pairing(list_of_dictionaries):
    '''This function randomly pairs dictionaries in a list.'''
    
    # Ensure the list has an even number of elements
    if len(list_of_dictionaries) % 2 != 0:
        raise ValueError("The list must contain an even number of dictionaries.")
    
    # Shuffle the list to ensure random pairing
    random.shuffle(list_of_dictionaries)
    
    # Create pairs from the shuffled list
    paired_list = []
    for i in range(0, len(list_of_dictionaries), 2):
        pair = (list_of_dictionaries[i], list_of_dictionaries[i + 1])
        paired_list.append(pair)
    
    return paired_list

def calculate_combinadas(paired_list):
    '''This function calculates combined odds for pairs of dictionaries.'''
    
    combinadas = []
    for pair in paired_list:
        dict1, dict2 = pair
        
        # Extract odds values (assuming 'Cuota' key exists in both dictionaries)
        value1 = dict1['Cuota']
        value2 = dict2['Cuota']
        
        # Calculate combinada odds
        cuota_combinada = value1 * value2
        
        # Create combinada
        combinada = (
            dict1,
            dict2,
            {'Cuota Combinada': cuota_combinada}
        )
        
        combinadas.append(combinada)
    
    return combinadas

