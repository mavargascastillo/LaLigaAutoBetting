import pandas as pd
import funciones as fx

apuestaPartido = {
    'Match': 'sevilla VS valencia',
    'Over 0.5 1st Half': 1,
    'Under 1.5 1st Half': 1,
    'Over 0.5 2nd Half': 0.5
    }

apuestaPartido2 = {
    'Match': 'barca VS madrid',
    'Over 0.5 1st Half': 2,
    'Under 1.5 1st Half': 3,
    'Over 0.5 2nd Half': 4
    }

lista = [apuestaPartido, apuestaPartido2]

prueba = fx.process_bets(lista)
print(prueba)