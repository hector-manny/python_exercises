print("Bienvenido al calculo de Semanas, Días, Horas y Segundos \n")

numero = float(input("Ingresa un Numero: \n"))

print("El numero que ingresaste es: \t", numero)


minuto = numero/60
hora = minuto/60
dia = hora/24
semana = dia/7


print("Segundos: ", round(numero, 2))
print("Minutos: ", round(minuto, 2))
print("Horas: ", round(hora, 1))
print("Dias: ", round(dia, 2))
print("Semanas: ", round(semana, 2))
