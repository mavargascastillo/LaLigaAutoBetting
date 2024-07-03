'''
Funciones que corresponderian a la clase de Bets
'''
import classes.data_handler as dh

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
