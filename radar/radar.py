from graphics import * 

# Importando minha propria biblioteca (biblioteca.py)
from biblioteca import biblioteca

# Desenhado o fundo do radar
fundo_radar = biblioteca.Tela_de_Fundo()

# Inicializando o radar
radar = fundo_radar

# Projetar
items = biblioteca.Projetar(1000, 2000, 3000, 100, 5000, radar)
biblioteca.Aviao(items['x'], items['y'], 'D', "LA 2203", radar)

# radar.close()

# fundo_radar = biblioteca.Tela_de_Fundo()
# radar = fundo_radar

radar.getMouse()
radar.close()


