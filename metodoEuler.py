import numpy as np
import matplotlib.pyplot as plt

# Función que evalua la ecuación diferencial
def f(t, y):
    return t + y


# Mostrar menú
print("Métodos Numéricos para Ecuaciones Diferenciales")
print("Seleccione el método:")
print("1 - Euler Simple")
print("2 - Euler Mejorado (Heun)")

metodo = input("Ingrese el número del método que desea usar: ")

# Datos de entrada del usuario
t0 = float(input("Ingrese el valor inicial de t: "))
y0 = float(input("Ingrese el valor inicial de y: "))
h = float(input("Ingrese el tamaño de paso h: "))
N = int(input("Ingrese el número de pasos: "))

# Inicializar arrays
t = np.zeros(N + 1)
y = np.zeros(N + 1)

# Asignar valores iniciales
t[0] = t0
y[0] = y0

# Iteración según el método
for n in range(N):
    t[n + 1] = t[n] + h

    if metodo == '1':
        # Euler Simple
        y[n + 1] = y[n] + h * f(t[n], y[n])

    elif metodo == '2':
        # Euler Mejorado
        k1 = f(t[n], y[n])
        y_pred = y[n] + h * k1
        k2 = f(t[n] + h, y_pred)
        y[n + 1] = y[n] + h / 2 * (k1 + k2)

    else:
        print("Método no válido. Terminando el programa.")
        exit()

print("\nResultados:")
print(" t \t\t y")
for i in range(N + 1):
    print(f"{t[i]:.4f}\t{y[i]:.6f}")

plt.plot(t, y, 'bo-', label='Solución aproximada')
plt.xlabel("t")
plt.ylabel("y")
plt.title("Método Numérico")
plt.legend()
plt.grid(True)
plt.show()
