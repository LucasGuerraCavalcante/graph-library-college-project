from graphics import * 

# Importando minha propria biblioteca (biblioteca.py)
from biblioteca import biblioteca

# Desenhado o fundo do radar
fundo_radar = biblioteca.Tela_de_Fundo()

# Inicializando o radar
radar = fundo_radar

# Projetar
biblioteca.Projetar(1000, 2000, 3000, 100, 5000, radar)

radar.close()

fundo_radar = biblioteca.Tela_de_Fundo()
radar = fundo_radar

biblioteca.Projetar(5000, 100, 3000, 2000, 1000, radar)

radar.getMouse()
radar.close()


