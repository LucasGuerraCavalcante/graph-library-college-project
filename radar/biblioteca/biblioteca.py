from tkinter import *
from graphics import *

def corrigirCoordenadas(x, y, janela):
    x = x + (janela.width)/2
    y = (janela.height)/2 - y
    return {'x':x, 'y':y}

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

# estilo 0 -> reta contínua 
# estilo 1 -> reta pontilhada 
# estilo 2 -> reta tracejada 

def Reta(x1,y1,x2,y2, cor, primitiva, janela, estilo = 0):

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
            
            if estilo != 0:
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

                if estilo == 0:
                    # Reta continua, desenha os pontos normalmente
                    Ponto(x, y, cor, primitiva, janela, False)

                elif estilo == 1:  
                    # Reta pontilhada 
                    if counter % 5 == 0:
                        counter += 1
                        Ponto(x, y, cor, primitiva, janela, False)
                    else:
                        counter += 1
                
                elif estilo == 2:   
                    # Reta Tracejada 
                    if counter == 2 or counter == 3 or counter == 4 or counter == 5:
                        counter += 1
                        Ponto(x, y, cor, primitiva, janela, False)
                    else:
                        counter += 1
                        if counter == 10:
                            counter = 0

                else:
                    print("Erro: Escolha somente um estilo para a reta, 0, 1 ou 2]")
                        
        else: # Eixo y dominante
            
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

            if estilo != 0:
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

                if estilo == 0:
                    # Reta continua, desenha os pontos normalmente
                    Ponto(x, y, cor, primitiva, janela, False)

                elif estilo == 1:  
                    # Reta pontilhada 
                    if counter % 4 == 0:
                        counter += 1
                        Ponto(x, y, cor, primitiva, janela, False)
                    else:
                        counter += 1
                
                elif estilo == 2:   
                    # Reta Tracejada 
                    if counter == 2 or counter == 3 or counter == 4 or counter == 5:
                        counter += 1
                        Ponto(x, y, cor, primitiva, janela, False)
                    else:
                        counter += 1
                        if counter == 10:
                            counter = 0

                else:
                    print("Erro: Escolha somente um estilo para a reta, 0, 1 ou 2]")


# Funcao resposavel apenas por desenhar os quadrantes do circulo ao mesmo tempo, colocando dois pontos em cada
def desenharQuadrantes(xc, yc, x, y, cor, primitiva, janela):
    Ponto( x + xc, y + yc, cor, primitiva, janela, False)
    Ponto( y + xc,  x + yc, cor, primitiva, janela, False)
    Ponto( -x + xc,  y + yc, cor, primitiva, janela, False)
    Ponto( -y + xc,  x + yc, cor, primitiva, janela, False)
    Ponto( -x + xc, -y + yc, cor, primitiva, janela, False)
    Ponto( -y + xc, -x + yc, cor, primitiva, janela, False)
    Ponto( x + xc, -y + yc, cor, primitiva, janela, False)
    Ponto( y + xc, -x + yc, cor, primitiva, janela, False)

def Circulo(xc, yc, r, cor, primitiva, janela):

    coordenadasCorrgidas = corrigirCoordenadas(xc, yc, janela)
    xc = coordenadasCorrgidas["x"]
    yc = coordenadasCorrgidas["y"]

    x = r
    y = 0
    err = 1-x

    # Algortimo de Bersenham 
    while x >= y:    

        # chama a funcao para desenhar os quadrantes
        desenharQuadrantes(xc, yc, x, y, cor, primitiva, janela)

        y = y + 1

        if err < 0:
            err = err + 2 * y + 1
        else:
            x = x - 1
            err = err + 2 * (y - x + 1)

def Texto(x, y, palavra, cor, tamanho, estilo, janela):

    coordenadasCorrgidas = corrigirCoordenadas(x, y, janela)
    x = coordenadasCorrgidas["x"]
    y = coordenadasCorrgidas["y"]

    t = Text(Point(x, y), palavra)
    t.setOutline(cor)
    t.setSize(tamanho)
    t.setStyle(estilo)
    t.draw(janela)

# calcula a (x', y') da tela realtiva ao ponto (x, y, z) 
# do aviao no espaco 3D com o onservador a distancia F da origem
# do sistema de coordenadas e o plano projetivo a distancia f do observador
def Aviao(x, y, z, f, F, janela):

    x1 = x * f / (F - z)
    y1 = y * f / (F - z)

    coordenadasCorrgidas = corrigirCoordenadas(x1, y1, janela)
    x1 = coordenadasCorrgidas["x"]
    y1 = coordenadasCorrgidas["y"]

    imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/biblioteca/src/decolando/0.png"
    aviao = Image(Point(x1,y1), imagem)
    aviao.draw(janela)







# def Aviao(x, y, decolando, angulo, janela):
#         coordenadasCorrgidas = corrigirCoordenadas(x, y, janela)
#         x = coordenadasCorrgidas["x"]
#         y = coordenadasCorrgidas["y"]

#         if decolando is True:
#             if angulo == 0:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/decolando/0.png"
#             elif angulo == 30:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/decolando/30.png"
#             elif angulo == 90:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/decolando/90.png"
#             elif angulo == 150:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/decolando/150.png"
#             elif angulo == 180:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/decolando/180.png"
#             elif angulo == 210:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/decolando/210.png"
#             elif angulo == 270:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/decolando/270.png"
#             elif angulo == 330:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/decolando/330.png"
#             else:
#                 print("Angulo não disponível [0, 30, 90, 150, 180, 210, 270, 330]")
        
#         elif decolando is False:
#             if angulo == 0:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/pousando/0.png"
#             elif angulo == 30:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/pousando/30.png"
#             elif angulo == 90:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/pousando/90.png"
#             elif angulo == 150:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/pousando/150.png"
#             elif angulo == 180:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/pousando/180.png"
#             elif angulo == 210:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/pousando/210.png"
#             elif angulo == 270:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/pousando/270.png"
#             elif angulo == 330:
#                 imagem = "/Users/Bete/Desktop/Trabalhos/graph-library-college-project/radar/library/src/pousando/330.png"
#             else:
#                 print("Angulo não disponível [0, 30, 90, 150, 180, 210, 270, 330]")
#         else:
#             print("O argumento decolando deve ser definido [True, False]")

#         aviao = Image(Point(x,y), imagem)
#         aviao.draw(janela)
