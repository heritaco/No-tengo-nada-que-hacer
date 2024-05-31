import numpy as np
from scipy.optimize import minimize

# Definir la función del área en términos de theta
def area(theta):
    # Las variables del problema
    b1 = 1  # base menor
    a = 1   # longitud de los lados
    b2 = b1 + 2 * a * np.cos(theta)  # base mayor
    h = a * np.sin(theta)            # altura
    
    # Función del área del trapecio
    A = 0.5 * (b1 + b2) * h
    # Queremos maximizar el área, por lo que devolvemos el negativo del área
    return -A

# Punto inicial pa  ra theta
theta_initial = np.pi / 4

# Encontrar el ángulo que maximiza el área
result = minimize(area, theta_initial, bounds=[(0, np.pi)])

# Obtener el ángulo óptimo y el área máxima
theta_optimal = result.x[0]
area_maxima = -result.fun

print(f"Ángulo óptimo (radianes): {theta_optimal}")
print(f"Área máxima del trapecio: {area_maxima}")
