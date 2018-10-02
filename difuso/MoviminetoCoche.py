
xCoche = 0
yCoche = 5

girarDerecha = True


def detector():
	global xCoche
	global girarDerecha
	for y in range(0,5):
		if xCoche + 1 == xObjeto and yCoche == yObjeto + y:
			print("Te has chocado")
			exit()

		elif  yCoche == yObjeto + y:
			print ("Objeto detectado en ", xObjeto,",",yObjeto+y)
			xCoche += 1
			if y % 3 == 1:
				girarDerecha = False
			return True;

	xCoche += 1
	print ("Objeto no detectado")
	return False

def giro():
	x = calcularDistancias()
	global xCoche
	global yCoche

	if girarDerecha:
		if x > 3:
			#xCoche = xCoche + 2
			yCoche = yCoche - 1
			print ("Giro lento derecha")

		elif x <= 3:
			#xCoche = xCoche + 1
			yCoche = yCoche - 3
			print ("Giro rapido derecha")


	else:

		if x > 3:
			#xCoche = xCoche + 2
			yCoche = yCoche + 1
			print ("Giro lento izquierda")

		elif x <= 3:
			#xCoche = xCoche + 1
			yCoche = yCoche + 3
			print ("Giro rapido izquierda")




def calcularDistancias():
	return xObjeto;



while xCoche <= 10:
	xObjeto = input("Introducir valor de X: ")
	xObjeto = int(xObjeto)
	yObjeto = input("Introducir valor de Y: ")
	yObjeto = int(yObjeto)
	if detector():
		giro()

	print ("Coche en ", xCoche,",",yCoche)


