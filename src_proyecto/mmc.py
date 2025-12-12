import numpy as np
import matplotlib.pyplot as plt

 
# DATOS DE LAS PARTÍCULAS (De las 6 tablas proporcionadas)


# Tabla 1: Partícula con masa 4m
tabla1_4m = {
    't': np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
    'x': np.array([1.000, 0.951, 0.809, 0.588, 0.309, 0.000]),
    'v': np.array([0.000, -0.485, -0.923, -1.271, -1.494, -1.571])
}

# Tabla 2: Partícula con masa 3m
tabla2_3m = {
    't': np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
    'x': np.array([0.707, 0.410, 0.060, -0.298, -0.618, -0.856]),
    'v': np.array([-1.283, -1.654, -1.811, -1.731, -1.427, -0.936])
}

# Tabla 3: Partícula con masa 3m
tabla3_3m = {
    't': np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
    'x': np.array([0.000, 0.710, 1.327, 1.772, 1.986, 1.941]),
    'v': np.array([3.628, 3.392, 2.714, 1.683, 0.433, -0.873])
}

# Tabla 4: Partícula con masa 2m
tabla4_2m = {
    't': np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
    'x': np.array([0.000, 0.860, 1.552, 1.944, 1.958, 1.591]),
    'v': np.array([4.443, 4.012, 2.801, 1.047, -0.910, -2.691])
}

# Tabla 5: Partícula con masa 2m
tabla5_2m = {
    't': np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
    'x': np.array([2.000, 1.806, 1.261, 0.471, -0.410, -1.211]),
    'v': np.array([0.000, -1.910, -3.448, -4.318, -4.349, -3.535])
}

# Tabla 6: Partícula con masa m
tabla6_m = {
    't': np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
    'x': np.array([-1.000, -0.809, -0.309, 0.309, 0.809, 1.000]),
    'v': np.array([0.000, 1.847, 2.988, 2.988, 1.847, 0.000])
}

# Diccionario con todas las tablas
todas_las_tablas = {
    'Tabla 1 (masa 4m)': tabla1_4m,
    'Tabla 2 (masa 3m)': tabla2_3m,
    'Tabla 3 (masa 3m)': tabla3_3m,
    'Tabla 4 (masa 2m)': tabla4_2m,
    'Tabla 5 (masa 2m)': tabla5_2m,
    'Tabla 6 (masa m)': tabla6_m
}



# PERSONA 1: Calcular coeficientes A y B usando Mínimos Cuadrados
 

def calcular_coeficiente_A(x_datos, y_datos):
    """
    Esta función calcula el coeficiente A, que representa la pendiente de la
    recta que mejor se ajusta a los datos. Usamos la fórmula del método de
    mínimos cuadrados que minimiza la suma de los errores al cuadrado.
    
    La fórmula matemática es: A = (n*Σ(xy) - Σx*Σy) / (n*Σ(x²) - (Σx)²)
    
    Donde:
    - n es el número de puntos
    - Σ representa la sumatoria
    - xy es el producto de cada par de valores
    """
    n = len(x_datos)
    
    # Calculamos cada una de las sumatorias que necesitamos
    suma_x = np.sum(x_datos)
    suma_y = np.sum(y_datos)
    suma_xy = np.sum(x_datos * y_datos)
    suma_x_cuadrado = np.sum(x_datos ** 2)
    
    # Aplicamos la fórmula dividiendo el numerador entre el denominador
    numerador = n * suma_xy - suma_x * suma_y
    denominador = n * suma_x_cuadrado - suma_x ** 2
    
    A = numerador / denominador
    
    print(f"  Cálculo del coeficiente A (pendiente):")
    print(f"    Número de puntos (n) = {n}")
    print(f"    Suma de x (Σx) = {suma_x:.4f}")
    print(f"    Suma de y (Σy) = {suma_y:.4f}")
    print(f"    Suma de xy (Σxy) = {suma_xy:.4f}")
    print(f"    Suma de x² (Σx²) = {suma_x_cuadrado:.4f}")
    print(f"    Numerador = {n}×{suma_xy:.4f} - {suma_x:.4f}×{suma_y:.4f} = {numerador:.4f}")
    print(f"    Denominador = {n}×{suma_x_cuadrado:.4f} - ({suma_x:.4f})² = {denominador:.4f}")
    print(f"    A = {numerador:.4f} / {denominador:.4f} = {A:.6f}\n")
    
    return A


