from tkinter import *
from graphics import * 

# import math 

# https://mcsp.wartburg.edu/zelle/python/graphics.py

# Montando a primeira tela

def main():
    win = GraphWin("Tela Radar", 800, 600)
    win.setBackground(color_rgb(16, 16, 37))

    print(win.width)

    point = Point(400,300)
    point.setFill("lime")
    point.draw(win)

    aCircle = Circle(point, 50)
    bCircle = Circle(point, 100)
    cCircle = Circle(point, 150)
    dCircle = Circle(point, 200)
    eCircle = Circle(point, 250)
    fCircle = Circle(point, 300)
    gCircle = Circle(point, 350)
    hCircle = Circle(point, 400)
    iCircle = Circle(point, 450)
    jCircle = Circle(point, 500)

    aCircle.draw(win)
    bCircle.draw(win)
    cCircle.draw(win)
    dCircle.draw(win)
    eCircle.draw(win)
    fCircle.draw(win)
    gCircle.draw(win)
    hCircle.draw(win)
    iCircle.draw(win)
    jCircle.draw(win)

    win.getMouse() 
    win.close()

main()



