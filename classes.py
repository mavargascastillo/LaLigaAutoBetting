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
    
