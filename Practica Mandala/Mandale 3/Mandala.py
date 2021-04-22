from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
import numpy as np
import random as rdn

#Modulos
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
  for i in range(0,steps): # range va hasta antes de un numero especifico, por eso el +1
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

def Circle8v(xc, yc, radio, r, g, b, size):
	# set_pixel(xc, yc + radio, 0, 1, 0, size)
	# set_pixel(xc, yc - radio, 0, 0, 1, size)
	# set_pixel(xc + radio, yc, 0, 1, 0, size)
	# set_pixel(xc - radio, yc, 0, 0, 1, size)

	for x in range(math.ceil(radio / math.sqrt(2)) + 1):
		y = math.ceil(math.sqrt(radio * radio - x * x))
		set_pixel(xc + x, yc + y, r, g, b, size)
		set_pixel(xc - x, yc + y, r, g, b, size)
		set_pixel(xc - x, yc - y, r, g, b, size)
		set_pixel(xc + x, yc - y, r, g, b, size)

		set_pixel(xc + y, yc + x, r, g, b, size)
		set_pixel(xc - y, yc + x, r, g, b, size)
		set_pixel(xc - y, yc - x, r, g, b, size)
		set_pixel(xc + y, yc - x, r, g, b, size)

def DrawPolygon(vertices, r, g, b, size):
	# vertices = [(x1, x2), (x2, y2), ..., (xn, yn)]
	vertices.append(vertices[0])
	for k in range(len(vertices) - 1):
		x0, y0 = vertices[k]
		x1, y1 = vertices[k + 1]
		Bressennham(x0, y0, x1, y1, r, g, b, size)

def SimpleSeedFill(width, height, size, xi, yi, r, g, b):
	stack = []
	stack.append((xi, yi))
	while len(stack) > 0:
		x, y = stack.pop()

		if color_pixel(width, height, x, y, size) != [r, g, b]:
			set_pixel(x, y, r, g, b, size)
			#print(x, y)

		# examine surrounding pixels to see if they should be placed onto stack
		if color_pixel(width, height, x + 1, y, size) != [r, g, b]:
			stack.append((x + 1, y))

		"""if color_pixel(width, height, x + 1, y + 1, size) != [r, g, b]:
			stack.append((x + 1, y + 1))"""

		if color_pixel(width, height, x, y + 1, size) != [r, g, b]:
			stack.append((x, y + 1))

		"""if color_pixel(width, height, x - 1, y + 1, size) != [r, g, b]:
			stack.append((x - 1, y + 1))"""

		if color_pixel(width, height, x - 1, y, size) != [r, g, b]:
			stack.append((x - 1, y))

		"""if color_pixel(width, height, x - 1, y - 1, size) != [r, g, b]:
			stack.append((x - 1, y - 1))"""

		if color_pixel(width, height, x, y - 1, size) != [r, g, b]:
			stack.append((x, y - 1))

		"""if color_pixel(width, height, x + 1, y - 1, size) != [r, g, b]:
			stack.append((x + 1, y - 1))"""

def display_openGL(width, height, scale):
    pygame.display.set_mode((width, height), pygame.OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # glScalef(scale, scale, 0)
    gluOrtho2D(-1 * width / 2, width / 2, -1 * height / 2, height / 2)


#PROGRAMA
def main():
	scale = 1
	width, height = scale * 500, scale * 500

	pygame.init()
	pygame.display.set_caption('Mandala_Miguel')
	
	display_openGL(width, height, scale)
	# glColor3f(1.0, 0, 0)
	x = 0
	y = 0
	set_pixel(x, y, 1, 1, 1, scale)
		

	#MANDALA
	vertices3 = [(0,50),(40,90),(35,35),(90,40),(50,0),(90,-40),(35,-35),(40,-90),(0,-50),
				(-40,-90),(-35,-35),(-90,-40),(-50,-0),(-90,40),(-35,35),(-40,90)]
	vertices4 = [(35,35),(30,0),(35,-35),(0,-30),(-35,-35),(-30,0),(-35,35),(0,30)]
	vertices5 = [(40,90),(90,40),(90,-40),(40,-90),(-40,-90),(-90,-40),(-90,40),(-40,90)]

	
	Circle8v(0, 0, 100, 255/255, 255/255, 0/255, scale)
	DrawPolygon(vertices3, 255, 255, 0, scale)
	Circle8v(0, 0, 50, 255/255, 255/255, 0/255, scale)
	DrawPolygon(vertices4, 255, 255, 0, scale)
	DrawPolygon(vertices5, 255, 255, 0, scale)
	Circle8v(0, 0, 30, 255/255, 255/255, 0/255, scale)
	Bressennham(-35,35, 35, -35, 255, 255, 0, scale)	
	Bressennham(35,35, -35, -35, 255, 255, 0, scale)
	
	SimpleSeedFill(width, height, scale, 60, 60, 255, 255, 0)
	SimpleSeedFill(width, height, scale, -60, 60, 255, 255, 0)
	SimpleSeedFill(width, height, scale, -60, -60, 255, 255, 0)
	SimpleSeedFill(width, height, scale, 60, -60, 255, 255, 0)
	SimpleSeedFill(width, height, scale, 0, -80, 255, 255, 0)
	SimpleSeedFill(width, height, scale, 0, 80, 255, 255, 0)
	SimpleSeedFill(width, height, scale, 80,0 , 255, 255, 0)
	SimpleSeedFill(width, height, scale, -80, 0, 255, 255, 0)
	SimpleSeedFill(width, height, scale, -0, 40, 255, 255, 0)
	SimpleSeedFill(width, height, scale, 0, -40, 255, 255, 0)
	SimpleSeedFill(width, height, scale, 40, 0, 255, 255, 0)
	SimpleSeedFill(width, height, scale, -40, 0, 255, 255, 0)

	print("Finish...")
	glFlush()
	pygame.display.flip()
	 
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

if __name__ == '__main__':
	main()