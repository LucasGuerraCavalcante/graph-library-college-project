from tkinter import *
from graphics import *

'''

 def ponto(valorx, valory, cor, primitiva):

 rodar o sistema de coordenadas

 desenhar o ponto

 if primitiva = 1
   plotPixel(x,y,cor)

 if primitiva = 2
    plotPixel(x,y,cor)
    plotPixel(x+1,y,cor)
    plotPixel(x,y-1,cor)
    etc ...

'''

def corrigirCoordenadas(x, y, janela):
    x = x + (janela.width)/2
    y = (janela.height)/2 - y
    return {'x':x, 'y':y}

'''
win = GraphWin("Tela Radar", 800, 600)

teste = corrigirCoordenadas(800, 600, win)
print(teste)
print(teste["x"])
print(teste["y"])
'''

def Ponto(x, y, cor, primitiva, janela, corrigirXY = True):
  
    if corrigirXY is True:
        coordenadasCorrgidas = corrigirCoordenadas(x, y, janela)
        x = coordenadasCorrgidas["x"]
        y = coordenadasCorrgidas["y"]
    else:
        pass

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
Ponto(100,-100,"red",1,win)
Ponto(0,0,"green",2,win)
Ponto(100,-100,"green",2,win)
Ponto(0,0,"blue",3,win)
Ponto(100,100,"blue",3,win)
Ponto(0,0,"purple",4,win)
Ponto(-100,100,"purple",4,win)
'''
Ponto(0,0,"red",1,win)
Ponto(30,90,"green",2,win)
Ponto(10,100,"blue",3,win)
Ponto(100,100,"purple",4,win)
Ponto(100,100,"purple",0,win)
'''


def Reta(x1,y1,x2,y2, cor, primitiva, janela):

    coordenadasCorrgidasA = corrigirCoordenadas(x1, y1, janela)
    x1 = coordenadasCorrgidasA["x"]
    y1 = coordenadasCorrgidasA["y"]

    coordenadasCorrgidasB = corrigirCoordenadas(x2, y2, janela)
    x2 = coordenadasCorrgidasB["x"]
    y2 = coordenadasCorrgidasB["y"]

    if x1 == x2 and y1 == y2:
        Ponto(x1, y1, cor, primitiva, janela, False)
    else:
        # Algoritmo de Bresenham
        # Distancias (Deltas)
        dx = x2 - x1
        dy = y2 - y1
        # Copias positivas do Delta
        dx1 = abs(dx)
        dy1 = abs(dy)
    
        # Calcular intervalo de erro em ambos eixos
        px = 2 * dy1 - dx1
        py = 2 * dx1 - dy1
    
        # Eixo x dominante
        if (dy1 <= dx1):
            
            # Desenhar da esquerda pra direita
            if (dx >= 0):
                x = x1
                y = y1
                xe = x2
            else: # Desenhar da direita pra esquerda
                x = x2
                y = y2
                xe = x1
            
            while (x < xe):
                x = x + 1
                
                if px < 0:
                    px = px + 2 * dy1
                else:
                    if ((dx < 0 and dy < 0) or (dx > 0 and dy > 0)):
                        y = y + 1;
                    else:
                        y = y - 1;
            
                    px = px + 2 * (dy1 - dx1)

                Ponto(x, y, cor, primitiva, janela, False)

        else: # Eixo y dominante
            
            # Desenhar de baixo pra cima
            if (dy >= 0):
                x = x1
                y = y1
                ye = y2
            else: # Desenhar de cima pra braixo
                x = x2
                y = y2
                ye = y1;
            
            Ponto(x, y, cor, primitiva, janela, False)
            
            while (y < ye):
                y = y + 1
                
                if py <= 0:
                    py = py + 2 * dx1
                else:
                    if ((dx < 0 and dy<0) or (dx > 0 and dy > 0)):
                        x = x + 1
                    else:
                        x = x - 1

                    py = py + 2 * (dx1 - dy1)

                Ponto(x, y, cor, primitiva, janela, False)

    

Reta(0,0,100,-100,"red",1,win)
Reta(0,0,-100,-100,"green",1,win)
Reta(0,0,100,100,"blue",3,win)
Reta(0,0,-100,100,"purple",4,win)
#Reta(100,100,"purple",0,win)

win.getMouse()
win.close()

# https://www.freecodecamp.org/news/how-to-code-your-first-algorithm-draw-a-line-ca121f9a1395/