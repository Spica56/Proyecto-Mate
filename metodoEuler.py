import numpy as np
import matplotlib.pyplot as plt

# Función que evalúa la ecuación diferencial
def f(t, y):
    return t + y

# Función para validar entradas numéricas
def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("El valor debe ser positivo. Intente nuevamente.")
                continue
            return value
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número.")

# Función para validar la elección del método
def input_method():
    while True:
        metodo = input("Ingrese el número del método que desea usar: ")
        if metodo == '1' or metodo == '2':
            return metodo
        else:
            print("Método no válido. Debe ingresar '1' para Euler Simple o '2' para Euler Mejorado (Heun).")

# Función para validar el número de pasos
def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("El número de pasos debe ser un número entero positivo. Intente nuevamente.")
                continue
            return value
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número entero.")

# Mostrar menú
print("Métodos Numéricos para Ecuaciones Diferenciales")
print("Seleccione el método:")
print("1 - Euler Simple")
print("2 - Euler Mejorado (Heun)")

metodo = input_method()

# Datos de entrada del usuario
t0 = input_float("Ingrese el valor inicial de t: ")
y0 = input_float("Ingrese el valor inicial de y: ")
h = input_float("Ingrese el tamaño de paso h: ")
N = input_int("Ingrese el número de pasos: ")

# Inicializar arrays
t = np.zeros(N + 1)
y = np.zeros(N + 1)

# Asignar valores iniciales
t[0] = t0
y[0] = y0

# Solución exacta
def exact_solution(t):
    return np.exp(t) - t - 1  # Solución exacta de y'(t) = t + y(t), con y(0) = 0

# Mostrar la fórmula utilizada y los pasos intermedios
print("\nFórmula utilizada:")
if metodo == '1':
    print("Método de Euler Simple: y_{n+1} = y_n + h * f(t_n, y_n)")
elif metodo == '2':
    print("Método de Euler Mejorado (Heun):")
    print("y_{n+1} = y_n + h / 2 * (f(t_n, y_n) + f(t_{n+1}, y_{predicho}))")

# Iteración según el método
for n in range(N):
    t[n + 1] = t[n] + h

    if metodo == '1':
        # Euler Simple
        print(f"\nPaso {n+1}:")
        print(f"t[{n}] = {t[n]:.4f}, y[{n}] = {y[n]:.6f}")
        print(f"Pendiente en t[{n}]: f(t[{n}], y[{n}]) = {f(t[n], y[n]):.6f}")
        y[n + 1] = y[n] + h * f(t[n], y[n])
        print(f"Nuevo valor de y[{n+1}] = {y[n+1]:.6f}")
    
    elif metodo == '2':
        # Euler Mejorado
        print(f"\nPaso {n+1}:")
        print(f"t[{n}] = {t[n]:.4f}, y[{n}] = {y[n]:.6f}")
        # Predicción de Euler
        y_pred = y[n] + h * f(t[n], y[n])
        print(f"Predicción de y[{n+1}] (Euler): y_pred = y[{n}] + h * f(t[{n}], y[{n}]) = {y_pred:.6f}")
        # Cálculo de la pendiente en el valor predicho
        k1 = f(t[n], y[n])
        k2 = f(t[n] + h, y_pred)
        print(f"Pendientes: k1 = f(t[{n}], y[{n}]) = {k1:.6f}, k2 = f(t[{n}+h], y_pred) = {k2:.6f}")
        y[n + 1] = y[n] + (h / 2) * (k1 + k2)
        print(f"Nuevo valor de y[{n+1}] (Heun): y[{n+1}] = {y[n+1]:.6f}")

# Mostrar resultados en tabla
print("\nResultados:")
print(" t \t\t y (Aproximado) \t y (Exacto) \t Error")
for i in range(N + 1):
    exact_y = exact_solution(t[i])
    error = abs(exact_y - y[i])
    print(f"{t[i]:.4f}\t{y[i]:.6f}\t{exact_y:.6f}\t{error:.6f}")

# Graficar los resultados
t_exact = np.linspace(t0, t[N], 100)
y_exact = exact_solution(t_exact)

plt.plot(t, y, 'bo-', label='Solución Aproximada')
plt.plot(t_exact, y_exact, 'r-', label='Solución Exacta')
plt.xlabel("t")
plt.ylabel("y")
plt.title(f"Comparación de Métodos: {['Euler', 'Heun'][int(metodo)-1]} vs. Solución Exacta")
plt.legend()
plt.grid(True)
plt.show()

