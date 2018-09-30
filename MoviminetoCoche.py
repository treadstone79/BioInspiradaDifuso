import random


xCoche = 0
yCoche = 5




def detector():

	for x in range(0,5):
		if  yCoche == (yObjeto + x):
			print ("Objeto detectado en ", xObjeto,",",yObjeto+x)
			return True;
	print ("Objeto no detectado")
	return False

def giro():
	x=calcularDistancias()
	if x>3: #giro lento
		xCoche+=2
		yCoche+=1
		print ("Giro lento izquierda")

	if x<=3: #giro rapido
		xCoche+=1
		yCoche+=3
		print ("Giro rapido izquierda")



def calcularDistancias():
	return xObjeto;
while(xCoche <= 10):
	xObjeto = input("Introducir valor de X: ")
	yObjeto = input("Introducir valor de Y: ")
	if detector:
		giro
	xCoche += 1
	print ("Coche en ", xCoche,",",yCoche)


