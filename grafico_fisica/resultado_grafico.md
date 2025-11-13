                          Analisis De Los Resultado Graficos

# FIGURA 1: ANÁLISIS DE ERROR RELATIVO

1. Masa 4m
Comportamiento General:
Los errores relativos son pequeños en magnitud, indicando una excelente concordancia con la solución analítica.
Error en Posición:
Muestra una tendencia creciente en valor absoluto conforme avanza el tiempo.
Comportamiento típico de métodos numéricos donde el error se acumula progresivamente.
Error en Velocidad:
Similar al de posición, pero con mayor magnitud.
La velocidad involucra derivadas que amplifican los errores numéricos.
Interpretación Física:
El sistema con mayor masa (4m) presenta mayor estabilidad numérica debido a que su inercia reduce las oscilaciones rápidas que son difíciles de capturar numéricamente.
2. Masa 3m-A
Comportamiento General:
Errores moderadamente bajos, pero ligeramente mayores que 4m.
Patrón Observado:
Los errores muestran un comportamiento oscilatorio débil.
Indica que el método numérico tiene un ligero desfase con la frecuencia real del sistema.
Error en Velocidad:
Domina sobre el error en posición.
Los métodos numéricos estándar (Euler, Runge-Kutta de bajo orden) tienen más dificultad preservando la derivada temporal.
Interpretación Física:
A menor masa, la frecuencia natural aumenta (ω es mayor), lo que exige pasos temporales más pequeños para mantener la precisión.
3. Masa 3m-B
Diferencia con 3m-A:
Las condiciones iniciales diferentes (x₀ y v₀) producen trayectorias distintas en el espacio fase.
Comportamiento Esperado:
Si las condiciones iniciales implican mayor energía total, el sistema oscila con mayor amplitud.
Esto puede magnificar los errores de truncamiento.
Error Relativo:
Probablemente mayor que 3m-A en ciertos instantes.
Especialmente cuando la solución analítica pasa por valores pequeños (cerca del equilibrio), donde el error relativo se amplifica.
Interpretación Física:
Demuestra la sensibilidad del método numérico a las condiciones iniciales del sistema.
4. Masa 2m-A
Comportamiento General:
Errores significativamente mayores que en masas más grandes.
Razón Física:
Con masa reducida, la frecuencia angular ω = √(k/m) aumenta (asumiendo rigidez k constante).
El sistema oscila más rápido.
Consecuencia Numérica:
El paso temporal Δt = 0.2s puede ser demasiado grande para capturar adecuadamente las oscilaciones rápidas.
Viola el criterio de estabilidad de Courant.
Error en Velocidad:
Muestra picos pronunciados, especialmente en puntos de inflexión donde la aceleración es máxima.
Interpretación Física:
Evidencia clara de que el método numérico se degrada con sistemas de alta frecuencia.
5. Masa 2m-B
Comportamiento General:
Similar a 2m-A en magnitud de error, pero con distribución temporal diferente.
Condiciones Iniciales:
Si v₀ = 0 y x₀ = 2 (partiendo del reposo en desplazamiento máximo), el error podría ser mínimo al inicio.
Posteriormente crece cuadráticamente con el tiempo.
Comparación con 2m-A:
Si 2m-A tiene v₀ ≠ 0, su error inicial será mayor porque involucra tanto posición como velocidad desde t=0.
Interpretación Física:
Los errores no solo dependen de la frecuencia, sino también de cómo se inicializa el sistema numéricamente.
6. Masa m
Comportamiento General:
Errores máximos de todas las configuraciones analizadas.
Razón Crítica:
Con la menor masa, este sistema tiene la frecuencia más alta.
Es el más difícil de simular con el paso temporal dado.
Posible Fallo del Método:
Si los errores crecen exponencialmente: indica inestabilidad numérica.
Si crecen linealmente: acumulación típica de error de truncamiento.
Error en Velocidad:
Desproporcionadamente grande.
Posiblemente supera el 100% en algunos instantes cuando v_analítica ≈ 0.
Interpretación Física:
Este caso representa el límite de aplicabilidad del método numérico con el paso temporal elegido.

# FIGURA 2: ANÁLISIS DE ERROR PORCENTUAL

Patrones Generales Esperados
Explosión de Errores Porcentuales:
Cuando x_analítica o v_analítica → 0 (en puntos de equilibrio o extremos), el error porcentual tiende a infinito matemáticamente.
Los valores NaN que aparecen son correctos desde el punto de vista del cálculo relativo.
1. Masa 4m
Característica
Descripción
Error promedio
Probablemente < 5%
Distribución
Relativamente uniforme, sin picos dramáticos
Conclusión
Método numérico aceptable para esta configuración
2. Masas 3m (A y B)
Característica
Descripción
Error promedio
Entre 5-15%
Distribución
Picos localizados donde el valor analítico es pequeño
Conclusión
Precisión moderada: aceptable para estudios cualitativos, pero NO para análisis cuantitativos precisos
3. Masas 2m (A y B)
Característica
Descripción
Error promedio
Puede superar 20-30%
Distribución
Picos pronunciados
Conclusión
Resultados cuestionables para análisis serios. Se requiere reducir Δt o usar método de orden superior
4. Masa m
Característica
Descripción
Error promedio
Posiblemente > 50%
Distribución
Dominada por picos, difícil extraer información útil
Conclusión
Simulación NO confiable. Los resultados numéricos no representan fielmente la física del sistema