import csv

fh = open('/home/adonis/Documentos/csv/encuesta_espanol.txt')
voto = []
totalvotos = 0

for line in fh:
	votos = line.split(' - ')
	votos = votos [1]
	votos = votos.replace( " ( ", "")
	if voto == votos:
		count +=1
return count
	
print votos
voto.append(votos)
		
