import pandas as pd

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
  

def apuestasMitades(listFrom_DataExtracted, ListadeApuestas):
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
    ListadeApuestas["Over 0.5 1st Half"] = over05_1stHalf

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
    ListadeApuestas["Under 1.5 1st Half"] = under15_1stHalf

    #Unpack list for 2nd half
    hometeam_2ndHalf = listFrom_DataExtracted[1] #count_hometeam_2ndHalf
    awayteam_2ndHalf = listFrom_DataExtracted[4] #count_awayteam_2ndHalf

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
    ListadeApuestas["Over 0.5 2nd Half"] = over05_2ndHalf






    



        