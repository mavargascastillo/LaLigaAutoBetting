'''
This file is an attempt to organize the functions of the betting strategy into separate classes. This is so the code is
more modular and easier to maintain. The idea is to have the function divided by data handlers and betting strategies
'''

import pandas as pd
import copy
import random

class DataHandler:
    ''' Attempt at grouping all functions that extract data from the Excel DataFrame'''

    def __init__ (self, filepath):
        self.filepath = filepath
    
    def extract_team_goals(self, team_df, last_n = 5):
        '''
        Extracts the goals scored by a team in the first and second halves in the last `last_n` matches.
        
        Args:
            team_df (DataFrame): DataFrame containing the team's goals data.
            last_n (int): Number of recent matches to consider.
            
        Returns:
            tuple: Count of goals in the first half, second half, and total goals.
        '''
        first_half_goals = team_df["1T"].iloc[-last_n:].values.flatten()
        second_half_goals = team_df["2T"].iloc[-last_n:].values.flatten()
        
        count_first_half = (first_half_goals > 0).sum()
        count_second_half = (second_half_goals > 0).sum()
        total_goals = count_first_half + count_second_half
        
        return count_first_half, count_second_half, total_goals

    def data_extraction(self, hometeam_name, awayteam_name):
        """
        Extracts goals information for the home and away teams from the given Excel file.
        
        Args:
            hometeam_name (str): Name of the home team.
            awayteam_name (str): Name of the away team.
            
        Returns:
            list: Contains counts of home and away team goals in the first and second halves and total goals.
        """
        # Load the Excel file
        df = pd.read_excel(self.filepath, header=[1, 2])
        
        # Extract data for the home and away teams
        hometeam_df = df[hometeam_name.title()]
        awayteam_df = df[awayteam_name.title()]
        
        # Extract goals information for both teams
        hometeam_goals = self.extract_team_goals(hometeam_df)
        awayteam_goals = self.extract_team_goals(awayteam_df)
        
        # Combine the results into a single list
        result = list(hometeam_goals) + list(awayteam_goals)
        
        return result

    def extract_enfrentamientos(self):
        ''' 
        Crear una lista con los pares de equipos de cada partido 

        Returns:
            list: a list of pairs, where each pair contains the teams playing against each other
        '''

        pares_partidos = []
        try:
            team_pairs = pd.read_excel(self.filepath, sheet_name="calendario", header=[0, 1], index_col=0)
        except Exception as e:
            raise ValueError(f"Error loading Excel sheet: {e}")

        num_cols = len(team_pairs.columns)
        
        for col in range(0, num_cols, 2):
            team1 = team_pairs.iloc[0, col]
            team2 = team_pairs.iloc[0, col+1]
            pares_partidos.append((team1, team2))
        
        return pares_partidos
    

class Bets:
    ''' Agrupar todas las funciones que procesan apuestas'''

    def __init__ (self, goals_data, pares_partidos):
        self.goals_data = goals_data
        self.pares_partidos = pares_partidos

    def bets_mitades(self, list_from_data_extracted):
        ''' 
        Asigna un valor a las tres apuestas de mitades según los datos extraídos del DataFrame de Excel
        
        Args:
            list_from_data_extracted (list): list of extracted data containing goal counts

        Returns:
            apuestas_partido (dict): A dictionary with the calculated bet weights
        '''

        apuestas_partido = {}
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

    def bets_jornada(self, pares_partidos):
        ''' 
        Loop over the team pairs and apply the functions data_extraction & bets_mitades. It also appends all of
        the bets to a list

        Args:    
            paresPartidos = type(list) ; list of pairs ; teams that play against each other

        Returns:
            apuestasPartido (dict): prints the dictionaries with the bets of every matcg
            apuestas_jornada (list): list containing the dictionaries of every match    
        '''

        apuestas_jornada = []

        for team1, team2 in pares_partidos:
            TeamsData = data_extraction(filepath, team1, team2)
            matchname = f"{team1} VS {team2}"
            #Crear nuevo diccionario para cada partido
            apuestasPartido = {"Match" : matchname} 
            #completar el diccionario de apuestas de un partido individual
            self.bets_mitades(TeamsData, apuestasPartido)
            apuestas_jornada.append(apuestasPartido)
            print(f'Processed data para el partido entre {team1} y {team2}: ')
            print(apuestasPartido)
            print('-----------------------------')

        return apuestas_jornada  