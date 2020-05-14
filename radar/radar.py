from tkinter import *
from graphics import * 

from library import library

# Criando a janela
win = GraphWin("Tela Radar", 1000, 800)
win.setBackground("#000")

# Retas
library.Reta(-1000,800, 1000,-800,"#339966",1,win, 2)
library.Reta(1000,800, -1000,-800,"#339966",1,win, 2)
library.Reta(0,800, 0,-800,"#339966",1,win, 2)
library.Reta(1000,0, -1000,0,"#339966",1,win, 2)

# Circulos
# library.Circulo(0, 0, 90, "#339966", 1, win)
# library.Circulo(0, 0, 190, "#339966", 1, win)
# library.Circulo(0, 0, 290, "#339966", 1, win)
# library.Circulo(0, 0, 390, "#339966", 1, win)

# Texto
# library.Texto(-100, 100, "palavra", "#FFF", win)
# library.Texto(-100, -100, "palavra", "#0F0", win)
# library.Texto(100, -100, "palavra", "#F00", win)
# library.Texto(100, 100, "palavra", "#00F", win)

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

