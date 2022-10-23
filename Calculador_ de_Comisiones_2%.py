nombre = input("Tu nombre es: ")
ventas = int(input("En total vendiste: "))

ventas = round(ventas*0.2/100, 2)
print(f"El empleado {nombre} a comisionado ${ventas}")
