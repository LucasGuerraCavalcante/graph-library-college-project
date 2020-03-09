from tkinter import *
from graphics import *

def corrigirCoordenadas(x, y, janela):
    x = x + (janela.width)/2
    y = (janela.height)/2 - y
    return {'x':x, 'y':y}

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

    



