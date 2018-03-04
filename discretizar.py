from PIL import Image, ImageDraw
import random as rr

# funcion para abrir la imagen y conseguir data del tamano
def imageSize(image):
	im = Image.open(image)
	width, height = im.size
	return width, height


def imageResize(image):
	im = Image.open(image)
	new_image = im.resize((400,400))
	new_image.save('resizedImg.png')


# funcion para obtener el color popular en un area seleccionada
# image= nombre del archivo
# x0, y0 = coordenadas de donde se quiere emepzar a analizar
# mode = tiene dos modos de discretizacion
# modo 1 hace una cuadricula de 10 x 10
# modo 2 hace una cuadricula de 20 x 20
# antes se uso green pero se cambio a lime ya que es verdaderamente 0,255,0

def getColors(image, x0, y0, mode):
	arrayW=0
	arrayB=0
	arrayR=0
	arrayG=0
	none=0
	i=0
	if mode == 1:
		size=40
	elif mode == 2:
		size=20

	im = Image.open(image)
	resizedImg = im.resize((400,400))
	rgb_im = resizedImg.convert('RGB')
	for i in range(size):
		for j in range (size):
			r, g, b =  rgb_im.getpixel((i+x0, j+y0))
			# print(r,g,b)
			if r>=240 and g >= 240 and b >= 240:
				arrayW+=1
			elif r<=50 and g <= 50 and b <= 50:
				arrayB+=1
			elif r==0 and g >= 230 and b <= 50:
				arrayG+=1
			elif r>=230 and g <= 50 and b <= 50:
				arrayR+=1
			else:
				none+=1

	mostPopular=max(arrayW, arrayR, arrayG, arrayB, none)
	if mostPopular == arrayW:
		return "white"
	elif mostPopular == arrayR:
		return "red"
	elif mostPopular == arrayG:
		return "lime"
	elif mostPopular == arrayB:
		return "black"
	else:
		return "blue"

"""
newX, newY = 400, 400

image_file='test.jpg'
Width, Height = imageSize(image_file) 
color = getColors(image_file,0, 0, 200, 200)
print("Color popular: ",color)
"""

# funcion para hacer un array de colores random para pruebas

def fillRandomColors():
	colores=[]
	qq=0
	while qq < 400:
		w = rr.randint(0,3)
		if w == 0:
			colores.append('black')
		elif w == 1:
			colores.append('white')
		elif w == 2:
			colores.append('red')
		else:
			colores.append('lime')
		qq+=1
	return colores

# funcion para sacar imagen de laberinto final
# mode = tipo de cuadricula que se va a imprimir
# 1 = cuadricula de 10 x 10 de 40 px
# 2 = cuadricula de 20 x 20 de 20 px

def outputImage(mode,colores):
	if mode == 1:
		size=40
		nsqr=10
	elif mode == 2:
		size=20
		nsqr=20
	counter=0
	blank_image = Image.new('RGB', (400, 400), 'white')
	img_draw = ImageDraw.Draw(blank_image)
	for i in range(nsqr):
		for j in range(nsqr):
			counter+=1
			img_draw.rectangle((0+(j*size), 0+(i*size), size+(j*size), size+(i*size)), fill=colores[counter-1])
	blank_image.save('Output.png')	



def myMaze(image, mode):
	colorArray = []
	if mode == 1:
		times=10
		size=40
	elif mode == 2:
		times=20
		size=20

	for i in range (times):
		for j in range (times):
			color=getColors(image,0+(i*size),0+(j*size),mode)
			print (color)
			colorArray.append(color)

	outputImage(mode, colorArray)

myMaze('test.bmp', 2)
# outputImage(2)
# imageResize('test.bmp')
#www = getColors('Output.png',0,320,1 )
#print (www)