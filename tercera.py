import matplotlib.pyplot as plt

# Datos para el gráfico
x1 = [10, 20, 30]
y1 = [20, 40, 10]  # Primera línea con pendiente negativa

x2 = [10, 20, 30]
y2 = [40, 10, 30]  # Segunda línea con pendiente positiva

# Crear el gráfico
plt.plot(x1, y1, label='Línea 1', color='blue')
plt.plot(x2, y2, label='Línea 2', color='red')

# Añadir títulos y etiquetas
plt.title('Gráfico en invertida')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()


