from PIL import Image, ImageDraw


# funcion para obtener el color popular en un area seleccionada
# image= nombre del archivo
# x0, y0 = coordenadas de donde se quiere emepzar a analizar
# mode = tiene dos modos de discretizacion
# modo 1 hace una cuadricula de 10 x 10
# modo 2 hace una cuadricula de 20 x 20
# antes se uso green pero se cambio a lime ya que es verdaderamente 0,255,0
# si regresa azul, es por que encontro un color que no esta dentro de los parametros
solutionSize=400
def getColors(image, x0, y0, sizeN):
	sizeSqr=int(solutionSize/sizeN)
	arrayW=0
	arrayB=0
	arrayR=0
	arrayG=0
	none=0
	i=0
	im = Image.open(image)
	resizedImg = im.resize((solutionSize,solutionSize))
	rgb_im = resizedImg.convert('RGB')
	for i in range(sizeSqr):
		for j in range (sizeSqr):
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

# funcion para hacer un array de colores random para pruebas

def fillRandomColors():
	colores=[]
	qq=0
	while qq < 100:
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
# sizeN = tamano de la cuadricula
# name = para nombrar el archivo, mas que todo para debug

def outputImage(sizeN,colores,name):
	imgName= name+'.png'
	sizeSqr=int(solutionSize/sizeN)
	counter=0
	blank_image = Image.new('RGB', (solutionSize, solutionSize), 'orange')
	img_draw = ImageDraw.Draw(blank_image)
	for i in range(sizeN):
		for j in range(sizeN):
			counter+=1
			img_draw.rectangle((0+(j*sizeSqr), 0+(i*sizeSqr), sizeSqr+(j*sizeSqr), sizeSqr+(i*sizeSqr)), fill=colores[counter-1], outline='grey')
	blank_image.save(imgName)	

# funcion para verificar que exita una meta y un punto de partida
# se toma el primer valor de partida y el primer valor de meta que
# se haya encontrado en el analisis

def searchSF(array):
	isGreen = False
	isRed = False
	if 'lime' in array:
		isGreen = True
		positionGreen = array.index('lime')
	if 'red' in array:
		isRed = True
		positionRed = array.index('red')
	
	if isGreen == True and isRed == True:
		return isGreen, isRed, positionRed, positionGreen
	else:
		return isGreen, isRed, 0, 0


#funcion que verifica que el espacio donde se encuentra el algoritmo sea la meta

def goalTest(number, array):
	if number > 399:
		number = 0
	if array[number] == 'lime':
		return True
	else:
		return False

def borders(sizeN):
	noUp=[]
	noRight=[]
	noDown=[]
	noLeft=[]
	for i in range(sizeN):
		noLeft.append(i*sizeN)
		noRight.append((sizeN-1)+i*sizeN)

	for i in range(sizeN**2):
		if i < sizeN:
			noUp.append(i)
		if i <= (sizeN**2)-1 and i>= (sizeN**2) - sizeN:
			noDown.append(i)
	return noUp, noRight, noDown, noLeft

#funcion de movimiento que verifica si es posible moverse a un nuevo espacio

def checkSpace(number,array, noMove):
	print(number)
	print(array[number])
	if number in noMove:
		return False
	else:
		if array[number] == 'black':
			return False
		else:
			return True




#funcion de movimiento que verifica el alrededor del punto donde este el algoritmo

def move(number, array, sizeN):
	noU, noR, noD, noL = borders(sizeN)
	sizeSqr=int(solutionSize/sizeN)
	u = number - sizeSqr
	r = number + 1
	d = number + sizeSqr
	l = number - 1
	
	moveUp = checkSpace(u, array, noU)
	moveRight = checkSpace(r, array, noR,)
	moveDown = checkSpace(d, array, noD,)
	moveLeft = checkSpace(l, array, noL)
		
	if d > (sizeN**2)-1:
		d=number
		moveDown=False	
	print(u,r,l,d)
	print (moveUp, moveRight, moveDown, moveLeft)
	if moveUp == False:
		u = number
	if moveRight == False:
		r = number
	if moveLeft == False:
		d = number 
	if moveDown == False:
		l = number
	
	return u,r,d,l

def action(number, array, sizeN):
	noU, noR, noD, noL = borders(sizeN)
	availableMoves=[]
	up, right, down, left = True, True, True, True
	#sizeSqr=int(solutionSize/sizeN)

	if number in noU:
		up = False
		if number in noR:
			right = False
		elif number in noL:
			left = False

	elif number in noR:
		right = False
		if number in noD:
			down = False
		elif number in noU:
			up = False
	
	elif number in noD:
		down = False
		if number in noR:
			right = False
		elif number in noL:
			left = False

	elif number in noL:
		left=False
		if number in noD:
			down = False
		elif number in noU:
			up = False

	return up, right, down, left

