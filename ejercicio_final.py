class Aguinaldo:
    
    "clase que define al empleado"
    
    nombre = ""
    dui = ""
    nit = ""
    sueldo = 0.0
    tiempo = 0

    "construcctor"
    def _init_(self, nombre, dui, nit, sueldo,tiempo):
        self.nombre = nombre
        self.dui = dui
        self.nit = nit
        self.sueldo = sueldo
        self.tiempo = tiempo
        
        "get y set"
        
    def getNombre(self):
        return self.nombre
    
    def getNombre(self,nuevoNombre):
      self.nombre = nuevoNombre
    
    def getDui(self):
        return self.dui
    
    def getNit(self):
        return self.nit
    
    def getNit(self, nuevoNit):
       self.nombre = nuevoNit
    
    def getSueldo(self):
        return self.sueldo
    
    def getSueldo(self, nuevoSueldo):
        self.sueldo = nuevoSueldo
        
    def getTiempo(self):
        return self.tiempo
    
    def getTiempo(self, nuevoTiempo):
        self.tiempo = nuevoTiempo
        
"metodos"

def calcularAguinaldo(sueldo, tiempo):
    calcularAguinaldo = 0.0
    if tiempo >= 12 and tiempo <= 36:
        if sueldo <= 300:
            calculo = sueldo / 30
            calcularAguinaldo = calculo * 15
            return calcularAguinaldo
    elif tiempo > 36 and tiempo <= 120:
        calculo = sueldo / 30
        calcularAguinaldo = calculo * 19
        return calcularAguinaldo
    elif tiempo > 120:
        calculo = sueldo / 30
        calcularAguinaldo = calculo * 21
        return calcularAguinaldo
    else:
        return calcularAguinaldo
    

"trabajando con la consola"

aguinaldo = None
print("*****************************\n")
print("**** calculo de aguinaldo ****\n")
print("*****************************")
nombre = input("Ingrese su Nombre: \n")
dui = input("ingrese su DUI - sin guiones \n")
while (len(dui) != 9):
    print("DUI INVALIDO")
    dui = input("ingrese su DUI - sin guiones: \n")
else:
    dui = dui[:-1] + "-" + dui[-1]
#pedimos el nit

nit = input("ingrese su numero de nit - sin guiones: \n")
while (len(nit) !=14):
    print("NIT invalido")
    nit = input("ingrese su numero de nit -sin guiones: \n")
else:
    nit = nit[:4] + "-" + nit[4:10] + "-" + nit[10:13] + nit[-1]
sueldo = float(input("Ingrese su sueldo: \n"))
tiempo = int(input("Ingrese su tienpo en meses que esta ens su trabajo: \n"))
bono = calcularAguinaldo(sueldo,tiempo)
print("\n\n\n")
aguinaldo = Aguinaldo()
aguinaldo.setNombre(nombre)
aguinaldo.setDui(dui)
aguinaldo.setNit(nit)
aguinaldo.setSueldo(sueldo)
aguinaldo.setTiempo(tiempo)


"impresion de ticket"

print("***********************************************\n")
print("************ BOLETA ELECTRONICA ***************\n")
print("***********************************************\n")
print("Nombre " +aguinaldo.getNombre()+ "\n")
print("Dui" +aguinaldo.getDui()+ "\n")
print("Nit" +aguinaldo.getNit()+ "\n")
print("Sueldo" + str(aguinaldo.getSueldo())+ "\n")
print("Tiempo en meses" +str(aguinaldo.getTiempo()) + "\n")
print("Aguinaldo asignado" + str(bono) + "\n")
    
            
    