# FUNDAMENTOS DE PROGRAMACION PARA INGENIERÍA
# SECCIÓN DEL CURSO: 0-C-2
# PROFESOR DE TEORÍA: GARY SIMKEN
# PROFESOR DE LABORATORIO: GERY GERENA
#
# AUTOR
# NOMBRE: Benjamín Ándres Zúñiga Jofré
# RUT: 21.337.525-3
# CARRERA: Ingeniería Civil Informatica
# Descripción:


# ENTRADAS
# Cantidad de datos
n = (input('Ingresar la cantidad de datos que se quiere ingresar:'))
while not n.isdigit():
	n = (input('Ingresar la cantidad de datos que se quiere ingresar:'))
n = int(n)
# Datos

tiempos_seg = []

i = 0
print('El tiempo debe ir en minutos, segundos y milisegundos, y el formato debe ser "mm:ss.mss"')
print('""mm" son los minutos, ":" los dos puntos para separar minutos y segundos, "ss" son los segundos y el "." es para separar los segundos de los milisegundos')
print('La cantidad de datos:',n)
while i < n:
    valor = input('Tiempo: ') # Se asume que el usario ingresara los datos de la manera que se le pide
	# Transformar el tiempo de minutos a segundos
    valor = valor.split(':')
    minutos_s = int(valor[0])
    segs = float(valor[1])
    minutos_s = minutos_s*60
    segs_totales = minutos_s + segs
	# Agregar tiempo en la lista de tiempos
    tiempos_seg.append(segs_totales)
    i += 1
# Tiempos para medallas
oro = 347.914
plata = 361.013
bronce = 363.607
# Contador de medallas
o = 0
p = 0
b = 0

# PROCESAMIENTO
# Odenar tiempos
tiempos_seg.sort()
# Contar medallas
i=0
while i < len(tiempos_seg):
	if tiempos_seg[i] < oro:
		o += 1
	elif plata > tiempos_seg[i] and tiempos_seg[i] > oro:
		p += 1
	elif bronce > tiempos_seg[i] and tiempos_seg[i] > plata:
		b += 1
	i +=1


# Salidas
print('Mejor tiempo en segundos:',tiempos_seg[0])
print('Peor tiempo en segundos:',tiempos_seg[n-1])
print('Oro:',o)
print('Plata:',p)
print('Bronce:',b)
print()
# Tiempos ordenados
print('Tiempos ordenados:')
i = 0
while i < len(tiempos_seg):
	min = str(int(tiempos_seg[i]//60))
	seg = str(tiempos_seg[i]%60)
	print(min+':'+seg)
	i+=1




	

