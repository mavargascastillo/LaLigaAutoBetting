'''
Module that contains functions to create the bets from the data extracted using the DataHandler class
'''
import classes.data_handler as dh
import copy
import random

def bets_mitades(list_from_data_extracted, matchname):
    ''' 
    Asigna un valor a las tres apuestas de mitades según los datos extraídos del DataFrame de Excel
    
    Args:
        list_from_data_extracted (list): list of extracted data containing goal counts

    Returns:
        apuestas_partido (dict): A dictionary with the calculated bet weights
    '''

    apuestas_partido = {"Match" : matchname}
    over05_1stHalf = 0
    under15_1stHalf = 0
    over05_2ndHalf = 0

    # Unpack the list for 1st half
    hometeam_1stHalf = list_from_data_extracted[0] #count_hometeam_1stHalf
    awayteam_1stHalf = list_from_data_extracted[3] #count_awayteam_1stHalf

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
    apuestas_partido["Over 0.5 1st Half"] = over05_1stHalf

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
    apuestas_partido["Under 1.5 1st Half"] = under15_1stHalf

    #Unpack list for 2nd half
    hometeam_2ndHalf = list_from_data_extracted[1] #count_hometeam_2ndHalf
    awayteam_2ndHalf = list_from_data_extracted[4] #count_awayteam_2ndHalf

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
    apuestas_partido["Over 0.5 2nd Half"] = over05_2ndHalf

    return apuestas_partido

def bets_jornada(filepath, pares_partidos):
    ''' 
    Loop over the team pairs and apply the functions data_extraction & bets_mitades. It also appends all of
    the bets to a list

    Args:    
        paresPartidos = type(list) ; list of pairs ; teams that play against each other

    Returns:
        [prints] apuestas_partido (dict): prints the dictionaries with the bets of every matcg
        apuestas_jornada (list): list containing the dictionaries of every match    
    '''

    apuestas_jornada = []
    data = dh.DataHandler(filepath)

    for team1, team2 in pares_partidos:
        teams_data = data.data_extraction(team1, team2)
        match = f"{team1} VS {team2}" 
        apuestas_partido = bets_mitades(teams_data, matchname = match)
        apuestas_jornada.append(apuestas_partido)
        print(f'Processed data para el partido entre {team1} y {team2}: ')
        print(apuestas_partido)
        print('-----------------------------')

    return apuestas_jornada  

def find_better_bet(apuestas_jornada, n=1):
    ''' 
    Finds the highest ranked bet of a match and its corresponding quote and creates a dictionary with them.
    
    Args:
        apuestas_jornada (list): list containing the dictionaries with the three possible bets per match
        n (int): sole purpose is to enumerate the matches when creating the new dictionaries

    Returns:
        apuestas_finales_jornada (list): list containing the dictionaries with the final bets per match
    '''

    apuestasfinales_jornada = []

    for dict in apuestas_jornada:
        apuesta_simple = {}
        # Crear copia profunda para no alterar los diccionarios originales
        copia_apuestas_jornada = copy.deepcopy(dict)
        # Delete Match key to be able to execute next step: select the bet with the highest count
        del copia_apuestas_jornada["Match"]

        better_bet = max(copia_apuestas_jornada, key=copia_apuestas_jornada.get)
        cuota_apuesta = 1.37 #falta construir dataset de quotes y programar la recogida de informacion
        # Add again Match key
        apuesta_simple[f"Match {n}"] = dict["Match"]
        apuesta_simple["Apuesta"] = better_bet
        apuesta_simple["Cuota"] = cuota_apuesta
        # Add final bet from individual match to list containing all individuals bets of that jornada
        apuestasfinales_jornada.append(apuesta_simple)
    
    return apuestasfinales_jornada

def random_pairing(list_of_dictionaries):
    '''
    This function randomly pairs dictionaries in a list.

    Args:
        list_of_dictionaries (list): apuestasfinales_jornada
        
    Returns:
        paired_list (list): paired list of dictionaries
    '''
    
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