def calcular_coeficiente_B(x_datos, y_datos, A):
    """
    Esta función calcula el coeficiente B, que representa el punto donde la
    recta cruza el eje y (el intercepto). Una vez que tenemos A, calcular B
    es más sencillo usando la fórmula: B = (Σy - A×Σx) / n
    
    Básicamente, B nos dice el valor promedio de y después de ajustar por
    la contribución de x multiplicada por la pendiente A.
    """
    n = len(x_datos)
    suma_x = np.sum(x_datos)
    suma_y = np.sum(y_datos)
    
    # Esta fórmula garantiza que la recta pase por el centroide de los datos
    B = (suma_y - A * suma_x) / n
    
    print(f"  Cálculo del coeficiente B (intercepto):")
    print(f"    Fórmula: B = (Σy - A×Σx) / n")
    print(f"    B = ({suma_y:.4f} - {A:.6f}×{suma_x:.4f}) / {n}")
    print(f"    B = {B:.6f}\n")
    
    return B


def calcular_errores(x_datos, y_datos, A, B):
    """
    Los errores nos dicen qué tan lejos están nuestros datos reales de la
    recta que calculamos. Para cada punto, el error es la diferencia entre
    el valor real de y y el valor que predice nuestra recta (A×x + B).
    
    Un error positivo significa que el punto real está por encima de la recta,
    y un error negativo significa que está por debajo.
    """
    # Usamos la ecuación de la recta para predecir los valores de y
    y_predichos = A * x_datos + B
    
    # El error es simplemente la diferencia entre lo real y lo predicho
    errores = y_datos - y_predichos
    
    print("  Cálculo de errores (diferencias entre valores reales y predichos):")
    print(f"    Ecuación de la recta ajustada: y = {A:.6f}×x + {B:.6f}\n")
    print("    {:>8} {:>12} {:>12} {:>12}".format("x", "y_real", "y_pred", "error"))
    print("    " + "-"*48)
    
    for i in range(len(x_datos)):
        print(f"    {x_datos[i]:8.4f} {y_datos[i]:12.4f} {y_predichos[i]:12.4f} {errores[i]:12.6f}")
    
    # El RMSE nos da una medida general de qué tan buenos son nuestros ajustes
    # Valores más pequeños de RMSE indican un mejor ajuste
    error_cuadratico_medio = np.sqrt(np.mean(errores ** 2))
    print(f"\n    Error cuadrático medio (RMSE): {error_cuadratico_medio:.6f}")
    print(f"    (Valores más pequeños indican un mejor ajuste)\n")
    
    return errores



# PERSONA 2: Linearizar datos (cambio de variable apropiado)
 

def linearizar_posicion_tiempo(t_datos, x_datos):
    """
    Para analizar cómo cambia la posición con el tiempo, a veces necesitamos
    transformar nuestros datos. En movimiento con aceleración constante, la
    posición sigue una ecuación cuadrática: x = x₀ + v₀t + (1/2)at²
    
    Si graficamos x vs t², obtenemos una relación lineal, lo cual nos permite
    usar mínimos cuadrados para encontrar la aceleración.
    """
    # Transformamos el tiempo a tiempo al cuadrado
    t_cuadrado = t_datos ** 2
    
    print("  Linearización para análisis de posición:")
    print("    Si x = x₀ + v₀t + (1/2)at², entonces graficando x vs t²")
    print("    obtenemos una relación lineal donde la pendiente es (1/2)a\n")
    print("    {:>10} {:>12} {:>12}".format("t[s]", "x[m]", "t²[s²]"))
    print("    " + "-"*36)
    
    for i in range(len(t_datos)):
        print(f"    {t_datos[i]:10.4f} {x_datos[i]:12.4f} {t_cuadrado[i]:12.6f}")
    
    print()
    return t_cuadrado, x_datos


