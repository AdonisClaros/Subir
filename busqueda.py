#busqueda de forma lineal#
for line in open('/home/adonis/Documentos/csv/borrowers_test.csv'):
			linea = line.split(',')
			N_Carrera = linea[1]
			L = [N_Carrera]
			print L
			x = 'Luis Arnol'
def linearSearch(L,x):
	for e in L:
		if e == x.upper() or e == x.lower():
			return True
	return False
print linearSearch(L,x)

#busqueda Secuencial#
'''lista = ['1','334','JUAN PEREZ','45','12','784','35','21','31','Ludwin']
buscar = 'juan perez'

posicion = 0
encontrado = False
posicion_valor_buscar = 0

for posicion in range(len(lista)):
	if lista[posicion]==buscar.lower() or lista[posicion]==buscar.upper():
		posicion_valor_buscar=posicion
		encontrado=True
	posicion=posicion+1
if encontrado==True:
	print 'Valor '  + buscar + ' encontrado en posicion',posicion_valor_buscar
else:
	print 'Valor no encontrado'	'''
	
#busqueda Binaria#
'''lista = [1,2,3,4,5,6,7,8]
encontrado=False
buscar=7
minimo=0
maximo=len(lista)-1
centro=0
posicion=0
while minimo <= maximo and not encontrado:
	centro=(minimo+maximo) // 2
	if lista[centro]==buscar:
		encontrado=True
		posicion=centro
	elif lista[centro] < buscar:
		minimo=centro+1
	else:
		maximo=centro-1
print 'valor ' +str(buscar)+' en la posicion: '+str(posicion)'''
