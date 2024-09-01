print("bienvenido al sistema")
edad= int(input("introduce tu edad:"))
ingresos = float(input("introduce tus ingresos mensuales"))
if edad >18 and ingresos >=3000000:
    print ("debes tributar")
else:
    print("no debes tributar")