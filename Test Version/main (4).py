
import random
import time
from tkinter import *
from math import *
import statistics


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
size = 5
nb = 20
vrange = 300    ##300
maxspeed = 100
sepaprationdistance = 20


def paint(x, y, color):    ##la fonction paint cree les points
    x1, y1 = (x - size), (y - size)
    x2, y2 = (x + size), (y + size)
    w.create_oval(x1, y1, x2, y2, fill=color)


class point():    ##cree la fonction point

    def __init__(self,m,dt,Ox,Oy,range):    ##initialisation (self = lui meme) tout les variable sont propres a luis
        self.Ox = Ox
        self.Oy = Oy
        self.m = m
        self.range = range
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
        global maxspeed
        self.OMx = self.Mx - self.Ox
        self.OMy = self.My - self.Oy
        self.fx = m * (-self.OMx)
        self.fy = m * (-self.OMy)
        self.ax = (1 / self.m) * self.fx
        self.ay = (1 / self.m) * self.fy
        self.vx = self.vx + (self.ax * self.dt)
        self.vy = self.vy + (self.ay * self.dt)

        ##limiter la vitesse des points

        if -maxspeed <= self.vx <= maxspeed:
            print()

        else:

            if self.vx > 0:
                self.vx = maxspeed
            else:
                self.vx = -maxspeed

        if -maxspeed <= self.vy <= maxspeed:
            print()

        else:

            if self.vy > 0:
                self.vy = maxspeed
            else:
                self.vy = -maxspeed

        self.Mx = self.Mx + (self.vx * self.dt)
        self.My = self.My + (self.vy * self.dt)


    def coherence(self):    ##satire les un les autres si ils sont a moins d'une distance donner
        listx = []
        listy =[]

        for boids in flock:
            distance = sqrt(((self.Mx-boids.Mx)**2)+((self.My-boids.My)**2))

            if distance <= self.range:
                listx.append(boids.Mx)
                listy.append(boids.My)

        self.Ox = statistics.mean(listx)
        self.Oy = statistics.mean(listy)

    def separation(self):    ##separe les points entre eux si il sont trop pr??s
        global sepaprationdistance

        for boids in flock:
            distance = sqrt(((self.Mx-boids.Mx)**2)+((self.My-boids.My)**2))

            if distance <= sepaprationdistance:

                self.Ox = self.Ox - (boids.Ox*2)
                self.Oy = self.Oy - (boids.Oy*2)

    def bord(self):    ## Fais passer de l'autre coter les points si il touche le bord

        if self.Mx > canvas_width:
            self.Mx = 0
        elif self.Mx < 0:
            self.Mx = canvas_width

        if self.My > canvas_height:
            self.My = 0
        elif self.My < 0:
            self.My = canvas_height

    def show(self):    ## met le point sur la carte
        paint(self.Mx,self.My,"#FF0000")

flock = [point(m,dt,Ox,Oy,vrange) for _ in range(nb)]    ## cree nb de point dans la liste

while True:

    for p in flock:    ##fais un par un les commande pour chaque elements de la liste
        p.coherence()
        #p.separation()
        p.calcule()
        p.bord()
        p.show()

    master.update()
    time.sleep(0.05)
    w.delete("all")
