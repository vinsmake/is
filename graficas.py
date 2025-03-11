# Importar librerías necesarias
import random
import math
import statistics
import matplotlib.pyplot as plt

# Generar una lista de al menos 50 números aleatorios únicos entre 40 y 300
valores = random.sample(range(40, 301), 50)

# Imprimir los valores generados
print("Valores generados:")
print(valores)

# Calcular la media y la desviación estándar
media = statistics.mean(valores)
desviacion_estandar = statistics.stdev(valores)

# Función de distribución normal
def distribucion_normal(x, media, desviacion_estandar):
	pi = math.pi
	e = math.e
	sigma = desviacion_estandar
	mu = media
	y = (1 / (math.sqrt(2 * pi) * sigma)) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
	return y

# Calcular los valores de la función de distribución normal para cada valor de la lista
y_valores = [distribucion_normal(x, media, desviacion_estandar) for x in valores]

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(valores, y_valores, label='Distribución Normal', color='blue')

# Agregar etiquetas a cada punto con su valor
for i, txt in enumerate(valores):
	plt.annotate(txt, (valores[i], y_valores[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.xlabel('Valores X')
plt.ylabel('Densidad de Probabilidad')
plt.title('Distribución Normal de los Valores Generados')
plt.legend()
plt.show()

# Mostrar la media y la desviación estándar
print(f"\nMedia de los valores: {media:.3f}")
print(f"Desviación estándar de los valores: {desviacion_estandar:.3f}")