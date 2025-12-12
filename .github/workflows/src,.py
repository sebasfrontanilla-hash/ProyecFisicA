import numpy as np
import matplotlib.pyplot as plt


# PERSONA 1: Calcular coeficientes A y B usando Mínimos Cuadrados
 

def calcular_coeficiente_A(x_datos, y_datos):
    """
    Calcula el coeficiente A (pendiente) usando el método de mínimos cuadrados.
    
    Fórmula: A = (n*Σ(xy) - Σx*Σy) / (n*Σ(x²) - (Σx)²)
    
    Args:
        x_datos: array con los valores de x
        y_datos: array con los valores de y
    
    Returns:
        float: coeficiente A (pendiente de la recta)
    """
    n = len(x_datos)
    
    # Calculamos las sumatorias necesarias
    suma_x = np.sum(x_datos)
    suma_y = np.sum(y_datos)
    suma_xy = np.sum(x_datos * y_datos)
    suma_x_cuadrado = np.sum(x_datos ** 2)
    
    # Aplicamos la fórmula de mínimos cuadrados para A
    numerador = n * suma_xy - suma_x * suma_y
    denominador = n * suma_x_cuadrado - suma_x ** 2
    
    A = numerador / denominador
    
    print(f"Cálculo de coeficiente A:")
    print(f"  n = {n}")
    print(f"  Σx = {suma_x:.4f}")
    print(f"  Σy = {suma_y:.4f}")
    print(f"  Σ(xy) = {suma_xy:.4f}")
    print(f"  Σ(x²) = {suma_x_cuadrado:.4f}")
    print(f"  A = {A:.6f}\n")
    
    return A


def calcular_coeficiente_B(x_datos, y_datos, A):
    """
    Calcula el coeficiente B (intercepto) usando el método de mínimos cuadrados.
    
    Fórmula: B = (Σy - A*Σx) / n
    
    Args:
        x_datos: array con los valores de x
        y_datos: array con los valores de y
        A: coeficiente A previamente calculado
    
    Returns:
        float: coeficiente B (intercepto de la recta)
    """
    n = len(x_datos)
    suma_x = np.sum(x_datos)
    suma_y = np.sum(y_datos)
    
    # Aplicamos la fórmula de mínimos cuadrados para B
    B = (suma_y - A * suma_x) / n
    
    print(f"Cálculo de coeficiente B:")
    print(f"  B = (Σy - A*Σx) / n")
    print(f"  B = ({suma_y:.4f} - {A:.6f}*{suma_x:.4f}) / {n}")
    print(f"  B = {B:.6f}\n")
    
    return B


def calcular_errores(x_datos, y_datos, A, B):
    """
    Calcula los errores entre los valores reales y los predichos por la recta.
    
    Error = y_real - y_predicho
    donde y_predicho = A*x + B
    
    Args:
        x_datos: array con los valores de x
        y_datos: array con los valores de y reales
        A: coeficiente A (pendiente)
        B: coeficiente B (intercepto)
    
    Returns:
        array: errores para cada punto
    """
    # Calculamos los valores predichos usando la ecuación de la recta
    y_predichos = A * x_datos + B
    
    # El error es la diferencia entre el valor real y el predicho
    errores = y_datos - y_predichos
    
    print("Cálculo de errores:")
    print(f"  Ecuación de la recta: y = {A:.6f}*x + {B:.6f}")
    print("\n  Tabla de errores:")
    print("  {:>8} {:>12} {:>12} {:>12}".format("x", "y_real", "y_pred", "error"))
    print("  " + "-"*48)
    
    for i in range(len(x_datos)):
        print(f"  {x_datos[i]:8.4f} {y_datos[i]:12.4f} {y_predichos[i]:12.4f} {errores[i]:12.6f}")
    
    # Calculamos el error cuadrático medio para evaluar la calidad del ajuste
    error_cuadratico_medio = np.sqrt(np.mean(errores ** 2))
    print(f"\n  Error cuadrático medio (RMSE): {error_cuadratico_medio:.6f}\n")
    
    return errores


 
# PERSONA 2: Linearizar datos de las tablas


def linearizar_datos_exponencial(x_datos, y_datos):
    """
    Lineariza datos que siguen un comportamiento exponencial: y = C*e^(kx)
    
    Aplicando logaritmo: ln(y) = ln(C) + kx
    Esto se convierte en: Y = B + A*x donde Y = ln(y), A = k, B = ln(C)
    
    Args:
        x_datos: valores originales de x
        y_datos: valores originales de y (deben ser positivos)
    
    Returns:
        tuple: (x_datos, y_linearizados)
    """
    # Aplicamos logaritmo natural a los valores de y
    y_linearizados = np.log(y_datos)
    
    print("Linearización exponencial (y = C*e^(kx)):")
    print("  Transformación: Y = ln(y)")
    print("  Ecuación linearizada: Y = B + A*x")
    print("\n  Datos linearizados:")
    print("  {:>10} {:>12} {:>12}".format("x", "y original", "Y = ln(y)"))
    print("  " + "-"*36)
    
    for i in range(len(x_datos)):
        print(f"  {x_datos[i]:10.4f} {y_datos[i]:12.4f} {y_linearizados[i]:12.6f}")
    
    print()
    return x_datos, y_linearizados


