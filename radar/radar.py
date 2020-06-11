from graphics import * 
import pandas as pd
import time

# Importando minha propria biblioteca (biblioteca.py)
from biblioteca import biblioteca

# Lendo e salvando a planilha
planilha = pd.read_csv("data/planilha_radar.csv", usecols = ['T','Status','Voo','X','Y','Z'])

# Desenhado o fundo do radar
radar = biblioteca.Tela_de_Fundo()

ct = 0
avioes = []
# Percorrendo as linhas da planilha
for index, row in planilha.iterrows():

    # Desenhando os 5 avioes, apos desenhar os 5, o contador zera, apaga os avioes
    # e desenha os mesmos 5 avioes na proxima posicao
    if ct < 5:
        # Calculos do aviao
        calculo = biblioteca.Projetar(row['X'], row['Y'], row['Z'], 1000, 62000, radar)
        angulo = biblioteca.Direcao(calculo['x'], calculo['y'])

        # Projetar aviao
        aviao = biblioteca.Aviao(calculo['x'], calculo['y'], angulo, row['Status'], row['Voo'], radar)
        avioes.append(aviao)

        ct += 1

    else:
        ct = 0
        # Limpar avioes
        time.sleep(3)
        biblioteca.Limpar_Avioes(avioes)


            


