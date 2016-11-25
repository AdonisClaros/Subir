import operator
productos={
0:{'Dulces':[0.05,"bolsa",30]},
1:{'Pan':[0.15,"unidad",50]},
2:{'Leche':[2.50,"galon",10]},
3:{'Queso':[3.0,"libra",10]},
4:{'Frijol':[0.78,"libra",200]},
5:{'Arroz':[0.40,"libra",100]},
6:{'Cereal':[3.40,"caja",100]},
7:{'Jabon':[0.80,"unidad",30]},
8:{'Embutidos':[1.20,"Libra",55]}}

def buscar():
    valor = raw_input("buscar:")
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            if k == valor:
                print k
                print "precio:",v[0]
                print "pos:" ,v[1]
                print "Existencias",v[2]
                
                
        
while True:
    print "Almacen"
    print "1 - Registrar producto"
    print "2 - Eliminar producto"
    print "3 - Modificar inventario"
    print "4 - Vender producto"
    print "5 - Buscar producto"
    print "6 - salir"
    
    opcion = int(raw_input("Seleccione opcion: "))
    
    if opcion == 1:
        
        #lista de los productos y verficacion
            print "listado de productos" , productos
            valor = raw_input("producto existente: ")
            for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == valor:
                        print k
                        print "precio:",v[0]
                        print "pos:" ,v[1]
                        print "Existencias",v[2] 
                        n = int(raw_input("ingrese el id del nuevo producto: "))
                        N = str(raw_input("ingrese nombre del nuevo producto: "))
                        P_d_V = (raw_input("Precio de venta: "))
                        P = str(raw_input("presentacion: "))
                        E = int(raw_input("Existencia: "))
                        nuevo_p=productos[n]={N:[P_d_V,P,E]}
                        o_nuevo_p = sorted(nuevo_p.items(), key=operator.itemgetter(0))
                        print o_nuevo_p
                 
              
    elif opcion == 2:
         
          delete = int(raw_input("ingrese el id del producto que desea eliminar: "))
          del productos[delete]
          print productos
      
    
    elif opcion == 3:
        
        #lista de los productos y verficacion
         print productos
         modi = raw_input("producto a modificar: ")
         for k1 in productos.keys():
                for k, v in productos[k1].iteritems():
                    if k == modi:
                         print k
                         print "precio:",v[0]
                         print "pos:" ,v[1]
                         print "Existencias",v[2]
                         N = int(raw_input("ingrese nuevo id del producto: "))
                         n = str(raw_input("ingrese el nuevo nombre del producto: "))
                         p_d_v = (raw_input("nuevo precio de venta: "))
                         p = str(raw_input("presentacion: "))
                         E = int(raw_input("Existencia: "))
                         nuevo_p = productos[N]={n:[p_d_v,p,E]}
                         o_nuevo_p = sorted(productos.items(), key=operator.itemgetter(0))
                         print o_nuevo_p

    elif opcion == 4:
        
        print "Productos para vender:" , productos
        
        producto_a_vender=raw_input("Digite el nombre del producto: ")
        venta_producto =  int(raw_input("Cantida a vender: "))
        for k1 in productos.keys():
            for k, v in productos[k1].iteritems():
                if k ==  producto_a_vender:
                    existencia = v[2]
                    venta = existencia - venta_producto
                    
                    
                    print "el total que queda del producto es:" ,venta
                
               
        
    elif opcion == 5:
        buscar()     
    elif opcion == 6:
        break                                                                                                                                                                        