def linearizar_datos_potencial(x_datos, y_datos):
    """
    Lineariza datos que siguen un comportamiento potencial: y = C*x^k
    
    Aplicando logaritmo: ln(y) = ln(C) + k*ln(x)
    Esto se convierte en: Y = B + A*X donde Y = ln(y), X = ln(x), A = k, B = ln(C)
    
    Args:
        x_datos: valores originales de x (deben ser positivos)
        y_datos: valores originales de y (deben ser positivos)
    
    Returns:
        tuple: (x_linearizados, y_linearizados)
    """
    # Aplicamos logaritmo natural a ambos ejes
    x_linearizados = np.log(x_datos)
    y_linearizados = np.log(y_datos)
    
    print("Linearización potencial (y = C*x^k):")
    print("  Transformación: X = ln(x), Y = ln(y)")
    print("  Ecuación linearizada: Y = B + A*X")
    print("\n  Datos linearizados:")
    print("  {:>10} {:>12} {:>12} {:>12}".format("x", "y", "X = ln(x)", "Y = ln(y)"))
    print("  " + "-"*48)
    
    for i in range(len(x_datos)):
        print(f"  {x_datos[i]:10.4f} {y_datos[i]:12.4f} {x_linearizados[i]:12.6f} {y_linearizados[i]:12.6f}")
    
    print()
    return x_linearizados, y_linearizados



# PERSONA 3: Graficar datos y ajuste


def graficar_ajuste_lineal(x_datos, y_datos, A, B, errores):
    """
    Crea una gráfica que muestra los datos originales, la recta ajustada
    y los errores verticales de cada punto.
    
    Args:
        x_datos: valores de x
        y_datos: valores de y
        A: coeficiente A (pendiente)
        B: coeficiente B (intercepto)
        errores: array con los errores de cada punto
    """
    plt.figure(figsize=(12, 8))
    
    # Creamos la recta de ajuste
    x_recta = np.linspace(x_datos.min(), x_datos.max(), 100)
    y_recta = A * x_recta + B
    
    # Graficamos los datos originales
    plt.scatter(x_datos, y_datos, color='blue', s=100, 
                label='Datos originales', zorder=3)
    
    # Graficamos la recta de ajuste
    plt.plot(x_recta, y_recta, 'r-', linewidth=2, 
             label=f'Ajuste: y = {A:.4f}x + {B:.4f}')
    
    # Dibujamos las líneas de error (verticales desde cada punto a la recta)
    for i in range(len(x_datos)):
        y_predicho = A * x_datos[i] + B
        plt.plot([x_datos[i], x_datos[i]], [y_datos[i], y_predicho], 
                'g--', linewidth=1, alpha=0.6)
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Ajuste de Mínimos Cuadrados con Errores Visualizados', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    # Agregamos información adicional en la gráfica
    rmse = np.sqrt(np.mean(errores ** 2))
    plt.text(0.02, 0.98, f'RMSE = {rmse:.6f}', 
             transform=plt.gca().transAxes, 
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()
    
    print("Gráfica generada exitosamente con:")
    print(f"  - Puntos de datos originales (azul)")
    print(f"  - Recta de ajuste (rojo)")
    print(f"  - Líneas de error (verde punteado)")
    print(f"  - RMSE: {rmse:.6f}\n")



# EJEMPLO DE USO INTEGRADO
 

if __name__ == "__main__":
    print("="*70)
    print("MÉTODO DE MÍNIMOS CUADRADOS - SEMANA 4")
    print("="*70 + "\n")
    
    # Datos de ejemplo (puedes cambiar estos valores)
    x_datos = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    y_datos = np.array([2.5, 3.8, 5.2, 6.9, 8.1, 9.7])
    
    print("DATOS ORIGINALES:")
    print(f"x = {x_datos}")
    print(f"y = {y_datos}\n")
    
    # PERSONA 1: Calcular coeficientes A y B
    print("\n" + "="*70)
    print("PERSONA 1: CÁLCULO DE COEFICIENTES A Y B")
    print("="*70 + "\n")
    
    A = calcular_coeficiente_A(x_datos, y_datos)
    B = calcular_coeficiente_B(x_datos, y_datos, A)
    errores = calcular_errores(x_datos, y_datos, A, B)
    
    # PERSONA 2: Linearizar datos (ejemplo con datos exponenciales)
    print("\n" + "="*70)
    print("PERSONA 2: LINEARIZACIÓN DE DATOS")
    print("="*70 + "\n")
    
    # Ejemplo con datos exponenciales
    y_exponencial = np.array([2.7, 7.4, 20.1, 54.6, 148.4, 403.4])
    x_lin, y_lin = linearizar_datos_exponencial(x_datos, y_exponencial)
    
    # Calculamos coeficientes en escala linearizada
    A_lin = calcular_coeficiente_A(x_lin, y_lin)
    B_lin = calcular_coeficiente_B(x_lin, y_lin, A_lin)
    
    print(f"En la escala original: y = e^({B_lin:.6f}) * e^({A_lin:.6f}*x)")
    print(f"Simplificado: y = {np.exp(B_lin):.6f} * e^({A_lin:.6f}*x)\n")
    
    # PERSONA 3: Graficar
    print("\n" + "="*70)
    print("PERSONA 3: GRAFICACIÓN DE RESULTADOS")
    print("="*70 + "\n")
    
    graficar_ajuste_lineal(x_datos, y_datos, A, B, errores)
    
    print("\n" + "="*70)
    print("RESUMEN FINAL")
    print("="*70)
    print(f"\nEcuación de la recta ajustada: y = {A:.6f}*x + {B:.6f}")
    print(f"Error cuadrático medio (RMSE): {np.sqrt(np.mean(errores**2)):.6f}")
    print("\n¡Proceso completado exitosamente!")