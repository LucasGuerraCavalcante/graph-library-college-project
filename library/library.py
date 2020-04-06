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
    

def Reta(x1,y1,x2,y2, cor, primitiva, janela, pontilhado = False, tracejado = False):

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
        # Copias positivas do Delta (so para facilitar)
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

            Ponto(x, y, cor, primitiva, janela, False)
            
            if tracejado is True or pontilhado is True:
                counter = 0

            while (x < xe):
                x = x + 1
                
                if px < 0:
                    px = px + 2 * dy1
                else:
                    if ((dx < 0 and dy < 0) or (dx > 0 and dy > 0)):
                        y = y + 1
                    else:
                        y = y - 1
            
                    px = px + 2 * (dy1 - dx1)

                if pontilhado is False and tracejado is False:
                    # Reta continua, desenha os pontos normalmente
                    Ponto(x, y, cor, primitiva, janela, False)

                elif pontilhado is True and tracejado is False:  
                    # Reta pontilhada 
                    if counter % 5 == 0:
                        counter += 1
                        Ponto(x, y, cor, primitiva, janela, False)
                    else:
                        counter += 1
                
                elif pontilhado is False and tracejado is True:   
                    # Reta Tracejada 
                    if counter % 5 == 0 or counter % 6 == 0 or counter % 7 == 0 or counter % 8 == 0:
                        counter += 1
                        Ponto(x, y, cor, primitiva, janela, False)
                    else:
                        counter += 1

                elif pontilhado is True and tracejado is True:
                    print("Erro: Escolha somente uma opção, ou pontilhado ou tracejado")

        # Eixo y dominante
        else: 
            
            # Desenhar de baixo pra cima
            if (dy >= 0):
                x = x1
                y = y1
                ye = y2
            else: # Desenhar de cima pra braixo
                x = x2
                y = y2
                ye = y1
            
            Ponto(x, y, cor, primitiva, janela, False)

            if tracejado is True or pontilhado is True:
                counter = 0
            
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

                if pontilhado is False and tracejado is False:
                    # Reta continua, desenha os pontos normalmente
                    Ponto(x, y, cor, primitiva, janela, False)

                elif pontilhado is True and tracejado is False:  
                    # Reta pontilhada 
                    if counter % 5 == 0:
                        counter += 1
                        Ponto(x, y, cor, primitiva, janela, False)
                    else:
                        counter += 1
                
                elif pontilhado is False and tracejado is True:   
                    # Reta Tracejada 
                    if counter % 5 == 0 or counter % 6 == 0 or counter % 7 == 0 or counter % 8 == 0:
                        counter += 1
                        Ponto(x, y, cor, primitiva, janela, False)
                    else:
                        counter += 1

                elif pontilhado is True and tracejado is True:
                    print("Erro: Escolha somente uma opção, ou pontilhado ou tracejado")
                        
