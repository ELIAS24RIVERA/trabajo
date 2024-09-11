import matplotlib.pyplot as plt

# Datos para el gráfico
x1 = [1, 4, 5, 6, 7]
y1 = [2, 6, 3, 6, 3]  # Primera línea con pendiente negativa

# Crear el gráfico
plt.plot(x1, y1, color='blue', marker='o', linestyle='dotted')

# Añadir títulos y etiquetas
plt.title('Gráfico de lineas intersectadas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')


# Mostrar el gráfico 1, 4, 5, 6, 7
plt.grid(True)
plt.show()