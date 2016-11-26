import csv
import numpy as np
import matplotlib.pyplot as plt

print "Menu"


def count_votes(resultados):
	print ("Numero de votos para " + resultados + ":")
	count = 0
	for line in open('/home/adonis/Documentos/csv/encuesta_espanol.txt'):
		line = line.strip()
		nombre, voto = line.split(" - ")
		if voto == resultados:
			count = count + 1
	return count
	
def grafica(resultados):
	print ("la grafica para " + resultados + ":")
	count = 0
	for line in open('/home/adonis/Documentos/csv/encuesta_espanol.txt'):
		line = line.strip()
		nombre, voto = line.split(" - ")
		if voto == resultados:
			count = count + 1
	return count
				
while True:

    print "1- Votos Vegetales"
    print "2- Votos frutas"
    print "3- Votos general"
    print "4- Ver votos especificos"
    print "5- Grafica"
    print "6- Grafica 2"
    print "7- Salir"


    elegir=int(raw_input("Ingrese opcion: "))
    
    if elegir == 1:
		print(count_votes("Pepinos"))
		print(count_votes("Papas"))
		print(count_votes("Rabano"))
		print(count_votes ("Lechuga"))
		print(count_votes ("Brocoli"))
		print(count_votes ("Frijoles"))
		print(count_votes ("Tomates"))
             

    elif elegir == 2:
		print(count_votes ("Fresas"))
		print(count_votes ("Aguacate"))
		print(count_votes ("Kiwi"))
		print(count_votes ("Sandia"))
		
    elif elegir == 3:
			print(count_votes ("Fresas"))
			print(count_votes("Pepinos"))
			print(count_votes("Papas"))
			print(count_votes("Rabano"))		
			print(count_votes ("Aguacate"))
			print(count_votes ("Kiwi"))
			print(count_votes ("Lechuga"))
			print(count_votes ("Sandia"))
			print(count_votes ("Brocoli"))
			print(count_votes ("Frijoles"))
			print(count_votes ("Tomates"))
			
		
    elif elegir == 4:
		veg_fru = "Fresas", "Pepinos", "Papas", "Rabano","Aguacate","Kiwi","Lechuga","Sandia","Brocoli","Frijoles","Tomates"
		print "el listado de frutas y verduras disponibles es: " , veg_fru 
		resultados = raw_input("Ingrese el nombre de fruta disponible: ") 
		print (count_votes (resultados))
		
    elif elegir == 5:
		
		
		veg_fru = ("Fresas" , "Pepinos", "Papas", "Rabano","Aguacate","Kiwi","Lechuga","Sandia","Brocoli","Frijoles","Tomates")
		posicion_y = np.arange(len(veg_fru))
		votos = (55, 76, 72, 61, 72, 72, 63, 64, 55, 54, 55)
		plt.barh(posicion_y, votos, align = "center")
		plt.yticks(posicion_y, veg_fru)
		plt.xlabel('Votos')
		plt.title("Vegetales y Frutas")
		plt.show()
		
		
    elif elegir == 6:
		N = 11
		print "\n","Preparando estadisticas......" , "\n"
		menMeans = (72, 55, 72, 54, 63, 72, 76, 61, 55, 55, 64)
		menStd =  (8)
		ind = np.arange(N)
		width = 0.35
		fig, ax = plt.subplots()
		rects1 = ax.bar(ind, menMeans, width, color='k', yerr=menStd)
		
		ax.set_ylabel('Numero de votos')
		ax.set_title('Estadisticas de la Encuesta sobre Frutas y Vegetales')
		ax.set_xticks(ind + width)
		ax.set_xticklabels(('Aguacate', 'Fresas', 'Kiwi', 'Frijoles', 'Lechuga','Papas','Pepinos','Rabano','Tomates','Brocoli', 'Sandia'))
		
		def autolabel(rects):
			for rect in rects:
				height = rect.get_height()
				ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
				'%d' % int(height),
				ha='center', va='bottom')
				
		autolabel(rects1)
		plt.show()
		
		print "\n"
    elif elegir == 7:
		break
		


