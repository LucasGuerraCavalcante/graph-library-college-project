from tkinter import *
from graphics import * 

from library import library

# Criando a janela
win = GraphWin("Tela Testes", 100, 100)
win.setBackground("#00001a")

# Pontos
library.Ponto(-10,0,"red",1,win)
library.Ponto(0,0,"green",2,win)
library.Ponto(10,0,"yellow",3,win)
library.Ponto(20,0,"blue",4,win)

"""
# Retas
library.Reta(-1000,800, 1000,-800,"#339966",1,win, 2)
library.Reta(1000,800, -1000,-800,"#339966",1,win, 2)
library.Reta(0,800, 0,-800,"#339966",1,win, 2)
library.Reta(1000,0, -1000,0,"#339966",1,win, 2)

# Circulos
library.Circulo(0, 0, 90, "#339966", 1, win)
library.Circulo(0, 0, 190, "#339966", 1, win)
library.Circulo(0, 0, 290, "#339966", 1, win)
library.Circulo(0, 0, 390, "#339966", 1, win)

# Marcador central
library.Reta(5,0, 10,0,"#FFF",1,win)
library.Reta(-5,0, -10,0,"#FFF",1,win)
library.Reta(0,5, 0,10,"#FFF",1,win)
library.Reta(0,-5, 0,-10,"#FFF",1,win)
library.Ponto(0,0,"red",4,win)
"""

win.getMouse()
win.close()