def moves(u,r,d,l, array, sizeN):
	up = number - sizeSqr
	right = number + 1
	left = number - 1
	down = number + sizeSqr
		

def BreathFirstSearch(array, locR,sizeN):
	sizeSqr=int(solutionSize/sizeN)
	frontier=[]
	explored=[]
	start=goalTest(locR, array)
	frontier.append(locR)
	cont=0
	# cont < 4 start == False
	while start == False:
		u,r,d,l = action(frontier[0], array, sizeN)
		if u == True:
			up = frontier[0] - sizeSqr
			start=goalTest(up, array)
			print('up= ', str(up))
			if array[up] == 'white':
				if up not in explored:
					frontier.append(up) 
					explored.append(up)

		if r == True:
			right = frontier[0] + 1
			start=goalTest(up, array)
			if array[right] == 'white':
				if right not in explored:
					frontier.append(right)
					explored.append(right)

		if d == True:
			down = frontier[0] + sizeSqr
			start=goalTest(down, array)
			if array[down] == 'white':
				if down not in explored:
					frontier.append(down)
					explored.append(down)

		if l == True:
			left = frontier[0] - 1
			start=goalTest(left, array)
			if array[left] == 'white':
				if left not in explored:
					frontier.append(left)
					explored.append(left)

		for i in range(len(frontier)):
			if frontier[i] not in explored:
				explored.append(frontier[i])

		if len(frontier)>0:
			frontier.pop(0)
			print (frontier)
			#start=goalTest(frontier[0], array)

		if len(frontier)==0:
			start=True

	for i in range(len(explored)):
		space=explored[i]
		array[space]='orange'
	# print (explored)
	# print ('@@')
	# print(frontier)
	return array

def DepthFirstSearch(array, locR,sizeN):
	sizeSqr=int(solutionSize/sizeN)
	frontier=[]
	explored=[]
	start=goalTest(locR, array)
	frontier.append(locR)
	cont=0
	# cont < 4 start == False
	while start == False:
		print(cont)
		u,r,d,l = action(frontier[0], array, sizeN)
		
		if len(frontier)==0:
			start=True


		cont+=1
		if cont > 1000:
			start = True
	print(explored)
	for i in range(len(explored)):
		space=explored[i]
		array[space]='orange'
	# print (explored)
	# print ('@@')
	# print(frontier)
	return array



# funcion que crea una nueva imagen a partir del analisis del mapa
# image=nombre del archivo a analizar
# mode = 1 & 2

def myMaze(image, sizeN):
	colorArray = []
	sqrSize = int(solutionSize/sizeN)
	print(sqrSize)
	for i in range (sizeN):
		for j in range (sizeN):
			color=getColors(image,0+(j*sqrSize),0+(i*sqrSize),sizeN)
			# print (color)
			colorArray.append(color)

	green, red, locR, locG = searchSF(colorArray)
	print(locR, locG)

	if green == True and red == True:
		solutioArray = BreathFirstSearch(colorArray, locR, sizeN)
		colorArray[locR]='red'
		outputImage(sizeN, solutioArray, 'BFS')
		#solutioArray = DepthFirstSearch(colorArray, locR, sizeN)
		colorArray[locR]='red'
		#outputImage(sizeN, solutioArray, 'DFS')
		#a,b,c,d=move(locR,colorArray,sizeN)
		#print(a,b,c,d)
	elif green == False and red == True:
		print("No finish point found")
		outputImage(sizeN, colorArray, 'Output')
	elif green == True and red == False:
		print("No start point found")
		outputImage(sizeN, colorArray, 'Output')
	else:
		print("No other color other than black and white were found on the maze")
		outputImage(sizeN, colorArray, 'Output')


fin='si'
while fin == 'si':
	print('########################')
	print('Parte 1: proyecto 1 IA')
	print('########################')
	imagen=input('Ingrese nombre del laberinto: ')
	print('########################')
	print('         menu')
	print('########################')
	print('1. Solucionar con BFS')
	print('2. Solucionar con DFS')
	print('3. Solucionar con A*')
	print('########################')
	tipo=input('ingrese el numero de la opcion: ')
	if tipo == 1:
		print('########################')
		print('Breadth First Search')
		print('########################')
		myMaze(imagen, 20)
	elif tipo == 2:
		print('########################')
		print('Depth First Search')
		print('########################')
	elif tipo == 3:
		print('########################')
		print('           A*')
		print('########################')
	else:
		print('opcion incorrecta')

#aaa=['white','white','white','white','white','white','white','white','white','white','white','white']
#u,r,d,l=borders(10)
#print(u,r,d,l)
#a,b,c,d=checkSpace(0, aaa, u,r,d,l)
#print (a,b,c,d)
# outputImage(2)
# imageResize('test.bmp')
#www = getColors('Output.png',0,320,1 )
#print (www)