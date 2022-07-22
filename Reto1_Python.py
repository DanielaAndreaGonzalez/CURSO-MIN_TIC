
def solucion(edad, peso):
#ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    edad= int(input("Indicar la edad del paciente: "))
    peso = float(input("Indicar el peso del paciente en kilogramos: "))

    estadoNutricional=""
    porcionCarbohidratos = (60.1 /1000)
    porcionProteinas =  (30.5 / 1000)
    porcionVerduras = (-24.4/1000)
    calculo = 0
    dias =0
    alcance = " "
    pesoObjetivo = 0
    pesoMaximo =0


#Proceso 
    if (edad >= 5 and edad <=10): 
        if (peso < 16):
            estadoNutricional = "A"
            calculo = (porcionCarbohidratos * 2) + porcionProteinas + (porcionVerduras*2)
            alcance = "un peso saludable"
            pesoObjetivo = 22 

        elif (peso > 28):
            estadoNutricional = "B"
            calculo = (porcionCarbohidratos * 0.6) + (porcionVerduras *4) +porcionProteinas
            alcance = "un peso saludable"
            pesoObjetivo = 24

        elif (not peso <16 and not peso > 28):
            estadoNutricional = "C"
            calculo = (porcionCarbohidratos * 0.5) + (porcionProteinas* 0.7) + (porcionVerduras *2) 
            alcance = "el peso maximo"
            pesoMaximo = 28

    elif (edad >10 and edad <=13): 
    
        if peso <30 :
            estadoNutricional = "A"
            calculo = (porcionCarbohidratos * 2) + porcionProteinas + (porcionVerduras*2)
            alcance = "un peso saludable"
            pesoObjetivo = 32

        elif (peso >50 ):
            estadoNutricional = "B"
            calculo = (porcionCarbohidratos * 0.6) + (porcionVerduras *4) +porcionProteinas
            alcance = "un peso saludable"
            pesoObjetivo = 43

        elif (not peso < 30 and not peso > 50):
            estadoNutricional = "C"
            calculo = (porcionCarbohidratos * 0.5) + (porcionProteinas* 0.7) + (porcionVerduras *2) 
            alcance = "el peso maximo"
            pesoMaximo = 50

    elif (edad >13 and edad <= 17 ):

        if(peso <51):
            estadoNutricional = "A"
            calculo = (porcionCarbohidratos * 2) + porcionProteinas + (porcionVerduras*2)
            alcance = "un peso saludable"
            pesoObjetivo = 56

        elif ( peso > 63):
            estadoNutricional = "B"
            calculo = (porcionCarbohidratos * 0.6) + (porcionVerduras *4) +porcionProteinas
            alcance = "un peso saludable"
            pesoObjetivo = 58

        elif (not peso <51 and not peso > 63)  :
            estadoNutricional = "C"
            calculo = (porcionCarbohidratos * 0.5) + (porcionProteinas* 0.7) + (porcionVerduras *2) 
            alcance = "el peso maximo"
            pesoMaximo = 63

    if estadoNutricional == "A":
        pesoFinal = peso 
        while pesoFinal < pesoObjetivo:
                pesoFinal +=calculo
                dias +=1

    if estadoNutricional == "B":
        pesoFinal = peso 
        while pesoFinal > pesoObjetivo:
                pesoFinal +=calculo
                dias +=1

    if estadoNutricional == "C":
        pesoFinal = peso 
        while pesoFinal < pesoMaximo:
                pesoFinal +=calculo
                dias +=1
                
    print(f"El estado nutricional del paciente es {estadoNutricional} y se requieren {dias} dias de dieta para que alcance {alcance}")
