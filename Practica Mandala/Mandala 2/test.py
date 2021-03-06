#Hector Paolo Barazorda Cuellar 145003
#Jerson Salinas Atausinchi 171605
#Ralexs Huallpa Montalvo 145002
#Pamela Aracely Villalobos Quispe 182939
#Noe Franklin Choquenaira Quispe

from grafica import *
def main():
	scale = 3
	width, height = scale * 200, scale * 200

	pygame.init()
	pygame.display.set_caption('C.G. I')

	display_openGL(width, height, scale)
	x = 0
	y = 0
	set_pixel(x, y, 0/255, 0/255, 0/255, scale)


	Circle2v(0, 0, 100, 0/255, 0/255, 0/255, scale)

	DDA(-70, -70, -70, 70, 240/255, 165/255, 0/255, scale)
	DDA(-70, -70, 70, -70, 240/255, 165/255, 0/255, scale)
	DDA(-70, 70, 70, 70, 240/255, 165/255, 0/255, scale)
	DDA(70, -70, 70, 70, 240/255, 165/255, 0/255, scale)

#cuadrado
	DDA(-60, -60, -60, 60, 255/255, 190/255, 15/255, scale)
	DDA(-60, -60, 60, -60, 255/255, 190/255, 15/255, scale)
	DDA(-60, 60, 60, 60, 255/255, 190/255, 15/255, scale)
	DDA(60, -60, 60, 60, 255/255, 190/255, 15/255, scale)

#rombo
	DDA(0, 60, 60, 0, 255/255, 0/255, 0/255, scale)
	DDA(60, 0, 0, -60, 255/255, 0/255, 0/255, scale)
	DDA(0, -60, -60, 0, 255/255, 0/255, 0/255, scale)
	DDA(-60, 0, 0, 60, 255/255, 0/255, 0/255, scale)

	#rombo
	DDA(0, 40, 40, 0, 240/255, 165/255, 0/255, scale)
	DDA(40, 0, 0, -40, 240/255, 165/255, 0/255, scale)
	DDA(0, -40, -40, 0, 240/255, 165/255, 0/255, scale)
	DDA(-40, 0, 0, 40, 240/255, 165/255, 0/255, scale)

	#rombo
	DDA(0, 20, 20, 0, 255/255, 0/255, 0/255, scale)
	DDA(20, 0, 0, -20, 255/255, 0/255, 0/255, scale)
	DDA(0, -20, -20, 0, 255/255, 0/255, 0/255, scale)
	DDA(-20, 0, 0, 20, 255/255, 0/255, 0/255, scale)

	#circulos
	CirclePM(0, 0, 100, 228/255, 137/255, 0/255, scale)
	CirclePM(0, 0, 7, 88/255, 24/255, 69/255, scale)

	#flechas
	DDA(-60, 60, -30, 30, 255/255, 190/255, 15/255, scale)
	DDA(60, 60, 30, 30, 255/255, 190/255, 15/255, scale)
	DDA(-60, -60, -30, -30, 255/255, 190/255, 15/255, scale)
	DDA(60, -60, 30, -30, 255/255, 190/255, 15/255, scale)
	
	#detalles
	DDA(0, 60, 0, 70, 199/255, 0/255, 57/255, scale)
	DDA(60, 0, 70, 0, 199/255, 0/255, 57/255, scale)
	DDA(0, -60, 0, -70, 199/255, 0/255, 57/255, scale)
	DDA(-60, 0, -70, 0, 199/255, 0/255, 57/255, scale)


