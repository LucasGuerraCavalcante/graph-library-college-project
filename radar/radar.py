from tkinter import *
from graphics import * 

# Importando minha propria biblioteca (biblioteca.py)
from biblioteca import biblioteca

# Criando a janela
win = GraphWin("Tela Radar", 1000, 800)
win.setBackground("#000")

# Retas
biblioteca.Reta(-1000,800, 1000,-800,"#339966",1,win, 2)
biblioteca.Reta(1000,800, -1000,-800,"#339966",1,win, 2)
biblioteca.Reta(0,800, 0,-800,"#339966",1,win, 2)
biblioteca.Reta(1000,0, -1000,0,"#339966",1,win, 2)

# Circulos
biblioteca.Circulo(0, 0, 90, "#339966", 1, win)
biblioteca.Circulo(0, 0, 190, "#339966", 1, win)
biblioteca.Circulo(0, 0, 290, "#339966", 1, win)
biblioteca.Circulo(0, 0, 390, "#339966", 1, win)

# Texto
biblioteca.Texto(-100, 100, "palavra", "#FFF", 10, 'bold', win)
biblioteca.Texto(-100, -100, "palavra", "#0F0", 10, 'bold', win)
biblioteca.Texto(100, -100, "palavra", "#F00", 10, 'bold', win)
biblioteca.Texto(100, 100, "palavra", "#00F", 10, 'bold', win)

# Marcador central
# library.Reta(5,0, 10,0,"#FFF",1,win)
# library.Reta(-5,0, -10,0,"#FFF",1,win)
# library.Reta(0,5, 0,10,"#FFF",1,win)
# library.Reta(0,-5, 0,-10,"#FFF",1,win)
# library.Ponto(0,0,"red",4,win)

# Aviao
# library.Aviao(10, 0, True, 0, win)
# library.Aviao(10, 50, True, 30, win)
# library.Aviao(10, 100, True, 90, win)
# library.Aviao(10, 150, True, 150, win)
# library.Aviao(10, 200, True, 180, win)
# library.Aviao(10, 250, True, 210, win)
# library.Aviao(10, 300, True, 270, win)
# library.Aviao(10, 350, True, 330, win)

# library.Aviao(-10, 0, False, 0, win)
# library.Aviao(-10, 50, False, 30, win)
# library.Aviao(-10, 100, False, 90, win)
# library.Aviao(-10, 150, False, 150, win)
# library.Aviao(-10, 200, False, 180, win)
# library.Aviao(-10, 250, False, 210, win)
# library.Aviao(-10, 300, False, 270, win)
# library.Aviao(-10, 350, False, 330, win)


win.getMouse()
win.close()

