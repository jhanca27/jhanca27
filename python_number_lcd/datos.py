import numpy
def evaluar(number):
    try:
        tipo = int(number)
        if type(tipo) == int:
            return tipo
    except:
        return  print(number,"no es un numero")

def numero():
    while True:
        val = evaluar(input("ingrese numero: "))
        if type(val)==int:
            return val

def solo_entero():
    while True:
        val = evaluar(input("ingrese numero: "))
        
        if type(val)==int:
            if val>=0 and val<=9:
                return val
            print("valor  no esta dentro del 1 a 9")


class Lcd:
    def __init__(self,datos):
        self.datos = datos        
    
    matriz_cero = numpy.array([['0_0'],
    ['| |'],
    ['|_|']])

    matriz_uno = numpy.array([['0'],
    ['|'],
    ['|']]);

    matriz_dos = numpy.array([['0_0'],
    [' _|'],
    ['|_0']]);

    matriz_tres = numpy.array([['_0'],
    ['_|'],
    ['_|']]); 

    matriz_cuatro = numpy.array([['000'],
    ['|_|'],
    ['  |']]); 

    matriz_cinco = numpy.array([[' _0'],
    ['|_0'],
    ['0_|']]);

    matriz_seis = numpy.array([[' _0'],
    ['|_0'],
    ['|_|']]);

    matriz_siete = numpy.array([['_0'],
    ['0|'],
    ['0|']]);

    matriz_ocho = numpy.array([[' _0'],
    ['|_|'],
    ['|_|']]);

    matriz_nueve = numpy.array([[' _0'],
    ['|_|'],
    ['0_|']]);
    
    def asignar_numero(self):
        matriz_principal = numpy.array([[0],[0],[0]])
        
        for n in self.datos:
            if n == "0":
                matriz_principal = numpy.append(matriz_principal,self.matriz_cero,axis=1)
                
            if n == "1":
                matriz_principal = numpy.append(matriz_principal,self.matriz_uno,axis=1)                
            if n == "2":
                matriz_principal = numpy.append(matriz_principal,self.matriz_dos,axis=1)
            if n == "3":
                matriz_principal = numpy.append(matriz_principal,self.matriz_tres,axis=1)
            if n == "4":
                matriz_principal = numpy.append(matriz_principal,self.matriz_cuatro,axis=1)
            if n == "5":
                matriz_principal = numpy.append(matriz_principal,self.matriz_cinco,axis=1)           
            if n == "6":
                matriz_principal = numpy.append(matriz_principal,self.matriz_seis,axis=1)
            if n == "7":
                matriz_principal = numpy.append(matriz_principal,self.matriz_siete,axis=1)
            if n == "8":
                matriz_principal = numpy.append(matriz_principal,self.matriz_ocho,axis=1)
            if n == "9":
                matriz_principal = numpy.append(matriz_principal,self.matriz_nueve,axis=1)
        
        return matriz_principal

    def imprimir(self,matriz_general):
        union = ""
        filas = numpy.shape(matriz_general)
        
        for i in range(0,filas[0]):
            union += str(matriz_general[i]).strip('[]').replace(",","").replace("'","").replace("0"," ") + "\n"
        return union

    def tamaño(self,numero,largo,ancho):
        for n in self.datos:
            if n == "0":
                largos =['|']
                largo_dos =['|']
                anchos = '_'
                lineas = []
                union = ""
                print(numero)
                for i in range(0,ancho):
                    largos[0] = "0" + largos[0]
                largos[0] = largo_dos[0] + largos[0]
                new_array = numero

                for i in range(0,largo):
                    new_array = numpy.insert(new_array,-1,largos,axis=0)
        
                


                for i in range(0,ancho):
                    lineas += anchos  
                    union += str(lineas[i]).strip('[]').replace(",","")
                tamaño = numpy.shape(new_array)
                filas = tamaño[0]
                val = int(filas/2)   
                new_array[0] = " "+union
                new_array[-1] = " "+union
                new_array = numpy.delete(new_array,-1,1)
                print(new_array)
                "new_array = numpy.delete(new_array,-1,0)"
                return new_array
                

            if n == "1":
                largos =['|']
                new_array = numero
        
                for i in range(0,largo-2):
                    new_array = numpy.insert(new_array,1,largos,axis=0)
                new_array = numpy.delete(new_array,0,1)
                return new_array


            if n == "2":
                largos =['|']
                largo_dos =['|']
                anchos = '_'
                lineas = []
                union = ""

                for i in range(0,ancho+1):
                    largos[0] = "0" + largos[0]
                new_array = numero
        
                for i in range(0,largo):
                    new_array = numpy.insert(new_array,1,largos,axis=0)
                    new_array = numpy.insert(new_array,-1,largo_dos,axis=0)
                new_array = numpy.delete(new_array,0,1)

                   
        
                for i in range(0,ancho):
                    lineas += anchos  
                    union += str(lineas[i]).strip('[]').replace(",","")
                tamaño = numpy.shape(new_array)
                filas = tamaño[0]
                val = int(filas/2)   
                new_array[0] = " "+union
                new_array[val] = " "+union
                new_array[-1] = " "+union
                return new_array
                
            if n == "3":
                largos =['|']
                largo_dos =['|']
                anchos = '_'
                lineas = []
                union = ""

                for i in range(0,ancho+1):
                    largos[0] = "0" + largos[0]
                new_array = numero

                for i in range(0,largo):
                    new_array = numpy.insert(new_array,1,largos,axis=0)
                    new_array = numpy.insert(new_array,-1,largos,axis=0)
                new_array = numpy.delete(new_array,0,1)

                for i in range(0,ancho):
                    lineas += anchos  
                    union += str(lineas[i]).strip('[]').replace(",","")
                tamaño = numpy.shape(new_array)
                filas = tamaño[0]
                val = int(filas/2)   
                new_array[0] = " "+union
                new_array[val] = " "+union
                new_array[-1] = " "+union
                return new_array

            if n == "4":
                largos =['|']
                largo_dos =['|']
                anchos = '_'
                lineas = []
                union = ""

                for i in range(0,ancho):
                    largos[0] = "0" + largos[0]
                largos[0] = largo_dos[0] + largos[0]
                for i in range(0,ancho+1):
                    largo_dos[0] = "0" + largo_dos[0]
                new_array = numero

                for i in range(0,largo):
                    new_array = numpy.insert(new_array,1,largos,axis=0)
                    new_array = numpy.insert(new_array,-1,largo_dos,axis=0)
                new_array = numpy.delete(new_array,0,1)

                for i in range(0,ancho):
                    lineas += anchos  
                    union += str(lineas[i]).strip('[]').replace(",","")
                tamaño = numpy.shape(new_array)
                filas = tamaño[0]
                val = int(filas/2)   
                new_array[val] = " "+union
                new_array[-1] = ""
                "new_array = numpy.delete(new_array,-1,0)"
                return new_array
                
            if n == "5":
                largos =['|']
                largo_dos =['|']
                anchos = '_'
                lineas = []
                union = ""

                for i in range(0,ancho+1):
                    largos[0] = "0" + largos[0]
                new_array = numero
        
                for i in range(0,largo):
                    new_array = numpy.insert(new_array,1,largo_dos,axis=0)
                    new_array = numpy.insert(new_array,-1,largos,axis=0)
                new_array = numpy.delete(new_array,0,1)

                   
        
                for i in range(0,ancho):
                    lineas += anchos  
                    union += str(lineas[i]).strip('[]').replace(",","")
                tamaño = numpy.shape(new_array)
                filas = tamaño[0]
                val = int(filas/2)   
                new_array[0] = " "+union
                new_array[val] = " "+union
                new_array[-1] = " "+union
                return new_array 

            if n == "6":
                largos =['|']
                largo_dos =['|']
                anchos = '_'
                lineas = []
                union = ""

                for i in range(0,ancho):
                    largos[0] = "0" + largos[0]
                largos[0] = largo_dos[0] + largos[0]
                new_array = numero
        
                for i in range(0,largo):
                    new_array = numpy.insert(new_array,1,largo_dos,axis=0)
                    new_array = numpy.insert(new_array,-1,largos,axis=0)
                new_array = numpy.delete(new_array,0,1)                 
        
                for i in range(0,ancho):
                    lineas += anchos  
                    union += str(lineas[i]).strip('[]').replace(",","")
                tamaño = numpy.shape(new_array)
                filas = tamaño[0]
                val = int(filas/2)   
                new_array[0] = " "+union
                new_array[val] = " "+union
                new_array[-1] = " "+union
                return new_array
            
            if n == "7":
                largos =['|']
                largo_dos =['|']
                anchos = '_'
                lineas = []
                union = ""

                for i in range(0,ancho+1):
                    largos[0] = "0" + largos[0]
                new_array = numero
        
                for i in range(0,largo):
                    new_array = numpy.insert(new_array,-1,largos,axis=0)
                new_array = numpy.delete(new_array,0,1)
                new_array = numpy.delete(new_array,1,0)

                   
        
                for i in range(0,ancho):
                    lineas += anchos  
                    union += str(lineas[i]).strip('[]').replace(",","")
                tamaño = numpy.shape(new_array)
                filas = tamaño[0]
                val = int(filas/2)   
                new_array[0] = " "+union
                new_array[-1] = ""
                return new_array
                
            if n == "8":
                largos =['|']
                largo_dos =['|']
                anchos = '_'
                lineas = []
                union = ""

                for i in range(0,ancho):
                    largos[0] = "0" + largos[0]
                largos[0] = largo_dos[0] + largos[0]
                new_array = numero
        
                for i in range(0,largo):
                    new_array = numpy.insert(new_array,1,largos,axis=0)
                    new_array = numpy.insert(new_array,-1,largos,axis=0)
                new_array = numpy.delete(new_array,0,1)                 
        
                for i in range(0,ancho):
                    lineas += anchos  
                    union += str(lineas[i]).strip('[]').replace(",","")
                tamaño = numpy.shape(new_array)
                filas = tamaño[0]
                val = int(filas/2)   
                new_array[0] = " "+union
                new_array[val] = " "+union
                new_array[-1] = " "+union
                return new_array
            if n == "9":
                largos =['|']
                largo_dos =['|']
                anchos = '_'
                lineas = []
                union = ""

                for i in range(0,ancho):
                    largos[0] = "0" + largos[0]
                largos[0] = largo_dos[0] + largos[0]
                for i in range(0,ancho+1):
                    largo_dos[0] = "0" + largo_dos[0]
                new_array = numero
        
                for i in range(0,largo):
                    new_array = numpy.insert(new_array,1,largos,axis=0)
                    new_array = numpy.insert(new_array,-1,largo_dos,axis=0)
                new_array = numpy.delete(new_array,0,1)                 
        
                for i in range(0,ancho):
                    lineas += anchos  
                    union += str(lineas[i]).strip('[]').replace(",","")
                tamaño = numpy.shape(new_array)
                filas = tamaño[0]
                val = int(filas/2)   
                new_array[0] = " "+union
                new_array[val] = " "+union
                new_array[-1] = " "
                return new_array

while True:
    eleccion = input("""selecciona: 
    1: convertir serie de numeros a LCD
    2: Cambia el tamaño de un entero en formato LCD(Entre el 0 y 9)
    0: Salir
    """)
    if eleccion == "1":
        parseo = str(numero()) 
        print(parseo)
        dat = Lcd(parseo)
        print(dat.imprimir(dat.asignar_numero()))
    
    if eleccion == "2":
        parseo = str(solo_entero())
        print("Ingrese largo del número: ")
        largo = numero()
        print("Ingrese el ancho: ")
        ancho = numero()
        dat = Lcd(parseo)
        print(dat.imprimir(dat.tamaño(dat.asignar_numero(),largo,ancho)))
    
    if eleccion == "0":
        print("Hasta luego")
        break

    if eleccion != "1" and eleccion != "2" and eleccion != "0":
        print("Eleccion incorrecta, intentalo de nuevo")











        
        
        
            


        
"dat = Lcd(parseo)"
"print(dat.imprimir(dat.asignar_numero()))"
"print(dat.imprimir(dat.tamaño(dat.asignar_numero(),3,3)))"



                
                




