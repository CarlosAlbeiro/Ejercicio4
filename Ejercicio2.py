contador=1
acumulado=0
while contador<=10:
    nota=float(input(f"Ingrese la nota {contador}: "))
    acumulado=acumulado+nota
    contador+=1
total=acumulado/10
print(f"El promedio es de: {total}")

