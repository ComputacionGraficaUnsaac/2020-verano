from Biblioteca import *
import random
def main():
	scale = 1
	angle = -15
	width, height = scale * 500, scale * 500
	pygame.init()
	display_openGL(width, height, scale)
	vertices1 =[[150, 0, 1], [0, 150, 1],[-150, 0, 1]]
	colors = [(0, 255, 255), (0, 128, 0), (0, 255, 0), (128, 0, 128), (255, 255, 0), (255, 0, 0), (0, 0, 255),
				(255, 20, 147), (128, 0, 128), (0, 255, 127)]
	for i in range (1, 20):
		vertices1 = Rotation(vertices1, angle)
		r, g, b  = random.choice(colors)
		#print(r,g,b)
		DrawPolygon(vertices1, r, g, b, scale)


	print("Finish...")
	glFlush()
	pygame.display.flip()
		 
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return


if __name__ == '__main__':
	main()