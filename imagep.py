from PIL import Image
import random as rr

def openImage(image):
	im = Image.open(image)
	width, height = im.size
	print (width)
	print (height)

	return im, width, height

def searchColor(image, width, height):
	isRed, isGreen = False, False
	rgb_im = image.convert('RGB')
	print (width, height)
	i=0
	while (i < 10000):
		print (i)
		x = rr.randint(0, width-1)
		y = rr.randint(0, height-1)
		print (x, y)
		r, g, b = rgb_im.getpixel((x, y))
		print (r,g,b)
		if r==0 and g == 255 and b == 0:
			isGreen=True
			gx, gy = x, y
			print ("@@@@@@@@@@@@@@@@")

		if r<=255 and r>=240 and g == 0 and b == 0:
			isRed=True
			rx, ry = x, y
			print ("############")

		if isGreen == True and isRed == True:
			i=i+10000000
		i=i+1


	if isRed == True and isGreen == True:
		print ("Green: " + str(gx) +', '+ str(gy))
		print("Red: "+ str(rx) +', '+ str(ry))
	if isRed == False and isGreen == True:
		print ("No Red Found")
	if isRed == True and isGreen == False:
		print ("No Green Found")



Maze, Width, Height=openImage('test.jpg')
searchColor(Maze, Width, Height)