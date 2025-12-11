import numpy as np
import matplotlib.pyplot as plt
import math

# Configuración de gráficas
plt.style.use('default')
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

# =============================================================================
# TABLA 1: Partícula con masa 4m - MAS (coseno)
# =============================================================================
t1 = np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000])
x1 = np.array([1.000, 0.951, 0.809, 0.588, 0.309, 0.000])
A1 = 1.000

# Cambio de variable: y = arccos(x/A)
y1 = np.arccos(x1/A1)

axes[0].plot(t1, y1, 'bo-', linewidth=2, markersize=6)
axes[0].set_xlabel('Tiempo t [s]')
axes[0].set_ylabel('y = arccos(x) [rad]')
axes[0].set_title('Tabla 1: Linealización MAS (coseno)\nMasa: 4m')
axes[0].grid(True, alpha=0.3)

# Ajuste lineal
coef1 = np.polyfit(t1, y1, 1)
linea1 = np.poly1d(coef1)
axes[0].plot(t1, linea1(t1), 'r--', alpha=0.7, label=f'ω = {coef1[0]:.3f} rad/s')
axes[0].legend()

# =============================================================================
# TABLA 2: Partícula con masa 3m - Movimiento parabólico
# =============================================================================
t2 = np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000])
x2 = np.array([0.000, 0.710, 1.327, 1.772, 1.986, 1.941])
t2_cuad = t2**2

axes[1].plot(t2_cuad, x2, 'go-', linewidth=2, markersize=6)
axes[1].set_xlabel('Tiempo² t² [s²]')
axes[1].set_ylabel('Posición x [m]')
axes[1].set_title('Tabla 2: Linealización movimiento parabólico\nMasa: 3m')
axes[1].grid(True, alpha=0.3)

# Ajuste cuadrático (para comparar)
coef2 = np.polyfit(t2_cuad, x2, 2)
linea2 = np.poly1d(coef2)
t_fit = np.linspace(0, 1, 100)
axes[1].plot(t_fit**2, linea2(t_fit**2), 'r--', alpha=0.7, label='Ajuste cuadrático')
axes[1].legend()

# =============================================================================
# TABLA 3: Partícula con masa 3m - Movimiento amortiguado
# =============================================================================
t3 = np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000])
x3 = np.array([2.000, 1.806, 1.261, 0.471, -0.410, -1.211])

# Cambio de variable: y = ln|x| (valor absoluto para números negativos)
y3 = np.log(np.abs(x3))

axes[2].plot(t3, y3, 'mo-', linewidth=2, markersize=6)
axes[2].set_xlabel('Tiempo t [s]')
axes[2].set_ylabel('y = ln|x|')
axes[2].set_title('Tabla 3: Linealización movimiento amortiguado\nMasa: 3m')
axes[2].grid(True, alpha=0.3)

# Ajuste lineal
coef3 = np.polyfit(t3, y3, 1)
linea3 = np.poly1d(coef3)
axes[2].plot(t3, linea3(t3), 'r--', alpha=0.7, label=f'Pendiente = {coef3[0]:.3f}')
axes[2].legend()

# =============================================================================
# TABLA 4: Partícula con masa 2m - MAS (seno)
# =============================================================================
t4 = np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000])
x4 = np.array([-1.000, -0.809, -0.309, 0.309, 0.809, 1.000])
A4 = 1.000

# Cambio de variable: y = arcsin(x/A)
y4 = np.arcsin(x4/A4)

axes[3].plot(t4, y4, 'co-', linewidth=2, markersize=6)
axes[3].set_xlabel('Tiempo t [s]')
axes[3].set_ylabel('y = arcsin(x) [rad]')
axes[3].set_title('Tabla 4: Linealización MAS (seno)\nMasa: 2m')
axes[3].grid(True, alpha=0.3)

# Ajuste lineal
coef4 = np.polyfit(t4, y4, 1)
linea4 = np.poly1d(coef4)
axes[3].plot(t4, linea4(t4), 'r--', alpha=0.7, label=f'ω = {coef4[0]:.3f} rad/s')
axes[3].legend()

# =============================================================================
# TABLA 5: Partícula con masa 2m - MAS (seno) - Igual a Tabla 4
# =============================================================================
t5 = np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000])
x5 = np.array([-1.000, -0.809, -0.309, 0.309, 0.809, 1.000])
A5 = 1.000

