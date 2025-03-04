# Librerías estándar
import statistics
import math

# Preguntar al usuario cómo quiere ingresar los valores
while True:
	print("\nSeleccione el método de ingreso:")
	print("1. Elegir la cantidad de valores desde el inicio (entre 11 y 20).")
	print("2. Ingresar valores uno a uno hasta alcanzar entre 11 y 20 valores.")
	opcion = input("Ingrese 1 o 2: ")
	6998
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
	n = solicitar_entero("Ingrese la cantidad de valores (entre 11 y 20): ", 11, 20)

	for i in range(n):
		valor = solicitar_entero(f"Ingrese el valor {i+1} (entre 3000 y 15000): ", 3000, 15000)
		valores.append(valor)

# Modo 2: Ingresar valores uno a uno hasta alcanzar entre 11 y 20 valores
else:
	while len(valores) < 20:
		valor = solicitar_entero(f"Ingrese el valor {len(valores)+1} (entre 3000 y 15000): ", 3000, 15000)
		valores.append(valor)

		# Si ya tiene al menos 11 valores, preguntar si quiere continuar o detenerse
		if len(valores) >= 11:
			continuar = input("¿Desea ingresar más valores? (Sí para continuar, cualquier tecla para detenerse): ").strip().lower()
			if continuar != "sí" and continuar != "si":
				break

# Calcular la media y la desviación estándar de los valores
media = statistics.mean(valores)
desviacion_estandar = statistics.stdev(valores)

# Niveles de confianza y valores críticos Z (para 95% y 99%)
z_95 = 1.96
z_99 = 2.58

# Solicitar el margen de error (E)
E = solicitar_entero("Ingrese el margen de error tolerable (valor positivo): ", 1, 1000)

# Calcular el tamaño de la muestra para ambos niveles de confianza
n_95 = (z_95 ** 2 * desviacion_estandar ** 2) / (E ** 2)
n_99 = (z_99 ** 2 * desviacion_estandar ** 2) / (E ** 2)

# Redondear el tamaño de la muestra al entero superior
n_95 = math.ceil(n_95)
n_99 = math.ceil(n_99)

# Mostrar los resultados
print("\nResultados del cálculo:")
print(f"Media de los valores: {media:.2f}")
print(f"Desviación estándar: {desviacion_estandar:.2f}")
print(f"Tamaño de muestra recomendado con 95% de confianza: {n_95}")
print(f"Tamaño de muestra recomendado con 99% de confianza: {n_99}")