#cuadrados afuera
	DDA(0, 100, 30, 70, 199/255, 0/255, 57/255, scale)
	DDA(70, 30, 100, 0, 199/255, 0/255, 57/255, scale)
	DDA(100, 0, 70, -30, 199/255, 0/255, 57/255, scale)
	DDA(30, -70, 0, -100, 199/255, 0/255, 57/255, scale)
	DDA(0, -100, -30, -70, 199/255, 0/255, 57/255, scale)
	DDA(0, -100, -30, -70, 199/255, 0/255, 57/255, scale)
	DDA(-70, -30, -100, 0, 199/255, 0/255, 57/255, scale)
	DDA(-100, 0, -70, 30, 199/255, 0/255, 57/255, scale)
	DDA(-30, 70, 0, 100, 199/255, 0/255, 57/255, scale)

	#pruebitas
	DDA(38, 92, 48, 70, 199/255, 0/255, 57/255, scale)
	DDA(83, -20, 90, -38, 199/255, 0/255, 57/255, scale)
	DDA(83, -20, 90, -38, 199/255, 0/255, 57/255, scale)
	DDA(90, -38, 72, -46, 199/255, 0/255, 57/255, scale)
	DDA(90, -38, 72, -46, 199/255, 0/255, 57/255, scale)
	DDA(-17, -83, -39, -92, 199/255, 0/255, 57/255, scale)
	
	DDA(-39, -92, -48, -70, 199/255, 0/255, 57/255, scale)
	DDA(-83, 16, -92, 38, 199/255, 0/255, 57/255, scale)
	DDA(-92, 38, -71, 47, 199/255, 0/255, 57/255, scale)
	DDA(17, 83, 38, 92, 199/255, 0/255, 57/255, scale)


	DDA(-37, 93, -16, 84, 199/255, 0/255, 57/255, scale)
	DDA(71, 47, 93, 38, 199/255, 0/255, 57/255, scale)
	#
	DDA(93, 38, 84, 16, 199/255, 0/255, 57/255, scale)
	DDA(48, -70, 39, -92, 199/255, 0/255, 57/255, scale)
	
	#
	DDA(39, -92, 17, -83, 199/255, 0/255, 57/255, scale)
	DDA(-71, -47, -93, -38, 199/255, 0/255, 57/255, scale)
	#
	DDA(-93, -38, -83, -16, 199/255, 0/255, 57/255, scale)
	DDA(-47, 70, -37, 93, 199/255, 0/255, 57/255, scale)


	vertices = [
		(40, 20), (30, 20), (30, 30), (20, 30), (20, 40), 
		(-20, 40), (-20, 30), (-30, 30), (-30, 20), (-40, 20),
		(-40, -20), (-30, -20), (-30, -30), (-20, -30), (-20, -40),
		(20, -40), (20, -30), (30, -30), (30, -20), (40, -20)
                
	]
	DrawPolygon(vertices, 255/255, 0/255, 0/255, scale)

#relleno de triangulos de la chacana
	vertices = [(-20, 40), (0, 60), (20, 40)]
	verticest = [(-60, 0), (-40, 20), (-40,-20)]
	verticest1 = [(-20,-40), (0, -60), (20, -40)]
	verticest2 = [(40,20), (60,0), (40,-20)]


	FillTriangle(vertices, 255/255, 0/255, 0/255, scale)
	FillTriangle(verticest, 255/255, 0/255, 0/255, scale)
	FillTriangle(verticest1, 255/255, 0/255, 0/255, scale)
	FillTriangle(verticest2, 255/255, 0/255, 0/255, scale)

	#pintado morado
	FillTriangle( [(-30,70),(0,100),(30,70)],7/255, 233/255, 199/255, scale)
	FillTriangle( [(-71,-29),(-100,0),(-71,29)],7/255, 233/255, 199/255, scale)
	FillTriangle( [(-30,-70),(0,-100),(30,-70)],7/255, 233/255, 199/255, scale)
	FillTriangle( [(72,-28),(100,0),(71,29)],7/255, 233/255, 199/255, scale)

	#bordecito del cuadro
	FillTriangle( [(60,-70),(70,70),(70,-70)],7/255, 115/255, 223/255, scale)
	FillTriangle( [(60,-70),(60,70),(70,70)],7/255, 115/255, 223/255, scale)

	vertices2 = [(-70, 70), (60, 60), (70, 70)]
	verticest2 = [(-70, 70), (60, 60), (-60,60)]
	verticest21 = [(-70,-70), (-60, -60), (60, -60)]
	verticest22 = [(-70,-70), (60,-60), (70,-70)]
	FillTriangle(vertices2, 7/255, 115/255, 223/255, scale)
	FillTriangle(verticest2, 7/255, 115/255, 223/255, scale)
	FillTriangle(verticest21, 7/255, 115/255, 223/255, scale)
	FillTriangle(verticest22, 7/255, 115/255, 223/255, scale)

	verticest23 = [(-70,70), (-60, -60), (-60, 60)]
	verticest24 = [(-70,70), (-60,-60), (-70,-70)]
	FillTriangle(verticest23, 7/255, 115/255, 223/255, scale)
	FillTriangle(verticest24, 7/255, 115/255, 223/255, scale)










































	input()

if __name__ == '__main__':
	main()
