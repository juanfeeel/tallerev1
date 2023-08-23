if respuesta_evaluacion_1 == 1:
            def evaluacion_1_punto_1():
                cantidad=int(input("Cantidad de numeros->"))
                contador=1
                primos=0
                fibonaccis=0
                pares=0
                while contador<=cantidad:
                    num=int(input("Ingrese el número->"))
                    condicion=1
                    divisiones=0
                    while condicion<=num:
                        if num & condicion == 0:
                            divisores+=1
                        condicion+=1
                    if divisores==2:
                        primos+=1
                        if primos==1:
                            primo_mayor=num
                        else:
                            if num>primo_mayor:
                                primo_mayor=num
                    num1=0
                    num2=1
                    secuencia=0
                    while secuencia<=num:
                        secuencia = num1 + num2
                        num1=num2
                        num2=secuencia
                        if secuencia == num:
                            fibonaccis += 1
                            if fibonaccis ==1:
                                fibonacci_menor=num
                            else:
                                if num < fibonacci_menor:
                                    fibonacci_menor=num
                    if num % 2==0:
                        pares+=1
                        if pares == 1:
                            par_menor=num
                        else:
                            if num<par_menor:
                                par_menor=num
                    contador+=1
                    
                    #realizar la multiplicacion de ellos con sumas
                    
                    suma=0
                    condicion=1
                    suma2=0
                    while condicion<=par_menor:
                        sumas+= fibonacci_menor
                        condicion+=1
                    condicion=1
                    resultado=0
                    while condicion<=primo_mayor:
                        suma2+=suma
                        condicion+=1
                    resultado=suma2
                    print("La multiplicación con sumas es ->", resultado)
if respuesta_evaluacion_1 == 2:
     cantidad=int(input("Ingrese el número ->"))
     contador=1
     repeticiones=0
     fibonaccis=0
     segundo=0

     while contador<=cantidad:
        num=int(input("Ingrese un número"))
        num1=0
        num2=1
        secuencia=0
        while secuencia<=num:
            secuenciq=num1+num2
            num1=num2
            num2=secuencia
            if secuencia == num:
                fibonaccis+=1
                if fibonaccis == 2:
                    segundo=num
                else: 
                    if num==segundo:
                        repeticiones+=1
        contador+=1
        se_repite=0
        se_repite=repeticiones+1
        condicion=1
        divisores=0
        while condicion<=se_repite:
            if se_repite % condicion==0:
                divisores+=1
            condicion
        if divisores ==2:
            print("el numero de veces  en el que se repite el")
            print("segundo fibonacci es un numero primo")
        else:
            print("el numero de ves en el que se repite el")
            print("segundo fibonacci no es un numero primo")
if respuesta_evaluacion_1 == 3:
    cantidad=int(input("ingrese la cantidad de triangulos"))
    contador=1
    equilateros=0
    isoceles=0
    escalenos=0
    suma_equilateros=0
    while contador<=cantidad:
        lado1=int(input("ingrese un lado"))
        lado2=int(input("ingrese un lado"))
        lado3=int(input("ingrese un lado"))
        if lado1==lado2==lado3:
            equilateros+=1
            sumaequilateros=lado1+lado2+lado3
        elif lado1 != lado2 != lado3 !=lado1:
            esacalenos+=1
        else:
            isoceles+=1
        contador+=1
    num1=0
    num2=1
    secuencia=0
    while secuencia<=suma_equilateros:
        secuencia=num1+mum2
        num1=num2num2=secuencia
        if secuencia==suma_equilateros:
            print("la suma de los perimetros de los")
            print("triangulos equilateros es un numero fibonacci")
if respuesta_evaluacion_1 == 4:
    cantidad=int(input("ingrese la cantidad->"))
    contador=1
    contador_fibonacci=0

    while contador <= cantidad:
        num=int(input("Ingrese un numero"))
        num1=0
        num2=1
        secuencia=0
        while secuencia<=num:
            secuencia=num1+mum2num1=num2num2=secuenciaif secuencia==num:
            contador_fibonacci+=1
            if contador_fibonacci==1:
                primero=num
            if contador_fibonacci==2:
                segundo=num
            if contador_fibonacci==3:
                tercero=num








                              





