Meses = ('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
d = int(input("ingresa un numero\n"))
if (d >= 1 and d <= 12):
 print ("El mes " + str(d) + " es " + Meses[d - 1])
else:
 print ("No existe")