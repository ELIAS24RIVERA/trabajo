import matplotlib.pyplot as plt

# Datos para el gráfico
x1 = [1, 2, 3]
y1 = [2, 4, 6]  # Primera línea con pendiente positiva

x2 = [3, 4, 5]
y2 = [6, 4, 2]  # Segunda línea con pendiente negativa


# Crear el gráfico
plt.plot(x1, y1, label='Línea 1', color='blue')
plt.plot(x2, y2, label='Línea 2', color='blue')

# Añadir títulos y etiquetas
plt.title('Gráfico en forma de V')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
