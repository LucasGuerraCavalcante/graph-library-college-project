
# Lucas Guerra & Rafael Viana

from graphics import * # Biblioteca graphics
from math import * # Biblioteca para calcular o angulo baseado no coeficente angular
import pandas as pd # Biblioteca para ler a planilha
import time # Biblioteca para auxiliar na varredura do radar usando sleep(x), executa algo apos x segundos
import os # Biblioteca para auxiliar na navegacao de diretorios para o python encontrar os icones dos avioes

''' 
#################################################
######### DECLARANDO AS FUNCOES #################
#################################################
'''

# Funcao que desloca a posicao (0,0) do canto superior esquerdo para o centro da tela
def corrigirCoordenadas(x, y, janela):
    x = x + (janela.width)/2
    y = (janela.height)/2 - y
    return {'x':x, 'y':y}

# Funcao que desenha um ponto de diferentes tamanhos (primitivas)
def Ponto(x, y, cor, primitiva, janela, corrigirXY = True):
  
    # Corrige o valor (x, y) considerando o ponto (0,0) no meio da tela, se necessario
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

# Funcao que desenha uma reta de diferentes estilos

# estilo 0 -> reta contínua 
# estilo 1 -> reta pontilhada 
# estilo 2 -> reta tracejada 

def Reta(x1,y1,x2,y2, cor, primitiva, janela, estilo = 0):

    # Corrige o valor (x, y) considerando o ponto (0,0) no meio da tela
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
# Fizemos assim pois deixa o desenho do circulo mais rapido, ao inves de desenhar um quadrante por vez, desse modo
# todos os quadrantes sao desenhados ao mesmo tempo
def desenharQuadrantes(xc, yc, x, y, cor, primitiva, janela):
    Ponto( x + xc, y + yc, cor, primitiva, janela, False)
    Ponto( y + xc,  x + yc, cor, primitiva, janela, False)
    Ponto( -x + xc,  y + yc, cor, primitiva, janela, False)
    Ponto( -y + xc,  x + yc, cor, primitiva, janela, False)
    Ponto( -x + xc, -y + yc, cor, primitiva, janela, False)
    Ponto( -y + xc, -x + yc, cor, primitiva, janela, False)
    Ponto( x + xc, -y + yc, cor, primitiva, janela, False)
    Ponto( y + xc, -x + yc, cor, primitiva, janela, False)

# Funcao que faz os calculos e desenha o circulo
def Circulo(xc, yc, r, cor, primitiva, janela):

    # Corrige o valor (x, y) considerando o ponto (0,0) no meio da tela
    coordenadasCorrgidas = corrigirCoordenadas(xc, yc, janela)
    xc = coordenadasCorrgidas["x"]
    yc = coordenadasCorrgidas["y"]

    x = r
    y = 0
    err = 1-x

    # Algortimo de Bersenham 
    while x >= y:    

        # Chama a funcao para desenhar os quadrantes
        desenharQuadrantes(xc, yc, x, y, cor, primitiva, janela)

        y = y + 1

        if err < 0:
            err = err + 2 * y + 1
        else:
            x = x - 1
            err = err + 2 * (y - x + 1)

# Funcao que escreve um texto na tela
def Texto(x, y, palavra, cor, tamanho, estilo, janela, corrgirXY = True):

    # Corrige o valor (x, y) considerando o ponto (0,0) no meio da tela, se necessario
    if corrgirXY == True:
        coordenadasCorrgidas = corrigirCoordenadas(x, y, janela)
        x = coordenadasCorrgidas["x"]
        y = coordenadasCorrgidas["y"]

    texto = Text(Point(x, y), palavra)
    texto.setOutline(cor)
    texto.setSize(tamanho)
    texto.setStyle(estilo)
    texto.draw(janela)

    return texto

# Funcao que inicia e desenha a tela de fundo
def Tela_de_Fundo():

    janela = GraphWin("Tela Radar", 1000, 800)
    janela.setBackground("#000")

    Reta(-1000, 800, 1000, -800,"#339966",1,janela, 2)
    Reta(1000, 800, -1000, -800,"#339966",1,janela, 2)
    Reta(0, 800, 0, -800,"#339966",1,janela, 2)
    Reta(1000, 0, -1000, 0,"#339966",1,janela, 2)

    Circulo(0, 0, 90, "#339966", 1, janela)
    Circulo(0, 0, 190, "#339966", 1, janela)
    Circulo(0, 0, 290, "#339966", 1, janela)
    Circulo(0, 0, 390, "#339966", 1, janela)

    Texto(15, 370, "0°", "#339966", 15, "bold", janela)
    Texto(30, -370, "180°", "#339966", 15, "bold", janela)
    Texto(420, 15, "90°", "#339966", 15, "bold", janela)
    Texto(-420, 15, "270°", "#339966", 15, "bold", janela)

    return janela