# Cambio de variable: y = arcsin(x/A)
y5 = np.arcsin(x5/A5)

axes[4].plot(t5, y5, 'yo-', linewidth=2, markersize=6)
axes[4].set_xlabel('Tiempo t [s]')
axes[4].set_ylabel('y = arcsin(x) [rad]')
axes[4].set_title('Tabla 5: Linealización MAS (seno)\nMasa: 2m')
axes[4].grid(True, alpha=0.3)

# Ajuste lineal
coef5 = np.polyfit(t5, y5, 1)
linea5 = np.poly1d(coef5)
axes[4].plot(t5, linea5(t5), 'r--', alpha=0.7, label=f'ω = {coef5[0]:.3f} rad/s')
axes[4].legend()

# =============================================================================
# TABLA 6: Partícula con masa 2m - MAS (coseno con fase)
# =============================================================================
t6 = np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000])
x6 = np.array([0.707, 0.410, 0.060, -0.298, -0.618, -0.856])
A6 = 0.856  # Aproximado del máximo desplazamiento

# Cambio de variable: y = arccos(x/A)
y6 = np.arccos(x6/A6)

axes[5].plot(t6, y6, 'ko-', linewidth=2, markersize=6)
axes[5].set_xlabel('Tiempo t [s]')
axes[5].set_ylabel('y = arccos(x/A) [rad]')
axes[5].set_title('Tabla 6: Linealización MAS (coseno con fase)\nMasa: 2m')
axes[5].grid(True, alpha=0.3)

# Ajuste lineal
coef6 = np.polyfit(t6, y6, 1)
linea6 = np.poly1d(coef6)
axes[5].plot(t6, linea6(t6), 'r--', alpha=0.7, label=f'ω = {coef6[0]:.3f} rad/s')
axes[5].legend()

# Ajustar layout y mostrar
plt.tight_layout()
plt.show()

# =============================================================================
# TABLAS DE DATOS LINEALIZADOS
# =============================================================================
print("=" * 60)
print("TABLAS DE DATOS LINEALIZADOS")
print("=" * 60)

print("\nTabla 1 - Linealización MAS (coseno):")
print("t[s]    x[m]    y=arccos(x)[rad]")
for i in range(len(t1)):
    print(f"{t1[i]:.3f}   {x1[i]:.3f}   {y1[i]:.3f}")

print("\nTabla 2 - Linealización movimiento parabólico:")
print("t[s]    t²[s²]    x[m]")
for i in range(len(t2)):
    print(f"{t2[i]:.3f}   {t2_cuad[i]:.3f}   {x2[i]:.3f}")

print("\nTabla 3 - Linealización movimiento amortiguado:")
print("t[s]    x[m]    y=ln|x|")
for i in range(len(t3)):
    print(f"{t3[i]:.3f}   {x3[i]:.3f}   {y3[i]:.3f}")

print("\nTabla 4 - Linealización MAS (seno):")
print("t[s]    x[m]    y=arcsin(x)[rad]")
for i in range(len(t4)):
    print(f"{t4[i]:.3f}   {x4[i]:.3f}   {y4[i]:.3f}")

print("\nTabla 5 - Linealización MAS (seno):")
print("t[s]    x[m]    y=arcsin(x)[rad]")
for i in range(len(t5)):
    print(f"{t5[i]:.3f}   {x5[i]:.3f}   {y5[i]:.3f}")

print("\nTabla 6 - Linealización MAS (coseno con fase):")
print("t[s]    x[m]    y=arccos(x/A)[rad]")
for i in range(len(t6)):
    print(f"{t6[i]:.3f}   {x6[i]:.3f}   {y6[i]:.3f}")

# =============================================================================
# RESUMEN DE FRECUENCIAS ANGULARES
# =============================================================================
print("\n" + "=" * 60)
print("RESUMEN DE FRECUENCIAS ANGULARES")
print("=" * 60)
print(f"Tabla 1 (4m): ω = {coef1[0]:.3f} rad/s")
print(f"Tabla 4 (2m): ω = {coef4[0]:.3f} rad/s") 
print(f"Tabla 5 (2m): ω = {coef5[0]:.3f} rad/s")
print(f"Tabla 6 (2m): ω = {coef6[0]:.3f} rad/s")