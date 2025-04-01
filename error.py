# Librerías estándar
import math

# Solicitar coeficientes de la ecuación de regresión (y' = a + b * x)
def solicitar_flotante(mensaje):
	while True:
		try:
			return float(input(mensaje))
		except ValueError:
			print("Error: Debe ingresar un número válido.")

print("Cálculo del error estándar de estimación (Sy.x)")
print("Ecuación de regresión: y' = a + b * x")

a = solicitar_flotante("Ingrese el valor de a: ")
b = solicitar_flotante("Ingrese el valor de b: ")

# Lista para almacenar tuplas de (x, y)
datos = []

# Ingreso de valores uno por uno
print("\nIngrese los pares de datos (x: LDC, y: Esfuerzo real).")
print("Escriba 'fin' en cualquier momento para terminar (mínimo 3 registros).\n")

while True:
	try:
		x_input = input("Ingrese x (LDC): ")
		if x_input.lower() == 'fin':
			break
		x = float(x_input)

		y_input = input("Ingrese y (Esfuerzo real): ")
		if y_input.lower() == 'fin':
			break
		y = float(y_input)

		datos.append((x, y))
	except ValueError:
		print("Error: Debe ingresar valores numéricos válidos.")

	if len(datos) >= 3:
		continuar = input("¿Desea ingresar otro par? (sí para continuar, otra tecla para terminar): ").strip().lower()
		if continuar != "sí" and continuar != "si":
			break

# Verificar cantidad de datos
n = len(datos)
if n < 3:
	print("Error: Se requieren al menos 3 registros para calcular Sy.x.")
	exit()

# Calcular y' y los errores
suma_errores_cuadrados = 0

print("\nDatos procesados:")
print(f"{'x':>6} {'y':>6} {'y\'':>10} {'y - y\'':>10} {'(y - y\')²':>15}")
for x, y in datos:
	y_estimado = a + b * x
	diferencia = y - y_estimado
	cuadrado = diferencia ** 2
	suma_errores_cuadrados += cuadrado
	print(f"{x:6.2f} {y:6.2f} {y_estimado:10.2f} {diferencia:10.2f} {cuadrado:15.2f}")

# Cálculo del error estándar de estimación
syx = math.sqrt(suma_errores_cuadrados / (n - 2))

# Mostrar resultados
# Mostrar resultados
print(f"\nSuma de errores al cuadrado: {suma_errores_cuadrados:.2f}")
print(f"División: {suma_errores_cuadrados:.2f} / ({n} - 2) = {suma_errores_cuadrados / (n - 2):.2f}")
print(f"Error estándar de estimación (Sy.x): {syx:.2f}")

