# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 0-C-2
# PROFESOR DE TEORÍA: GARY SIMKEN
# PROFESOR DE LABORATORIO: GERY GERENA
#
# AUTOR
# NOMBRE: Benjamín Zúñiga Jofré
# RUT: 21.337.525-3
# CARRERA: Ingeniería Civil Informática
# DESCRIPCIÓN: Este programa crea los .csv vacios 

# Importaciones
import pandas as pd

# Bloque principal

datos = []
with open('Participantes.csv', 'r', encoding='utf8') as archivo:
    for linea in archivo:
        datos.append(linea)
        datos.pop()
print(datos)






'''
tabla_participantes = pd.read_csv("Participantes.csv",
                                  sep=";")
tabla_participantes = tabla_participantes.sort_values("pais")

tabla_paises = tabla_participantes["pais"]
paises = []

for pais in tabla_paises:
    if pais not in paises:
        paises.append(pais)
        with open("resultados-" + pais + ".csv", "w", encoding="utf8") as arch:
            texto = ''
paises.pop()

i = 0
while i in range(paises):
    a = open("resultados-" + paises[i] + ".csv", "a", encoding="utf8")
    if tabla_participantes[tabla_participantes["pais"] == paises[i]]:
        a.write(str(tabla_participantes["pais"]))
        a.close()
    i += 1

tabla_tiempos = pd.read_csv("Tiempos.csv",
                            sep=";")
tabla_tiempos = tabla_tiempos[tabla_tiempos["vuelta"] == 5]
tabla_tiempos = tabla_tiempos.sort_values("tiempo")
with open("ganadores" + ".csv", "w", encoding="utf8") as arch:
    texto = ""
archivo = open("ganadores" + ".csv", "a", encoding="utf8")
archivo.write(str(tabla_tiempos[0:10]))
archivo.close()
print(tabla_tiempos)
'''