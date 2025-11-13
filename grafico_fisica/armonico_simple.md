                                 Movimiento Armónico Simple

# 1. Definición y Concepto Fundamental
El Movimiento Armónico Simple es un tipo de movimiento periódico que ocurre cuando un cuerpo oscila alrededor de una posición de equilibrio bajo la acción de una fuerza restauradora proporcional al desplazamiento y de sentido opuesto a este. Es uno de los movimientos más importantes en física porque describe muchos fenómenos naturales y sirve como base para entender oscilaciones más complejas.

2. Condiciones para que exista MAS
Para que un sistema realice MAS debe cumplirse que la fuerza restauradora sea propproporcional al desplazamiento y dirigida hacia la posición de equilibrio:
F = -kx
Esta es la Ley de Hooke, donde:

F es la fuerza restauradora
k es la constante de recuperación o constante elástica
x es el desplazamiento desde la posición de equilibrio
El signo negativo indica que la fuerza siempre apunta hacia el equilibrio

3. Ecuación Diferencial del MAS
Aplicando la segunda ley de Newton (F = ma):
m(d²x/dt²) = -kx
Reordenando:
d²x/dt² + (k/m)x = 0
o bien:
d²x/dt² + ω²x = 0
donde ω² = k/m y ω es la frecuencia angular.

4. Solución de las Ecuaciones del Movimiento
Posición en función del tiempo:
x(t) = A·cos(ωt + φ)
o equivalentemente:
x(t) = A·sen(ωt + φ₀)
Velocidad:
v(t) = dx/dt = -Aω·sen(ωt + φ)
Aceleración:
a(t) = dv/dt = -Aω²·cos(ωt + φ) = -ω²x
Nota importante: la aceleración es proporcional al desplazamiento pero de signo opuesto.


5. Parámetros Fundamentales
Amplitud (A)
Es el desplazamiento máximo desde la posición de equilibrio. Representa la máxima elongación del sistema y depende de las condiciones iniciales (cómo se inicia el movimiento).
Frecuencia Angular (ω)
ω = √(k/m) (en radianes por segundo)
Relaciona las propiedades del sistema (masa y constante elástica) con la rapidez de oscilación.
Periodo (T)
Es el tiempo que tarda el sistema en completar una oscilación completa:
T = 2π/ω = 2π√(m/k)
Frecuencia (f)
Es el número de oscilaciones completas por unidad de tiempo:
f = 1/T = ω/2π = (1/2π)√(k/m)
Se mide en Hertz (Hz) o ciclos por segundo.
Fase (φ)
Es el ángulo inicial que determina la posición y velocidad del sistema en t = 0. Depende de las condiciones iniciales del problema.


6. Relaciones entre Velocidad y Posición
Combinando las ecuaciones de posición y velocidad, podemos obtener relaciones independientes del tiempo:
v² = ω²(A² - x²)
o bien:
v = ±ω√(A² - x²)
Esta ecuación muestra que:

Cuando x = 0 (equilibrio): v = ±ωA (velocidad máxima)
Cuando x = ±A (extremos): v = 0 (velocidad nula)

La velocidad máxima es: v_máx = ωA
La aceleración máxima es: a_máx = ω²A


7. Energía en el MAS
Energía Potencial Elástica:
E_p = (1/2)kx² = (1/2)kA²cos²(ωt + φ)
Energía Cinética:
E_c = (1/2)mv² = (1/2)mω²A²sen²(ωt + φ) = (1/2)kA²sen²(ωt + φ)
Energía Mecánica Total:
E_total = E_p + E_c = (1/2)kA² = constante
La energía total es proporcional al cuadrado de la amplitud y permanece constante si no hay fricción. Hay una transformación continua entre energía potencial y cinética.
En los extremos (x = ±A): toda la energía es potencial.
En el equilibrio (x = 0): toda la energía es cinética.


8. Sistema Masa-Resorte
Es el ejemplo más común de MAS. Un objeto de masa m unido a un resorte de constante k oscila con:
T = 2π√(m/k)
ω = √(k/m)
Características importantes:

El periodo NO depende de la amplitud (isocronismo)
A mayor masa, mayor periodo (oscila más lento)
A mayor constante k (resorte más rígido), menor periodo (oscila más rápido)

9. Péndulo Simple
Un péndulo de longitud L y masa m realiza MAS para ángulos pequeños (θ < 15°):
T = 2π√(L/g)
donde g es la aceleración de la gravedad.
Características:

El periodo NO depende de la masa
El periodo NO depende de la amplitud (para ángulos pequeños)
Solo depende de la longitud y la gravedad

La aproximación: sen(θ) ≈ θ (en radianes) es válida para ángulos pequeños.


10. Composición de Movimientos Armónicos
Cuando dos MAS se superponen en la misma dirección:
x(t) = A₁cos(ωt + φ₁) + A₂cos(ωt + φ₂)
Si tienen la misma frecuencia, el resultado es otro MAS con amplitud:
A = √(A₁² + A₂² + 2A₁A₂cos(φ₂ - φ₁))


11. Oscilaciones Amortiguadas
En la realidad, siempre hay fuerzas de fricción que disipan energía. La ecuación del movimiento incluye un término de amortiguamiento:
m(d²x/dt²) + b(dx/dt) + kx = 0
donde b es el coeficiente de amortiguamiento.
Tipos de amortiguamiento:

Subamortiguado: el sistema oscila con amplitud decreciente
Críticamente amortiguado: retorna al equilibrio sin oscilar en el menor tiempo posible
Sobreamortiguado: retorna lentamente al equilibrio sin oscilar

12. Oscilaciones Forzadas y Resonancia
Cuando se aplica una fuerza externa periódica:
m(d²x/dt²) + b(dx/dt) + kx = F₀cos(ω_ft)
donde ω_f es la frecuencia de la fuerza externa.
Resonancia: ocurre cuando la frecuencia de la fuerza externa coincide con la frecuencia natural del sistema (ω_f ≈ ω₀). En este caso, la amplitud de oscilación puede ser muy grande, incluso destructiva si el sistema no puede soportarla.

13. Aplicaciones Importantes

Relojes de péndulo: medición del tiempo
Sistemas de suspensión: automóviles, edificios antisísmicos
Instrumentos musicales: cuerdas, membranas
Circuitos eléctricos: circuitos LC oscilantes
Átomos y moléculas: vibraciones moleculares
Ondas: el MAS es la base para entender ondas mecánicas y electromagnéticas
Astronomía: movimiento de estrellas binarias
Medicina: electrocardiogramas, análisis de vibraciones

14. Conceptos Clave para Recordar

La fuerza restauradora siempre apunta hacia el equilibrio y es proporcional al desplazamiento
El movimiento es periódico y sinusoidal
La energía total se conserva (sin fricción)
El periodo no depende de la amplitud (isocronismo)
La velocidad es máxima en el equilibrio y cero en los extremos
La aceleración es máxima en los extremos y cero en el equilibrio
La aceleración siempre es opuesta al desplazamiento

 15. Representación Gráfica
Las gráficas típicas del MAS muestran:

x vs t: función coseno o seno
v vs t: desfasada 90° respecto a x
a vs t: desfasada 180° respecto a x (opuesta)
E vs t: energía total constante, energías cinética y potencial variando senoidalmente