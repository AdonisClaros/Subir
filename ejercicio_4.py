# -*- coding: utf-8 -*-

list='La mayoria de los buenos programadores programan no porque esperan que se les pague o por adulacion por parte del publico sino porque es divertido programar';


listado= list.split()

for index, palabra in enumerate(listado):
    print "numero", index, "(", palabra, ")"

    