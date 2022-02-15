numero=int(input("Ingrese hasta que numero desea ver los numeros impares: "))
numero+=1
for i in range(1,numero):
    if i%2==0:
        print(i-1)