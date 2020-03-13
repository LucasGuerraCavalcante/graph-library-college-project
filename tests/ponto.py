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





win = GraphWin("Tela Radar", 800, 600)

Ponto(0,0,"red",1,win)
Ponto(30,90,"green",2,win)
Ponto(10,100,"blue",3,win)
Ponto(100,100,"purple",4,win)
Ponto(100,100,"purple",0,win)

win.getMouse()
win.close()


