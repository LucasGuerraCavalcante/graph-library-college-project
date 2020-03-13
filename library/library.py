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
        pixel = Point(x,y)
        pixel.setFill(cor)
        pixel.draw(janela)
        return janela

    elif primitiva == 2: 
        points = [Point(x,y),Point(x+1,y+1),
                  Point(x+1,y),Point(x,y+1)]
        for ponto in points:
            pixel = ponto
            pixel.setFill(cor)
            pixel.draw(janela)
        return janela

    elif primitiva == 3:     
        points = [Point(x+1,y),Point(x-1,y),
                  Point(x,y+1),Point(x,y-1),
                  Point(x,y)]
        for ponto in points:
            pixel = ponto
            pixel.setFill(cor)
            pixel.draw(janela)
        return janela
        
    elif primitiva == 4:              
        points = [Point(x,y),Point(x+1,y+1),Point(x+1,y),Point(x,y+1),
                  Point(x-1,y),Point(x+2,y),Point(x,y-1),Point(x,y+2),
                  Point(x-1,y+1),Point(x+1,y+2),Point(x+2,y+1),Point(x+1,y-1)]
        for ponto in points:
            pixel = ponto
            pixel.setFill(cor)
            pixel.draw(janela)
        return janela
    else:
        print("ERROR: Primitiva incorreta ou não permitida")
    



