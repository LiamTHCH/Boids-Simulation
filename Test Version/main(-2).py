import random

import time

from tkinter import *

master = Tk()
master.title("Points")

canvas_width = 5000
canvas_height = 1500

w = Canvas(master,width=canvas_width,height=canvas_height)
w.pack(expand=YES, fill=BOTH)


width = 500
height = 150
OMx = 0
OMy = 0
fx = 0
fy = 0
ax = 0
ay = 0
vx = 100
vy = 50
Ox = (random.randint(200,300))
Oy = (random.randint(700,800))
Mx = (random.randint(200,300))
My = (random.randint(700,800))
m = 30
dt=1
t=0

def paint(x,y,color):
    python_green = color
    x1, y1 = (x - 10), (y - 10)
    x2, y2 = (x + 10), (y + 10)
    w.create_oval(x1, y1, x2, y2, fill=python_green)

paint(Ox,Oy,"#000000")
while t < 100 :

  t = t+1

  OMx = Mx - Ox
  OMy = My - Oy

  fx = m * (-OMx)
  fy = m * (-OMy)

  ax = (1 / m) * fx
  ay = (1 / m) * fy

  vx = vx + (ax * dt)
  vy = vy + (ay * dt)
  Mx = Mx + (vx * dt)
  My = My + (vy * dt)
  paint(Mx,My,"#FF0000")
  print(Mx,My)
mainloop()
