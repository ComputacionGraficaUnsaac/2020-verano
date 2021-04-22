# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:09:36 2021

@author: Daniel
"""

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
    pygame.time.wait(1)
    glFlush()
def color_pixel(width, height, x, y, size):
    rgb = glReadPixels(width / 2 + x , height / 2 + y, size ,size
    ,
    GL_RGB,
    GL_UNSIGNED_BYTE, None)
    
    return list(rgb)
def DDA(x0, y0, x1, y1, r, g, b, size):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    x = x0
    y = y0
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    if steps>0:
        xi = dx / steps
        yi = dy / steps
    set_pixel(round(x), round(y), r, g, b, size)
    points.append((round(x), round(y)))
    for k in range(steps):
        x += xi
        y += yi
        set_pixel(round(x), round(y), r, g, b, size)
        points.append((round(x), round(y)))
    return points

def drawBressennham(x0, y0, x1, y1, r, g, b, size):
    
#inicializar Vars
    x=x0
    y=y0
#Calcular difs
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
#Manejamos signos
    Sx=np.sign(x1-x0)
    Sy=np.sign(y1-y0)
    if (dy>dx):
        t=dx
        dx=dy
        dy=t
        steps=dx
        flag=1
    else:
        steps=dx
        flag=0
    Pk =2*dy-dx

    set_pixel(x, y, 1, 0, 0, size)
    for i in range(steps):
        while Pk>=0:
            if flag ==1:
                x+=Sx
            else:
                y+=Sy
            Pk=Pk-2*dx
        if flag==1:
            y+=Sy
        else:
            x+=Sx
        Pk+=2*dy
        set_pixel(x, y, r, g, b, size)
    	


def Circle8v(xc, yc, radio, r, g, b, size):
	

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
		drawBressennham(x0, y0, x1, y1, r, g, b, size)
		


def SimpleSeedFill(width, height, size, xi, yi, r, g, b):
	r, g, b = 255 * r, 255 * g, 255 * b
	stack = []
	stack.append((xi, yi))
	while len(stack) > 0:
		x, y = stack.pop()

		if color_pixel(width, height, x, y, size) != [r, g, b]:
			set_pixel(x, y, r/255, g/255, b/255, size)
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

