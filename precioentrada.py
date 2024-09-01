print ("bienvenido al sistema")
edad = int(input("introduzca la edad del cliente:"))
if edad <4:
    print("la entrada es gratis")
elif 4<= edad <= 18:
    print("el precio de la entrada es 5000")
else:
    print ("el precio de la entrada es 10000")