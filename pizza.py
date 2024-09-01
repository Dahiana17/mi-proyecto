print("bienvenido a la Pizzeria Bella Napoli")
tipo_pizza = input("¿Quieres una pizza vegetariana o no vegetariana?")
if tipo_pizza == "vegetariana":
    ingredientes_disponibles = "1. Pimiento 2. Tofu"
    tipo_pizza_final = "vegetariana"
elif tipo_pizza == "no vegetariana":
    ingredientes_disponibles = "1. Peperoni 2. Jamón 3. Salmón"
    tipo_pizza_final = "no vegetariana"
else:
    ingredientes_disponibles = ""
    tipo_pizza_final = "no válida"
print("Ingredientes disponibles (además de Mozzarella y Tomate):")
print(ingredientes_disponibles)
opcion = int(input("Elige el número del ingrediente adicional que quieres:"))
if tipo_pizza_final == "vegetariana":
    if opcion == 1:
        ingrediente_adicional = "Pimiento"
    elif opcion == 2:
        ingrediente_adicional = "Tofu"
    else:
        ingrediente_adicional = "Opción no válida"
elif tipo_pizza_final == "no vegetariana":
    if opcion == 1:
        ingrediente_adicional = "Peperoni"
    elif opcion == 2:
        ingrediente_adicional = "Jamón"
    elif opcion == 3:
        ingrediente_adicional = "Salmón"
    else:
        ingrediente_adicional = "Opción no válida"
else:
    ingrediente_adicional = "Tipo de pizza no válido"
if tipo_pizza_final != "no válida" and ingrediente_adicional != "Opción no válida":
    print("Has elegido una pizza " + tipo_pizza_final )
    print("Ingredientes: Mozzarella, Tomate, " + ingrediente_adicional)
else:
    print("Selección no válida.")