# # Area triangulo
# base = float(input('Ingrese la base\n'))
# print('la base es:'+ str(base))
# altura = float(input('Ingrese la altura\n'))
# print('la altura es:' + str(altura))

# area = (base*altura) / 2
# print('El area del triangulo es:'+ str(area))

# # Conversion de dolares a pesos

# vlrDolar = 4023

# dolares = float(input('Ingrese la cantidad de dolares\n'))
# print('La cantidad de dolares es:\n' + str(dolares))

# vlrPesos = dolares * vlrDolar
# print('El valor en pesos colombianos es:\n' + str(vlrPesos))


# # Conversion de Grados Celsius a Fahrenheit

# celsius = float(input('Ingrese grados celsius\n'))
# print('Los grados celsius son:\n' + str(celsius))

# fahrenheit = (celsius * 9)/5 + 32

# print('Equivalen a:'+ ' ' + str(fahrenheit) + '°F')

# # Cantidad de segundos que tiene un Lustro 

# lustro = 5 # Un lustro es un periodo de 5 años.
# lustroSeg = lustro * 365 * 24 * 3600
# print('La cantidad que tiene un lustro es:'+ ' ' + str(lustroSeg) + ' ' +'seg')

# # Viaje de la luz del sol a Marte

# distancia = 227940000 # Distancia que hay del sol a Marte
# velocidadLuz = 300000 # Velocidad de la luz 
# totalVelocidad = distancia / velocidadLuz
# print('La luz viaja del sol a Marte en:' + ' '+ str(totalVelocidad) + ' ' + 'seg')

# # Numero de vueltas Llanta

# pi = 3.1416
# # Para sacar el radio 50 de diametro/2
# radio = 25
# llanta = (2 * pi) * 25
# vueltas = 100000 / llanta # 100000 es la conversion de km a cm
# print('El numero de vueltas queda una llanta son ' + str(vueltas) + ' vueltas')

# # Longitud de la sombra de un edificio

# edificio = 20
# angulo = 22 # tan 22°
# tangente = 0.40402623
# longitud = edificio / tangente
# print('La longitud de la sombra del edificio es de: ' + longitud + ' metros')

# Edad de 2 usuarios es la misma

# edad1 = int(input('Ingrese la edad\n'))
# print('La edad uno es de: ' + str(edad1))
# edad2 = int(input('Ingrese la edad\n'))
# print('La edad dos es de: ' + str(edad2))
# comparacion = edad1 == edad2
# print(comparacion)

# Meses transcurridos de un usuario desde la F/N

# añoActual = int(input('Ingrese el año en el que esta actualmente:\n'))
# añoNac = int(input('Ingrese el año en el que ud nació:\n'))
# añoTotal = añoActual - añoNac
# mesTotal = añoTotal * 12
# print('En este momento ud tiene: ' + str(añoTotal) + ' años' + ' y han transcurrido ' + str(mesTotal) + ' meses desde entonces...')

# Promedio de un alumno

notaEsp = float(input('Ingrese la nota de Español:\n'))
notaMat = float(input('Ingrese la nota de Matemáticas:\n'))
notaEco = float(input('Ingrese la nota de Economía:\n'))
notaPro = float(input('Ingrese la nota de Programación:\n'))
notaIng = float(input('Ingrese la nota de Ingles:\n'))
promedio= notaEsp + notaMat + notaEco + notaPro + notaIng / 5
print('El promedio de las 5 materias es de: ' + str(promedio))



