import random
import time
from tkinter import *


master = Tk()
master.title("Points")


canvas_width = 1000
canvas_height = 800
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack(expand=YES, fill=BOTH)
w.pack()

##definir les variables

Ox = (random.randint(100, 900))
Oy = (random.randint(100, 700))
m = 30
dt = 0.1
t = 0
size = 10
nb = 3


def paint(x, y, color):    ##la fonction paint cree les points
    color
    x1, y1 = (x - size), (y - size)
    x2, y2 = (x + size), (y + size)
    w.create_oval(x1, y1, x2, y2, fill=color)


class point():    ##cree la fonction point

    def __init__(self,m,dt,Ox,Oy):    ##initialisation (self = lui meme) tout les variable sont propres a luis
        self.Ox = Ox
        self.Oy = Oy
        self.m = m
        self.dt = dt
        self.Mx = (random.randint(0, 800))
        self.My = (random.randint(0, 1000))
        self.OMx = 0
        self.OMy = 0
        self.fx = 0
        self.fy = 0
        self.ax = 0
        self.ay = 0
        self.vx = 100
        self.vy = 50


    def calcule(self):    ## calcule de son prochain point
        self.OMx = self.Mx - self.Ox
        self.OMy = self.My - self.Oy
        self.fx = m * (-self.OMx)
        self.fy = m * (-self.OMy)
        self.ax = (1 / self.m) * self.fx
        self.ay = (1 / self.m) * self.fy
        self.vx = self.vx + (self.ax * self.dt)
        self.vy = self.vy + (self.ay * self.dt)
        self.Mx = self.Mx + (self.vx * self.dt)
        self.My = self.My + (self.vy * self.dt)


    def show(self):    ## met le point sur la carte
        paint(self.Mx,self.My,"#FF0000")

flock = [point(m,dt,Ox,Oy) for _ in range(nb)]    ## cree nb de point dans la liste


while True:
    for p in flock:    ##fais un par un les commande pour chaque elements de la liste
        p.calcule()
        p.show()

    paint(Ox, Oy, "#000000")
    master.update()
    time.sleep(0.05)
    w.delete("all")



mainloop()