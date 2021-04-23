from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
import numpy as np
import random as rdn
### Algorithm ###
def set_pixel(x, y, r, g, b, size):
    glColor3f(r, g, b)
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    
    #pygame.display.flip()
    #print("{}\t{}".format(x, y))
    pygame.time.wait(10)
    glFlush()

def color_pixel(width, height, x, y, size):
    rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size
    ,
    GL_RGB,
    GL_UNSIGNED_BYTE, None)
    return list(rgb)

def Bressennham(x1, y1, x2, y2, r, g, b, size):
	#inicializar variable
  x = x1
  y = y1
  #calcular los diferenciales
  dx = abs(x2-x1)
  dy = abs(y2-y1)
  if dx==0:
  	m=0
  else:
  	m= dy/dx
  #bresenham maneja el artificio de los signos para dibujar en cualquier cuadrante
  Sx = np.sign(x2-x1) #5
  Sy = np.sign(y2-y1) #6 
  #el swap deacuerdo a la pendiente. Si es mayor a 1 entonces dy crece más, por tanto el swap 
  if (dy>dx): 
    t = dx
    dx = dy
    dy = t
    steps = dx #steps o largo de linea
    flag = 1
  else:
    steps = dx
    flag = 0
  #el Pk viene a ser el valor de error o fault visto en otras versiones del algoritmo
  Pk = 2*dy - dx 
  # dibuja el punto inicial
  set_pixel(x,y,r,g,b,size)

  # comienza a iterar a lo largo de la linea (definido por steps)
  for i in range(0,int(steps)): # range va hasta antes de un numero especifico, por eso el +1
    while Pk > 0: 
      if flag == 1:
        x += Sx   
      else:
        y += Sy
      Pk = Pk - 2*dx 
    if flag == 1:
      y += Sy
    else:
      x += Sx  
    Pk += 2*dy 
    set_pixel(x,y,r,g,b,size)

def DrawPolygon(vertices, r, g, b, size):
	# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
	vertices.append(vertices[0])
	for k in range(len(vertices) - 1):
		x0, y0, z0 = vertices[k]
		x1, y1, z0 = vertices[k + 1]
		Bressennham(x0, y0, x1, y1, r, g, b, size)		

def display_openGL(width, height, scale):
    pygame.display.set_mode((width, height), pygame.OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # glScalef(scale, scale, 0)
    gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)

#Traslación de un polígono
def Traslate(vertices, tx, ty):
	T=[[1,0,tx], [0,1,ty], [0,0,1]]
	result = []
	for item in vertices:
		point = np.dot(T, item)
		result.append(point)
	return result

#Rotación de un polígono
def Rotation(vertices, angle):
	angle = math.radians(angle)
	R=[[math.cos(angle), -math.sin(angle), 0],
	[math.sin(angle), math.cos(angle), 0], [0, 0, 1]]
	result = []
	for item in vertices:
		point = np.dot(R, item)
		result.append(point)
	return result

#Escalamiento de un poligono
def Escalamiento(vertices, sx, sy):
	S = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
	result  = []
	for item in vertices:
		point = np.dot(S, item)
		result.append(point)
	return result

#Reflexion de un poligono
def Reflexion(vertices, angle):
	angle = math.radians(angle)
	R = [[math.cos(angle*2), math.sin(angle*2), 0],
		[math.sin(angle*2), -math.cos(angle*2), 0],
		[0, 0, 1]]
	result = []
	for item in vertices:
		point = np.dot(R, item)
		result.append(point)
	return result

#Deformacion de un poligono
def Deformacion(vertices, angle, factor):
	angle = math.radians(angle)
	R = [[1-factor*math.sin(angle)*math.cos(angle), factor*math.cos(angle)*math.cos(angle), 0],
		[-factor*math.sin(angle)*math.sin(angle), 1+factor*math.sin(angle)*math.cos(angle), 0],
		[0, 0, 1]]
	result = []
	for item in vertices:
		point = np.dot(R,item)
		result.append(point)
	return result