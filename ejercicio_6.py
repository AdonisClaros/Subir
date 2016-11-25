lista1 = [1,3,4,5,7,8,9,2,5,6,4,12,20,3,7,9,0,1,4,3,8]
repetido = []
unico = []
 
for x in lista1:
	if x not in unico:
		unico.append(x)
	else:
		if x not in repetido:
			repetido.append(x)
print sorted (unico),
print  sorted (repetido, reverse = True),