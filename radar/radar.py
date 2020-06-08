from graphics import * 

# Importando minha propria biblioteca (biblioteca.py)
from biblioteca import biblioteca

# Desenhado o fundo do radar
radar = biblioteca.Tela_de_Fundo()

# Inicializando o radar
fundo_radar = radar.items

# Projetar
items = biblioteca.Projetar(1000, 2000, 3000, 100, 5000, radar)
av1 = biblioteca.Aviao(items['x'], items['y'], 'D', "TESTE", radar)

items = biblioteca.Projetar(-12990, 7500, 7500, 120, 15000, radar)
av2 = biblioteca.Aviao(items['x'], items['y'], 'P', "LA 2203", radar)

items = biblioteca.Projetar(-3473, 19696, 10000, 150, 20000, radar)
av3 = biblioteca.Aviao(items['x'], items['y'], 'P', "GZ 0331", radar)

items = biblioteca.Projetar(-9397, -3420.2, 5000, 100, 10000, radar)
av4 = biblioteca.Aviao(items['x'], items['y'], 'P', "AZ 0032", radar)

avioes = [av1, av2, av3, av4]

radar.getMouse()
biblioteca.Limpar_Avioes(avioes)

items = biblioteca.Projetar(1000, 2000, 3000, 100, 5000, radar)
av1 = biblioteca.Aviao(items['x'], items['y'], 'D', "TESTE", radar)

items = biblioteca.Projetar(-11951, 6900, 6900, 120, 13800, radar)
av2 = biblioteca.Aviao(items['x'], items['y'], 'P', "LA 2203", radar)

items = biblioteca.Projetar(-3212, 18219, 9250, 150, 18500, radar)
av3 = biblioteca.Aviao(items['x'], items['y'], 'P', "GZ 0331", radar)

items = biblioteca.Projetar(-8457, -3078.18, 4500, 100, 9000, radar)
av4 = biblioteca.Aviao(items['x'], items['y'], 'P', "AZ 0032", radar)

avioes = [av1, av2, av3, av4]

radar.getMouse()
radar.close()


