#Descuentos de ley
#script hecho por Hector Martinez

print('Bienvenido al Programa descuentos de ley')
#pedir el nombre 
nombre=input("Ingresa tu nombre:")
dui=int(input("Digita tu numero de DUI:"))
nit=int(input("Digite su numero de NIT:"))

#pedir salario 
salario=float(input("Digita tu salario:"))

bono=input("tienes bono? si ó no:")

if bono=="si":
    montodebono=float(input("Digita el monto del bono: "))
    dAFP=salario*7/100
    dISS=salario*3/100
    drenta=salario*10/100
    salariotot=dAFP+dISS+drenta
    salarioDesc = salario-salariotot
    salarioneto = salarioDesc+montodebono
    print("nombre:",nombre,"dui:", dui, "nit:",nit,"tu descuento es de:",salariotot,"tu salario neto es:",salarioneto)
else:
    afp=salario*7/100
    iss=salario*3/100
    renta=salario*10/100
    total=afp+iss+renta
    descuento=salario-total
    print("nombre:",nombre,"dui:", dui, "nit:",nit,"tu descuento es de:",total,"tu salario neto es:",descuento)