import matplotlib.pyplot as plt

# Datos para el gráfico
x1 = [0, 1, 2, 3, 4, 5, 6]
y1 = [0, 10, 30, 60, 100, 150, 210]  # Primera línea con curva creciente más pronunciada

x2 = [0, 1, 2, 3, 4, 5, 6]
y2 = [0, 5, 15, 30, 50, 75, 105]  # Segunda línea con curva creciente menos pronunciada

x3 = [0, 1, 2, 3, 4, 5, 6]
y3 = [0, 2, 6, 12, 20, 30, 42]  # Tercera línea con una curva creciente más moderada

# Crear el gráfico
plt.plot(x1, y1, color='blue', marker='o', linestyle='-')
plt.plot(x2, y2, color='red', marker='o', linestyle='--' )
plt.plot(x3, y3, color='green', marker='o', linestyle='-.')

# Añadir títulos y etiquetas
plt.title('Gráfico con curvas crecientes')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

