# Librerías estándar
import statistics

# Preguntar al usuario cómo quiere ingresar los valores
while True:
	print("\nSeleccione el método de ingreso:")
	print("1. Elegir la cantidad de valores desde el inicio (entre 4 y 15).")
	print("2. Ingresar valores uno a uno hasta alcanzar entre 4 y 15 valores.")
	opcion = input("Ingrese 1 o 2: ")
	
	if opcion in ("1", "2"):
		break
	else:
		print("Error: Opción inválida. Debe ser 1 o 2.")

# Función para solicitar un número en un rango específico (solo enteros)
def solicitar_entero(mensaje, min_val, max_val):
	while True:
		try:
			numero = int(input(mensaje))
			if min_val <= numero <= max_val:
				return numero
			else:
				print(f"Error: El número debe estar entre {min_val} y {max_val}. Intenta de nuevo.")
		except ValueError:
			print("Error: Entrada no válida. Debes ingresar un número entero.")

# Lista para almacenar los valores ingresados
valores = []

# Modo 1: Elegir la cantidad de valores desde el inicio
if opcion == "1":
	n = solicitar_entero("Ingrese la cantidad de valores (entre 4 y 15): ", 4, 15)

	for i in range(n):
		valor = solicitar_entero(f"Ingrese el valor {i+1} (entre 5 y 100): ", 5, 100)
		valores.append(valor)

# Modo 2: Ingresar valores uno a uno hasta alcanzar entre 4 y 15 valores
else:
	while len(valores) < 15:
		valor = solicitar_entero(f"Ingrese el valor {len(valores)+1} (entre 5 y 100): ", 5, 100)
		valores.append(valor)

		# Si ya tiene al menos 4 valores, preguntar si quiere continuar o detenerse
		if len(valores) >= 4:
			continuar = input("¿Desea ingresar más valores? (Sí para continuar, cualquier tecla para detenerse): ").strip().lower()
			if continuar != "sí" and continuar != "si":
				break

# Calcular la desviación estándar de los valores
desviacion_estandar = statistics.stdev(valores)

# Imprimir los resultados
print("\nValores ingresados:", valores)
print(f"La desviación estándar de los valores es: {desviacion_estandar:.2f}")