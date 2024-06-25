import pandas as pd

def dataExtraction(filepath, hometeam_name, awayteam_name):
    ''' Extraer informacion que va a ser utilizada en el resto de funciones '''
    
    df = pd.read_excel(filepath, header = [1,2])
    hometeam = df[f"{hometeam_name.title()}"]
    awayteam = df[f"{awayteam_name.title()}"]
    
    #hometeam goals 1st half in the last five matches
    hometeam_1stHalf = hometeam["1T"]
    hometeam_1stHalf_lastFive = hometeam_1stHalf.iloc[-5:].values.flatten()
    count_hometeam1stHalf = (hometeam_1stHalf > 0).sum()

    #hometeam goals 2nd half in the last five matches
    hometeam_2ndHalf = hometeam["2T"]
    hometeam_2ndHalf_lastFive = hometeam_2ndHalf.iloc[-5:].values.flatten()
    count_hometeam2ndHalf = (hometeam_2ndHalf > 0).sum()

    #hometeam total goals in the last five matches
    hometeam_TotalGoals = count_hometeam1stHalf + count_hometeam2ndHalf

    #awayteam goals 1st half in the last five matches
    awayteam_1stHalf = awayteam["1T"]
    awayteam_1stHalf_lastFive = awayteam_1stHalf.iloc[-5:].values.flatten()
    count_awayteam1stHalf = (awayteam_1stHalf > 0).sum()

    #awayteam goals 1st half in the last five matches
    awayteam_2ndHalf = awayteam["2T"]
    awayteam_2ndHalf_lastFive = awayteam_2ndHalf.iloc[-5:].values.flatten()
    count_awayteam2ndHalf = (awayteam_2ndHalf > 0).sum()

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

    hometeam_1stHalf_lastFive = listFrom_DataExtracted[0] #count_hometeam1stHalf
    awayteam_1stHalf_lastFive = listFrom_DataExtracted[3] #count_awayteam1stHalf

    #hometeam
    if hometeam_1stHalf_lastFive >= 2:
        over05_1stHalf += 0.5 
    elif hometeam_1stHalf_lastFive >= 3:
        over05_1stHalf += 1
    elif hometeam_1stHalf_lastFive >= 4:
        over05_1stHalf += 1.5

    #awayteam
    if awayteam_1stHalf_lastFive >= 2:
        over05_1stHalf += 0.5 
    elif awayteam_1stHalf_lastFive >= 3:
        over05_1stHalf += 1
    elif awayteam_1stHalf_lastFive >= 4:
        over05_1stHalf += 1.5
        
    ListadeApuestas["Over 0.5 1st half"]= over05_1stHalf




    



        