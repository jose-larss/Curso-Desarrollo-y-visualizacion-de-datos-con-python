""""
metodo get -> permite obtener la clave por parametro
"""

provincias = dict()

provincias = {
    924 : "Badajoz",
    956:  "Cádiz",
    958 : "Granada",
    959 : "Huelva",
    91 : "Madrid",
    95 : "Málaga",
    968 : "Murcia",
    923 : "Salamanca",
    95 : "Sevilla",
    922 : "Sta. Cruz de Tenerife",
    975 : "Soria",
    96 : "Valencia",
    976 : "Zaragoza"
}
print(provincias)

dato = provincias.get(91)
dato1 = provincias[976]

print(dato1)
print(f"El dato cogido con corchetes se llama: {dato}")

for clave,valor in provincias.items():
    print("Prefijo: ", clave,"Provincia: ",valor)

#############################################3
#recorrer solo las claves y solo los valores

for claves in provincias.keys():
    print("Prefijo: ", claves)


print("----------------------------------------------------------")
for valores in provincias.values():
    print("Provincia: ", valores)
##################################################################33333
provincias.setdefault(925,"Toledo")
print(provincias)
#Si la clave existe no lo insertará
provincias.setdefault(91,"Toledo")
print(provincias)
#########################################################################33
provincias.pop(924)
print(provincias)