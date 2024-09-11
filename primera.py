import matplotlib.pyplot as plt

# Datos para el gráfico (relación lineal)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]  # y = 2 * x

# Crear el gráfico
plt.plot(x, y)

# Añadir títulos y etiquetas
plt.title('Gráfico de línea recta')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()
