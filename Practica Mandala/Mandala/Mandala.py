# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:17:50 2021

@author: Daniel
"""


from LibGrafica import *

def main():
    run = True
    scale = 1
    width, height = scale * 500, scale * 500
    pygame.init()
    pygame.display.set_caption('MANDALA-DANIEL CARRASCO-VANESSA MENDOZA')
      
    display_openGL(width, height, scale)
	
    xc = 40
    yc = 40
    x2=-40
    y2=40
    x3=-40
    y3=-40
    x4=40
    y4=-40
    #Estrella8puntas
    vertices3=[(0,100),(30,60),(70,70),(60,30),(100,30),(70,0),
               (100,-30),(60,-30),(70,-70),(30,-60),(0,-100),
               (-30,-60),(-70,-70),(-60,-30),(-100,-30),(-70,0),
               (-100,30),(-60,30),(-70,70),(-30,60)]
    #Espigas
    vertices4=[(0,100),(80,185),(70,70),(170,100),(100,30),(200,0),
               (100,-30),(170,-100),(70,-70),(80,-185),(0,-100),
               (-80,-185),(-70,-70),(-170,-100),(-100,-30),(-200,0),
               (-100,30),(-170,100),(-70,70),(-80,185)]
    #otro poligono
    vertices5=[(80,185),(170,100),(200,0),(170,-100),(80,-185),(-80,-185),
               (-170,-100),(-200,0),(-170,100),(-80,185)]
    
    #Mandala
    Circle8v(0,0,215,123/255,0/255,172/255,scale)
    Circle8v(0,0,210,123/255,0/255,172/255,scale)
    
    DrawPolygon(vertices3, 217/255,170/255,246/255, scale)
    drawBressennham(0, 0, 30, 60,  217/255,170/255,246/255, scale)
    drawBressennham(0, 0, 60, 30,  217/255,170/255,246/255, scale)
    drawBressennham(0, 0, 70, 0,  217/255,170/255,246/255, scale)
    drawBressennham(0, 0, 60, -30, 217/255,170/255,246/255, scale)
    drawBressennham(0, 0, 30, -60,  217/255,170/255,246/255, scale)
    drawBressennham(0, 0, -30, 60,  217/255,170/255,246/255, scale)
    drawBressennham(0, 0, -60, 30,  217/255,170/255,246/255, scale)
    drawBressennham(0, 0, -30, -60,  217/255,170/255,246/255, scale)
    drawBressennham(0, 0, -60, -30,  217/255,170/255,246/255, scale)
    drawBressennham(0, 0, -70, 0,  217/255,170/255,246/255, scale)
    Circle8v(0,0,100,217/255,170/255,246/255,scale)
    Circle8v(0,0,102,5/255,244/255,246/255,scale)
    DrawPolygon(vertices4, 5/255,244/255,246/255, scale)
    DrawPolygon(vertices5, 255/255,255/255,0/255, scale)
    
    #Relleno Mandala
    SimpleSeedFill(width, height, scale, xc, yc, 217/255,170/255,246/255)
    SimpleSeedFill(width, height, scale, x2, y2, 217/255,170/255,246/255)
    SimpleSeedFill(width, height, scale, x3, y3, 217/255,170/255,246/255)
    SimpleSeedFill(width, height, scale, x4, y4, 217/255,170/255,246/255)
    SimpleSeedFill(width, height, scale, 80, 0, 217/255,170/255,246/255)
    SimpleSeedFill(width, height, scale, -80, 0, 217/255,170/255,246/255)
    SimpleSeedFill(width, height, scale, 160, 0, 5/255,244/255,246/255)
    SimpleSeedFill(width, height, scale, -160, 0, 5/255,244/255,246/255)
    SimpleSeedFill(width, height, scale, 60,130, 5/255,244/255,246/255)
    SimpleSeedFill(width, height, scale, -60,130, 5/255,244/255,246/255)
    SimpleSeedFill(width, height, scale, 60,-130 ,5/255,244/255,246/255)
    SimpleSeedFill(width, height, scale, -60, -130, 5/255,244/255,246/255)
    SimpleSeedFill(width, height, scale, 212, 0, 123/255,0/255,172/255)
    Circle8v(0,0,30,247/255,0/255,124/255,scale)
    SimpleSeedFill(width, height, scale, 0, 0, 247/255,0/255,124/255)
    drawBressennham(0, 0, 30, 60,  28/255,13/255,2/255, scale)
    drawBressennham(0, 0, 60, 30,  28/255,13/255,2/255, scale)
    drawBressennham(0, 0, 60, -30, 28/255,13/255,2/255, scale)
    drawBressennham(0, 0, 30, -60,  28/255,13/255,2/255, scale)
    drawBressennham(0, 0, -30, 60,  28/255,13/255,2/255, scale)
    drawBressennham(0, 0, -60, 30,  28/255,13/255,2/255, scale)
    drawBressennham(0, 0, -30, -60,  28/255,13/255,2/255, scale)
    drawBressennham(0, 0, -60, -30,  28/255,13/255,2/255, scale)
   
    
    print("Finish...")
    glFlush()
    pygame.display.flip()
    
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run=False
    pygame.quit()
            
if __name__ == '__main__':
	main()