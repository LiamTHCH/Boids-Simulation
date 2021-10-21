import random
import time
from tkinter import *
from math import *
import statistics

## Definir la fenètre 

master = Tk()
master.title("Points")

canvas_width = 1000
canvas_height = 800
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack(expand=YES, fill=BOTH)
w.pack()


## Definir les variables

Ox = (random.randint(100, 900))    
Oy = (random.randint(100, 700))
m = 30
dt = 0.1
t = 0
size = 5
nb = 20    ## Nombre de points     
vrange = 300    
maxspeed = 100
sepaprationdistance = 20


def paint(x, y, color):    ## La fonction paint cree les points
    x1, y1 = (x - size), (y - size)
    x2, y2 = (x + size), (y + size)
    w.create_oval(x1, y1, x2, y2, fill=color)


class point():    ## Cree la fonction point


    def __init__(self,m,dt,Ox,Oy,range):    ## Initialise les variable, (self = lui meme) tout les variable sont propres à lui
        self.Ox , self.Oy = Oy , Ox
        self.m = m
        self.range = range
        self.dt = dt
        self.Mx , self.My = (random.randint(0, 1000)),(random.randint(0, 800))
        self.OMx , self.OMy =  0,0
        self.fx , self.fy = 0,0
        self.ax , self.ay = 0,0
        self.vx , self.vy = (random.randint(-200, 200)),(random.randint(-200, 200))
        self.Nx , self.Ny = 0,0
        self.Vsx  ,self.Vsy = 0,0
        self.Vomx , self.Vomy = 0,0
        

    def calcule(self):    ## Calcule de sa prochaine position
        global maxspeed
        self.OMx = self.Mx - self.Ox
        self.OMy = self.My - self.Oy
        self.OMx = self.OMx + self.Vsx
        self.OMy = self.OMy + self.Vsy
        self.OMx = self.OMx + self.Vomx
        self.OMy = self.OMy + self.Vomy
        self.fx = m * (-self.OMx)
        self.fy = m * (-self.OMy)
        self.ax = (1 / self.m) * self.fx
        self.ay = (1 / self.m) * self.fy
        self.vx = self.vx + (self.ax * self.dt)
        self.vy = self.vy + (self.ay * self.dt)


        ## Limite la vitesse des points

        if not -maxspeed <= self.vx <= maxspeed:
            if self.vx > 0:
                self.vx = maxspeed
            else:
                self.vx = -maxspeed


        if not -maxspeed <= self.vy <= maxspeed:
            if self.vy > 0:
                self.vy = maxspeed
            else:
                self.vy = -maxspeed

        self.Mx = self.Mx + (self.vx * self.dt)
        self.My = self.My + (self.vy * self.dt)


    def coherence(self):    ## Les points satirent les un les autres si ils sont a moins d'une distance donner
        listx = []
        listy =[]

        for boids in flock:
            distance = sqrt(((self.Mx-boids.Mx)**2)+((self.My-boids.My)**2))

            if distance <= self.range:
                listx.append(boids.Mx)
                listy.append(boids.My)

        self.Ox = statistics.mean(listx)
        self.Oy = statistics.mean(listy)


    def separation(self):    ## Separe les points entre eux si il sont trop près
        global sepaprationdistance
        vecteurx = []
        vecteury = []
        for boids in flock:
            distance = sqrt(((self.Mx-boids.Mx)**2)+((self.My-boids.My)**2))

            if (distance <= sepaprationdistance) and (distance != 0):
              vecteurx.append((boids.Mx-self.Mx)*1/distance)
              vecteury.append((boids.My-self.My)*1/distance)
        self.Vsx = sum(vecteurx)
        self.Vsy = sum(vecteury)


    def alignement(self):    ## Aligne les points dans une même direction
        vecteurx = []
        vecteury = []
        for boids in flock:
            distance = sqrt(((self.Mx-boids.Mx)**2)+((self.My-boids.My)**2))
            if distance <= self.range:
                vecteurx = vecteurx + [self.OMx]
                vecteury = vecteury + [self.OMy]
        self.Vomx = statistics.mean(vecteurx)
        self.Vomy = statistics.mean(vecteury)


    def bord(self):    ## Fais passer de l'autre coter les points si il touche le bord

        if self.Mx > canvas_width:
            self.Mx = 0
        elif self.Mx < 0:
            self.Mx = canvas_width

        if self.My > canvas_height:
            self.My = 0
        elif self.My < 0:
            self.My = canvas_height


    def show(self):    ## Met le point sur la carte
        paint(self.Mx,self.My,"#FF0000")
        #w.create_line(self.Mx,self.My,self.Ox,self.Oy)     ## Crée une ligne vers où les points sont attirés 
        #paint(self.Ox, self.Oy, "#00FF00")                 ## Fait le point O de chaque points visible 


    def direction(self):
        self.Ny = self.My + 20 * sin(atan2(self.OMx,self.OMy))
        self.Nx = self.Mx + 20*cos(atan2(self.OMx,self.OMy))


flock = [point(m,dt,Ox,Oy,vrange) for _ in range(nb)]       ## Crée nb de point dans la liste

while True:

    for p in flock:    ## Fais un par un les commande pour chaque elements de la liste
        p.coherence()
        p.separation()
        p.calcule()
        p.bord()
        p.show()
        #print(degrees(atan2(p.OMx,p.OMy)))
    master.update()
    time.sleep(0.05)
    w.delete("all")
