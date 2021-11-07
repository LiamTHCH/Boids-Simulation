import random

import time

from tkinter import *

master = Tk()
master.title("Points")

canvas_width = 1000
canvas_height = 800

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
Ox = (random.randint(400,600))
Oy = (random.randint(400,600))
Mx = (random.randint(400,600))
My = (random.randint(400,600))
m = 30
dt=1
t=0
size =10




def paint(x,y,color):
    python_green = color
    x1, y1 = (x - size), (y - size)
    x2, y2 = (x + size), (y + size)
    w.create_oval(x1, y1, x2, y2, fill=python_green)
    

paint(Ox,Oy,"#000000")

w.pack()


while t < 10:
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
  paint(Ox,Oy,"#000000")
  print(Mx,My)
  master.update()
  time.sleep(1)
  w.delete("all")





mainloop()