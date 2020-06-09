from graphics import * 
import pandas as pd
import time

# Importando minha propria biblioteca (biblioteca.py)
from biblioteca import biblioteca

planilha = pd.read_csv("data/planilha_radar.csv", usecols = ['T','Status','Voo','X','Y','Z'])

# Desenhado o fundo do radar
radar = biblioteca.Tela_de_Fundo()

ct = 0
avioes = []
for index, row in planilha.iterrows():

    if ct <= 5:
        # Projetar avioes
        calculo = biblioteca.Projetar(row['X'], row['Y'], row['Z'], 200, 12000, radar)
        avioes.append(biblioteca.Aviao(calculo['x'], calculo['y'], row['Status'], row['Voo'], radar))

    else:
        ct = 0
        # Limpar avioes
        time.sleep(3)
        biblioteca.Limpar_Avioes(avioes)

    ct += 1
            