# Funcao que apaga todos os avioes da tela 
# (apaga apenas os avioes e seus codigos de voo, a tela de fundo fica intacta)
def Limpar_Avioes(avioes):

    for aviao in avioes:
        (aviao['aviao']).undraw()
        (aviao['codigo']).undraw()


# Funcao que calcula o (x', y') da tela realtiva ao ponto (x, y, z) 
# do aviao no espaco 3D com o onservador a distancia F da origem
# do sistema de coordenadas e o plano projetivo a distancia f do observador
def Projetar(x, y, z, f, F, janela):

    x2 = x * f / (F - z)
    y2 = y * f / (F - z)

    return {'x':x2, 'y':y2}

# Funcao que retorna o angulo (direcao do aviao)
def Direcao(x, y):

    # y = x*m + B
    # (1) 0 = 0*m + B = B
    # (2) y = x*m + B -> m = y/x 

    if x == 0 or y == 0:
        return 0
    else:
        m = y/x
        # calcula a arco targente de m (radianos) e depois converte para graus 
        angulo = degrees(atan(m))

        return angulo

# Funcao que desenha o aviao e o codigo de voo na tela
# obs: status = cor do icone
def Aviao(x, y, angulo, status, codigo_de_voo, janela):

    # aproximando o angulo calculado ao angulo dos icones (baseado no angulo teta da reta em relacao a (x,y))
    if 0 <= angulo <= 10:
        angulo = '0'
    elif 10 < angulo <= 67:
        angulo = '45'
    elif 67 < angulo <= 112:
        angulo = '90'
    elif 112 < angulo <= 157:
        angulo = '135'
    elif 157 < angulo <= 180:
        angulo = '180'
    elif 0 > angulo >= -10:
        angulo = '0'
    elif -10 > angulo >= -67:
        angulo = '-45'  
    elif -67 > angulo >= -112:
        angulo = '-90'
    elif -112 > angulo >= -157:
        angulo = '-135'
    elif -157 > angulo >= -180:
        angulo = '180'

    # selecionando o icone a partir do angulo e do status (cor) 
    icone = 'biblioteca/src/%s/%s.png'%(status, angulo)

    # selecionando o direotiro atual para o python encontrar a pasta dos icones
    diretorioAtual = os.path.dirname(__file__)

    # Corrige o valor (x, y) considerando o ponto (0,0) no meio da tela
    coordenadasCorrgidas = corrigirCoordenadas(x, y, janela)
    x = coordenadasCorrgidas["x"]
    y = coordenadasCorrgidas["y"]

    aviao = Image(Point(x,y), os.path.join(diretorioAtual, icone))
    aviao.draw(janela)

    codigo = Texto(x + 35, y, codigo_de_voo, "#FFF", 10, "bold", janela, False)

    return {'aviao':aviao, 'codigo':codigo}

''' 
############################################################
######### DESENHANDO O GRAFICO E OS AVIOES #################
############################################################
'''

# Lendo e salvando a planilha
planilha = pd.read_csv("data/planilha_radar.csv", usecols = ['T','Status','Voo','X','Y','Z'])

# Desenhado o fundo do radar
radar = Tela_de_Fundo()

# Contator que auxilia na varredura do radar
ct = 0
# Array com os avioes presentes em tela
avioes = []
# Loop percorrendo as linhas da planilha
for index, row in planilha.iterrows():

    # Desenhando os 5 avioes, apos desenhar os 5, o contador zera, apaga os avioes
    # e desenha os mesmos 5 avioes na proxima posicao

    if ct < 5:
        # Calculos do aviao
        calculo = Projetar(row['X'], row['Y'], row['Z'], 1000, 62000, radar)
        angulo = Direcao(calculo['x'], calculo['y'])

        # Projetar aviao
        aviao = Aviao(calculo['x'], calculo['y'], angulo, row['Status'], row['Voo'], radar)
        # Adicionando o aviao desenhado ao array
        avioes.append(aviao)

        ct += 1

    else:
        ct = 0
        # Limpar avioes

        # Espera 3 segundos 
        time.sleep(3)
        # Apaga todos os avioes e sues codigos de voo presentes na tela
        Limpar_Avioes(avioes)


            