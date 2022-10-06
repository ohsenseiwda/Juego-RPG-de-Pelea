import os
import random
import time

#Clase personaje
class jugador():
	def __init__ (self,nombre,
	tipo,
	vida,
	ataque,
	elemental,
	defensa,
	velocidad,
	pCritico
	):
		self.nombre=nombre
		self.tipo=tipo
		self.vida=vida
		self.ataque=ataque
		self.elemental=elemental
		self.defensa=defensa
		self.velocidad=velocidad
		self.pCritico=pCritico
		self.vivo=True
		
	def vive(self):
		self.vivo=False
	
	def mostrar(self):
		print("Nombre: ",self.nombre,
					"\nTipo: ",self.tipo,
					"\nVida: ",self.vida)
	
def enemigos(nombre):
	yy=["Fuego","Hielo","Electro","Agua"]
	elemento1=random.choice(yy)
	elemento2=random.choice(yy)
	elemento3=random.choice(yy)
	elemento4=random.choice(yy)
	elemento5=random.choice(yy)

	
	if str(nombre) == "Mago Enigmatico":
		xx=jugador(nombre,str(elemento1),100,15,5,10,10,10)
	elif str(nombre) == "Soldado Real":
		xx=jugador(nombre,str(elemento2),130,20,5,9,15,8)
	elif str(nombre) == "Dragon Volador":
		xx=jugador(nombre,str(elemento3),160,25,5,8,20,6)
	elif str(nombre) == "Lobo Agresivo":
		xx=jugador(nombre,str(elemento4),190,30,5,7,25,4)
	elif str(nombre) == "Jefe Final":
		xx=jugador(nombre,str(elemento5),220,40,5,6,25,15)
	return xx



def attack1(atq1,atq2,num):
	esquivar=random.randrange(1,100)
	golpe=atq2.vida
	resto=atq2.vida
	defensa=atq2.defensa
	if esquivar<=atq2.velocidad:
		if num ==1:
			print("EL ENEMIGO ESQUIVO TU ATAQUE")
		else:
			print("ESQUIVASTE EL ATAQUE ENEMIGO")
	else:
		golpe=atq2.vida-atq1.ataque+defensa
		
		if atq1.tipo=="Fuego" and atq2.tipo=="Hielo":
			golpe+=-atq1.elemental
		elif atq1.tipo=="Fuego" and atq2.tipo=="Agua":
			golpe+=+atq1.elemental
		elif atq1.tipo=="Agua" and atq2.tipo=="Fuego":
			golpe+=-atq1.elemental
		elif atq1.tipo=="Agua" and atq2.tipo=="Electro":
			golpe+=+atq1.elemental
		elif atq1.tipo=="Electro" and atq2.tipo=="Agua":
			golpe+=-atq1.elemental
		elif atq1.tipo=="Electro" and atq2.tipo=="Hielo":
			golpe+=+atq1.elemental
		elif atq1.tipo=="Hielo" and atq2.tipo=="Electro":
			golpe+=-atq1.elemental
		elif atq1.tipo=="Hielo" and atq2.tipo=="Fuego":
			golpe+=+atq1.elemental

		if random.randrange(1,100) < atq1.pCritico:
			golpe+=-atq1.ataque
			print("**GOLPE CRITICO**")
		else:
			print("Golpe Certero ")
			
	print("HIT: "+str(resto-golpe))
	time.sleep(1)
	return golpe


def reset(num):
	os.system('clear')
	pj1.mostrar()
	print()
	print("***VERSUS***")
	print()
	pj2.mostrar()
	print()
	print("<- - - - - - - - - - - - ->")
	if num == 1:
		input("Enter para ATACAR")
	else:
		print(pj2.nombre+" ATACA")
		time.sleep(1)


x=["Mago Enigmatico","Soldado Real","Dragon Volador","Lobo Agresivo","Jefe Final"]

#Seleccion de personaje
nombre_jugador=input("Nombre del Jugador: ")
def elHeroe():
	while True:
		try:
			elemento=int(input("Elige ELEMENTO: \n1) Para Fuego \n2) Para Agua \n3) Para Electro \n4) Para Hielo \n"))
			if elemento == 1:
				pj=jugador(nombre_jugador,"Fuego",150,21,5,10,22,14)
				break
			elif elemento == 2:
				pj=jugador(nombre_jugador,"Agua",150,15,5,11,24,20)
				break
			elif elemento == 3:
				pj=jugador(nombre_jugador,"Electro",150,17,5,8,26,18)
				break
			elif elemento == 4:
				pj=jugador(nombre_jugador,"Hielo",150,19,5,9,20,16)
				break
			os.system('clear')
			print("Elige una opcion correcta!")
		except ValueError:
			os.system('clear')
			print("Elige una opcion correcta!")
	return pj



while True:
	os.system('clear')
	pj1=elHeroe()
	conteoEleccion=0
	for i in x:
		pj2=enemigos(i)
		turno=random.choice([True,False])
		while True:
			if turno == True:
				reset(1)
				pj2.vida=attack1(pj1,pj2,1)
				conteoEleccion+=1
				if conteoEleccion == 5:
					os.system('clear')
					print("Presiona V para recuperar algo de Vida\nPresiona A para aumentar tu Ataque\nPresiona D para Aumentar tu Defensa")
					opciones=str.capitalize(input())
					conteoEleccion=0
					if opciones == "V":
						q=random.randrange(10,60)
						pj1.vida+=q
						print("VIDA EXTRA: "+str(q))
						time.sleep(1)
					elif opciones == "D":
						pj1.defensa+=1
						print("DEFENSA AUMENTA +1")
						time.sleep(1)
					elif opciones == "A":
						pj1.ataque+=1
						print("ATAQUE AUMENTA +1")
						time.sleep(1)
					else:
						print("TOCASTE CUALQUIER COSA, PERDISTE POWER-UP")
						time.sleep(1)
						
						
				turno=False
				if pj2.vida<1:
					print("DERROTASTE A "+pj2.nombre)
					print("ViDA +150")
					pj1.vida+=150
					input()
					break
			else:
				reset(2)
				pj1.vida=attack1(pj2,pj1,2)
				turno=True
				if pj1.vida<1:
					print("PERDISTE!!!")
					input()
					break
		if pj1.vida<1:
			print("VUELVE A INTENTARLO")
			input()
			break






