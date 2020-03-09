from tkinter import *
from graphics import *

# def ponto(valorx, valory, cor, primitiva):

# rodar o sistema de coordenadas

# desenhar o ponto

# if primitiva = 1
#   plotPixel(x,y,cor)

# if primitiva = 2
#   plotPixel(x,y,cor)
#   plotPixel(x+1,y,cor)
#   plotPixel(x,y-1,cor)
#   etc ...

def corrigirCoordenadas(x, y, janela):
    x = x + (janela.width)/2
    y = (janela.height)/2 - y
    return {'x':x, 'y':y}

# win = GraphWin("Tela Radar", 800, 600)

# teste = corrigirCoordenadas(800, 600, win)
# print(teste)
# print(teste["x"])
# print(teste["y"])

def Ponto(x, y, cor, primitiva, janela):
    coordenadasCorrgidas = corrigirCoordenadas(x, y, janela)
    x = coordenadasCorrgidas["x"]
    y = coordenadasCorrgidas["y"]

    if primitiva == 1:
        point = Point(x,y)
        point.setFill(cor)
        point.draw(janela)
        janela.getMouse()
        janela.close()




# win = GraphWin("Tela Radar", 800, 600)

# Ponto(0,0,"red",0,win)


