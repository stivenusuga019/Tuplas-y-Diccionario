#Los elemntos de un Dicionario continen una clave y un valor 
"""Ejemplo 
Diccionario={"nombre":"laura", "edad":5,  "sexo":"F"}
               |         |       |   |      |     | 
               v         v       v   v      v     v 
             Clave    valor   Clave valor  Clave    valor  
"""

diccionario={"nombre":"laura",
             "edad":25,
             "sexo":"F"
             }
"""diccionario1 = dict(Nombre= "laura",
                    Edad= 25,
                    Sexo="F"
                    )
diccionario2 = {"Nombre": "Sandra",
                    "telefono": 2554522,
                    "apellido":"Gonzales"
    }"""
#print(diccionario)
#print(diccionario1)

#Acceder a los valores de un Diccionario->get(clave)
"""print(diccionario.get("edad"))

#Modificar un Diccionario
diccionario["edad"]=69
#Si una clave no existe la agrega y si existe la modifica
diccionario["apellido"]="Zapata"
print(diccionario)

#popitem()->Elimina el ultimo elemto
diccionario.popitem()
print(diccionario)"""

#update()
#diccionario1.update(diccionario2)
#print(diccionario1)

#Recorrer un Diccionario Metodo Largo
"""for claves in diccionario:
    print(claves)#Imprime solo las claves"""

"""for valores in diccionario:
   print(diccionario[valores])#Imprime solo los Valores"""

"""for claveF in diccionario:
   print(claveF,diccionario[claveF])"""

#Recorrer un Diccionario Metodo Corto
#keys(): obtener solo claves
"""for claves in diccionario.keys():
    print(claves)"""
#values():obtener solo los valores
"""for valores in diccionario.values():
    print(valores)"""
#items(): obtener claves y valores
"""for claval in diccionario.items():
    print(claval)#Se imprime en forma Tuplas"""

"""for clave, valor in diccionario.items():
    print(clave,valor)#Se imprime en forma lista"""