def linearizar_velocidad_tiempo(t_datos, v_datos):
    """
    La relación entre velocidad y tiempo en movimiento con aceleración constante
    es naturalmente lineal: v = v₀ + at
    
    Esta es la forma más directa de encontrar la aceleración, ya que la pendiente
    de la recta v vs t nos da directamente el valor de la aceleración.
    """
    print("  Análisis de velocidad vs tiempo:")
    print("    La ecuación v = v₀ + at es ya lineal")
    print("    La pendiente de v vs t nos da directamente la aceleración\n")
    print("    {:>10} {:>12}".format("t[s]", "v[m/s]"))
    print("    " + "-"*24)
    
    for i in range(len(t_datos)):
        print(f"    {t_datos[i]:10.4f} {v_datos[i]:12.4f}")
    
    print()
    return t_datos, v_datos



# PERSONA 3: Graficar datos y ajuste (con valores A, B y errores)
 

def graficar_ajuste_completo(x_datos, y_datos, A, B, errores, 
                            titulo, xlabel, ylabel):
    """
    Esta función crea una visualización completa que nos ayuda a entender
    qué tan bien se ajusta nuestra recta a los datos. Mostramos tres elementos:
    
    1. Los puntos originales (en azul)
    2. La recta de ajuste calculada (en rojo)
    3. Las líneas de error verticales (en verde punteado)
    
    Las líneas de error son especialmente útiles porque nos permiten ver
    visualmente qué puntos se alejan más de nuestro modelo.
    """
    plt.figure(figsize=(12, 8))
    
    # Creamos puntos para dibujar una recta suave
    x_recta = np.linspace(x_datos.min(), x_datos.max(), 100)
    y_recta = A * x_recta + B
    
    # Graficamos los datos experimentales como puntos
    plt.scatter(x_datos, y_datos, color='blue', s=100, 
                label='Datos experimentales', zorder=3, alpha=0.7)
    
    # Graficamos la recta de mejor ajuste
    plt.plot(x_recta, y_recta, 'r-', linewidth=2.5, 
             label=f'Ajuste lineal: y = {A:.4f}x + {B:.4f}')
    
    # Dibujamos líneas verticales que muestran el error de cada punto
    # Estas líneas conectan cada punto real con su correspondiente punto en la recta
    for i in range(len(x_datos)):
        y_predicho = A * x_datos[i] + B
        plt.plot([x_datos[i], x_datos[i]], [y_datos[i], y_predicho], 
                'g--', linewidth=1.5, alpha=0.6, 
                label='Errores' if i == 0 else '')
    
    plt.xlabel(xlabel, fontsize=13, fontweight='bold')
    plt.ylabel(ylabel, fontsize=13, fontweight='bold')
    plt.title(titulo, fontsize=15, fontweight='bold', pad=20)
    plt.legend(fontsize=11, loc='best')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Calculamos y mostramos estadísticas importantes del ajuste
    rmse = np.sqrt(np.mean(errores ** 2))
    r_cuadrado = 1 - (np.sum(errores**2) / np.sum((y_datos - np.mean(y_datos))**2))
    
    # Agregamos un cuadro de texto con información del ajuste
    texto_info = f'RMSE = {rmse:.6f}\nR² = {r_cuadrado:.6f}'
    plt.text(0.02, 0.98, texto_info, 
             transform=plt.gca().transAxes, 
             verticalalignment='top',
             fontsize=10,
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    plt.tight_layout()
    plt.show()
    
    print(f"  Gráfica generada: {titulo}")
    print(f"    - RMSE (Error cuadrático medio): {rmse:.6f}")
    print(f"    - R² (Coeficiente de determinación): {r_cuadrado:.6f}")
    print(f"      (R² cercano a 1 indica excelente ajuste)\n")



# ANÁLISIS COMPLETO DE TODAS LAS TABLAS


def analizar_tabla_completa(nombre_tabla, datos_tabla):
    """
    Esta función realiza el análisis completo de una tabla de datos. Ejecuta
    los tres pasos del proyecto: calcula coeficientes, lineariza si es necesario,
    y crea las visualizaciones correspondientes.
    """
    print("\n" + "="*75)
    print(f"ANÁLISIS DE {nombre_tabla}")
    print("="*75 + "\n")
    
    t = datos_tabla['t']
    x = datos_tabla['x']
    v = datos_tabla['v']
    
    # -------------------------------------------------------------------------
    # ANÁLISIS 1: Velocidad vs Tiempo (v vs t)
    # -------------------------------------------------------------------------
    print("\n--- ANÁLISIS 1: VELOCIDAD vs TIEMPO ---\n")
    print("PERSONA 1: Calculando coeficientes para v vs t")
    A_vt = calcular_coeficiente_A(t, v)
    B_vt = calcular_coeficiente_B(t, v, A_vt)
    errores_vt = calcular_errores(t, v, A_vt, B_vt)
    
    print(f"Resultado: v = {A_vt:.6f}×t + {B_vt:.6f}")
    print(f"Interpretación física:")
    print(f"  - Velocidad inicial (v₀) = {B_vt:.4f} m/s")
    print(f"  - Aceleración (a) = {A_vt:.4f} m/s²\n")
    
    print("PERSONA 3: Generando gráfica de v vs t")
    graficar_ajuste_completo(t, v, A_vt, B_vt, errores_vt,
                            f'{nombre_tabla}: Velocidad vs Tiempo',
                            'Tiempo t [s]', 'Velocidad v [m/s]')
    
    # -------------------------------------------------------------------------
    # ANÁLISIS 2: Posición vs Tiempo al Cuadrado (x vs t²)
    # -------------------------------------------------------------------------
    print("\n--- ANÁLISIS 2: POSICIÓN vs TIEMPO AL CUADRADO ---\n")
    print("PERSONA 2: Linearizando datos (x vs t²)")
    t_cuadrado, x_lin = linearizar_posicion_tiempo(t, x)
    
    print("PERSONA 1: Calculando coeficientes para x vs t²")
    A_xt2 = calcular_coeficiente_A(t_cuadrado, x_lin)
    B_xt2 = calcular_coeficiente_B(t_cuadrado, x_lin, A_xt2)
    errores_xt2 = calcular_errores(t_cuadrado, x_lin, A_xt2, B_xt2)
    
    print(f"Resultado: x = {A_xt2:.6f}×t² + {B_xt2:.6f}")
    print(f"Interpretación física:")
    print(f"  - Posición inicial (x₀) = {B_xt2:.4f} m")
    print(f"  - (1/2)×aceleración = {A_xt2:.6f}")
    print(f"  - Aceleración calculada = {2*A_xt2:.4f} m/s²\n")
    
    print("PERSONA 3: Generando gráfica de x vs t²")
    graficar_ajuste_completo(t_cuadrado, x_lin, A_xt2, B_xt2, errores_xt2,
                            f'{nombre_tabla}: Posición vs Tiempo²',
                            'Tiempo² t² [s²]', 'Posición x [m]')
    
    # Comparación de aceleraciones
    print("\n" + "-"*75)
    print("COMPARACIÓN DE RESULTADOS:")
    print(f"  Aceleración desde v vs t:  {A_vt:.4f} m/s²")
    print(f"  Aceleración desde x vs t²: {2*A_xt2:.4f} m/s²")
    diferencia = abs(A_vt - 2*A_xt2)
    print(f"  Diferencia: {diferencia:.6f} m/s²")
    if diferencia < 0.1:
        print("  ✓ Excelente concordancia entre ambos métodos")
    else:
        print("  ⚠ Hay diferencia significativa - revisar datos")
    print("-"*75 + "\n")



# PROGRAMA PRINCIPAL
 

if __name__ == "__main__":
    print("\n" + "="*75)
    print("MÉTODO DE MÍNIMOS CUADRADOS APLICADO A DATOS DE PARTÍCULAS")
    print("SEMANA 4 - ANÁLISIS COMPLETO DE LAS 6 TABLAS")
    print("="*75)
    
    # Procesamos cada tabla individualmente
    for nombre, datos in todas_las_tablas.items():
        analizar_tabla_completa(nombre, datos)
        print("\n" + "="*75)
        input("Presiona ENTER para continuar con la siguiente tabla...")
        print("="*75)
    
    print("\n" + "="*75)
    print("ANÁLISIS COMPLETADO")
    print("="*75)
    print("\nResumen: Se han procesado las 6 tablas de partículas.")
    print("Para cada tabla se realizaron dos análisis:")
    print("  1. Velocidad vs Tiempo (para encontrar aceleración directamente)")
    print("  2. Posición vs Tiempo² (para verificar aceleración)")
    print("\nCada análisis incluye:")
    print("  - Cálculo de coeficientes A y B (Persona 1)")
    print("  - Linearización de datos cuando es necesario (Persona 2)")
    print("  - Gráficas con errores visualizados (Persona 3)")
    print("\n¡Proyecto completado exitosamente!")