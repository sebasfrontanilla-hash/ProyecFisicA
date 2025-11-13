import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

# Configurar estilo
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.facecolor'] = '#f8f9fa'
plt.rcParams['figure.facecolor'] = 'white'

# DATOS DE LAS 6 TABLAS (masas del sistema)
tablas = [
    ('4m', np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
           np.array([1.000, 0.951, 0.809, 0.588, 0.309, 0.000]),
           np.array([0.000, -0.485, -0.923, -1.271, -1.494, -1.571])),
    
    ('3m-A', np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
             np.array([0.707, 0.410, 0.060, -0.298, -0.618, -0.856]),
             np.array([-1.283, -1.654, -1.811, -1.731, -1.427, -0.936])),
    
    ('3m-B', np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
             np.array([0.000, 0.710, 1.327, 1.772, 1.986, 1.941]),
             np.array([3.628, 3.392, 2.714, 1.683, 0.433, -0.873])),
    
    ('2m-A', np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
             np.array([0.000, 0.860, 1.552, 1.944, 1.958, 1.591]),
             np.array([4.443, 4.012, 2.801, 1.047, -0.910, -2.691])),
    
    ('2m-B', np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
             np.array([2.000, 1.806, 1.261, 0.471, -0.410, -1.211]),
             np.array([0.000, -1.910, -3.448, -4.318, -4.349, -3.535])),
    
    ('m', np.array([0.000, 0.200, 0.400, 0.600, 0.800, 1.000]),
          np.array([-1.000, -0.809, -0.309, 0.309, 0.809, 1.000]),
          np.array([0.000, 1.847, 2.988, 2.988, 1.847, 0.000]))
]

def solucion_analitica(t, x0, v0, omega=np.pi):
    """Solución analítica del oscilador armónico simple"""
    x_exacta = x0 * np.cos(omega * t) + (v0 / omega) * np.sin(omega * t)
    v_exacta = -x0 * omega * np.sin(omega * t) + v0 * np.cos(omega * t)
    return x_exacta, v_exacta

def calcular_errores(t, x_num, v_num, x0, v0):
    """Calcula errores relativos y porcentuales """
    errores_rel_x, errores_porc_x = [], []
    errores_rel_v, errores_porc_v = [], []
    
    for i, tiempo in enumerate(t):
        x_exacta, v_exacta = solucion_analitica(tiempo, x0, v0)
        
        # Error en posición
        if abs(x_exacta) > 1e-10:
            error_rel_x = x_num[i] - x_exacta
            error_porc_x = abs(error_rel_x / x_exacta) * 100
        else:
            error_rel_x = x_num[i] if abs(x_num[i]) > 1e-10 else 0.0
            error_porc_x = np.nan
        
        # Error en velocidad
        if abs(v_exacta) > 1e-10:
            error_rel_v = v_num[i] - v_exacta
            error_porc_v = abs(error_rel_v / v_exacta) * 100
        else:
            error_rel_v = v_num[i] if abs(v_num[i]) > 1e-10 else 0.0
            error_porc_v = np.nan
        
        errores_rel_x.append(error_rel_x)
        errores_porc_x.append(error_porc_x)
        errores_rel_v.append(error_rel_v)
        errores_porc_v.append(error_porc_v)
    
    return (np.array(errores_rel_x), np.array(errores_porc_x), 
            np.array(errores_rel_v), np.array(errores_porc_v))

# Procesar todas las tablas
datos_errores = []
for nombre, t, x, v in tablas:
    e_rel_x, e_porc_x, e_rel_v, e_porc_v = calcular_errores(t, x, v, x[0], v[0])
    datos_errores.append((nombre, t, e_rel_x, e_porc_x, e_rel_v, e_porc_v))

# FIGURA 1: ERROR RELATIVO

fig1, axes1 = plt.subplots(2, 3, figsize=(16, 10))
fig1.patch.set_facecolor('white')
fig1.suptitle('ERROR RELATIVO: ', 
              fontsize=17, fontweight='bold', y=0.98)
axes1 = axes1.flatten()

lines_rel_x, lines_rel_v = [], []
points_rel_x, points_rel_v = [], []
texts_rel = []

for idx, (nombre, t, e_rel_x, e_porc_x, e_rel_v, e_porc_v) in enumerate(datos_errores):
    ax = axes1[idx]
    
    # Líneas animadas con mejor estilo
    line_x, = ax.plot([], [], 'o-', color='#e74c3c', linewidth=2.5, 
                      markersize=7, label='Error Pos', alpha=0.85)
    line_v, = ax.plot([], [], 's-', color='#3498db', linewidth=2.5, 
                      markersize=7, label='Error Vel', alpha=0.85)
    
    # Puntos destacados para valor actual
    point_x, = ax.plot([], [], 'o', color='#c0392b', markersize=15, 
                       markeredgecolor='white', markeredgewidth=2.5, zorder=5)
    point_v, = ax.plot([], [], 's', color='#2980b9', markersize=15, 
                       markeredgecolor='white', markeredgewidth=2.5, zorder=5)
    
    # Texto para mostrar tiempo actual
    text = ax.text(0.98, 0.97, '', transform=ax.transAxes, 
                   fontsize=10, ha='right', va='top',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    texts_rel.append(text)
    
    lines_rel_x.append((line_x, t, e_rel_x))
    lines_rel_v.append((line_v, t, e_rel_v))
    points_rel_x.append((point_x, t, e_rel_x))
    points_rel_v.append((point_v, t, e_rel_v))
    
    # Configuración de ejes con márgenes adecuados
    ax.set_xlim(-0.05, 1.05)
    valid_vals = list(e_rel_x[~np.isnan(e_rel_x)]) + list(e_rel_v[~np.isnan(e_rel_v)])
    if valid_vals:
        y_min, y_max = min(valid_vals), max(valid_vals)
        y_range = y_max - y_min
        ax.set_ylim(y_min - 0.15*y_range, y_max + 0.15*y_range)
    
    # Línea de referencia
    ax.axhline(y=0, color='#34495e', linestyle='--', linewidth=1.8, alpha=0.6, zorder=1)
    
    ax.set_title(f'Masa: {nombre}', fontsize=12, fontweight='bold', pad=10)
    ax.set_xlabel('Tiempo (s)', fontsize=10, fontweight='medium')
    ax.set_ylabel('Error Relativo', fontsize=10, fontweight='medium')
    ax.legend(fontsize=9, loc='best', framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()

def animate_rel(frame):
    """Animación del error relativo """
    for idx in range(6):
        line_x, t, e_x = lines_rel_x[idx]
        line_v, t, e_v = lines_rel_v[idx]
        point_x, t_px, e_px = points_rel_x[idx]
        point_v, t_pv, e_pv = points_rel_v[idx]
        text = texts_rel[idx]
        
        if frame < len(t):
            # Actualizar líneas progresivamente
            line_x.set_data(t[:frame+1], e_x[:frame+1])
            line_v.set_data(t[:frame+1], e_v[:frame+1])
            
            # Actualizar puntos actuales
            if not np.isnan(e_px[frame]):
                point_x.set_data([t[frame]], [e_px[frame]])
            else:
                point_x.set_data([], [])
                
            if not np.isnan(e_pv[frame]):
                point_v.set_data([t[frame]], [e_pv[frame]])
            else:
                point_v.set_data([], [])
            
            # Actualizar texto de tiempo
            text.set_text(f't = {t[frame]:.1f}s')
    
    return []

#  FIGURA 2: ERROR PORCENTUAL 

fig2, axes2 = plt.subplots(2, 3, figsize=(16, 10))
fig2.patch.set_facecolor('white')
fig2.suptitle('ERROR PORCENTUAL (%):', 
              fontsize=17, fontweight='bold', y=0.98)
axes2 = axes2.flatten()

lines_porc_x, lines_porc_v = [], []
points_porc_x, points_porc_v = [], []
texts_porc = []

for idx, (nombre, t, e_rel_x, e_porc_x, e_rel_v, e_porc_v) in enumerate(datos_errores):
    ax = axes2[idx]
    
    # Líneas animadas
    line_x, = ax.plot([], [], 'o-', color='#9b59b6', linewidth=2.5, 
                      markersize=7, label='Error Pos %', alpha=0.85)
    line_v, = ax.plot([], [], 'D-', color='#e67e22', linewidth=2.5, 
                      markersize=7, label='Error Vel %', alpha=0.85)
    
    # Puntos destacados
    point_x, = ax.plot([], [], 'o', color='#8e44ad', markersize=15, 
                       markeredgecolor='white', markeredgewidth=2.5, zorder=5)
    point_v, = ax.plot([], [], 'D', color='#d35400', markersize=15, 
                       markeredgecolor='white', markeredgewidth=2.5, zorder=5)
    
    # Texto de tiempo
    text = ax.text(0.98, 0.97, '', transform=ax.transAxes, 
                   fontsize=10, ha='right', va='top',
                   bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    texts_porc.append(text)
    
    lines_porc_x.append((line_x, t, e_porc_x))
    lines_porc_v.append((line_v, t, e_porc_v))
    points_porc_x.append((point_x, t, e_porc_x))
    points_porc_v.append((point_v, t, e_porc_v))
    
    # Configuración de ejes
    ax.set_xlim(-0.05, 1.05)
    valid_vals = list(e_porc_x[~np.isnan(e_porc_x)]) + list(e_porc_v[~np.isnan(e_porc_v)])
    if valid_vals:
        max_val = max(valid_vals)
        ax.set_ylim(0, max_val * 1.2)
    else:
        ax.set_ylim(0, 10)
    
    ax.set_title(f'Masa: {nombre}', fontsize=12, fontweight='bold', pad=10)
    ax.set_xlabel('Tiempo (s)', fontsize=10, fontweight='medium')
    ax.set_ylabel('Error Porcentual (%)', fontsize=10, fontweight='medium')
    ax.legend(fontsize=9, loc='best', framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()

def animate_porc(frame):
    """Animación del error porcentual """
    for idx in range(6):
        line_x, t, e_x = lines_porc_x[idx]
        line_v, t, e_v = lines_porc_v[idx]
        point_x, t_px, e_px = points_porc_x[idx]
        point_v, t_pv, e_pv = points_porc_v[idx]
        text = texts_porc[idx]
        
        if frame < len(t):
            line_x.set_data(t[:frame+1], e_x[:frame+1])
            line_v.set_data(t[:frame+1], e_v[:frame+1])
            
            if not np.isnan(e_px[frame]):
                point_x.set_data([t[frame]], [e_px[frame]])
            else:
                point_x.set_data([], [])
                
            if not np.isnan(e_pv[frame]):
                point_v.set_data([t[frame]], [e_pv[frame]])
            else:
                point_v.set_data([], [])
            
            text.set_text(f't = {t[frame]:.1f}s')
    
    return []

# Crear animaciones con velocidad ajustada
anim1 = FuncAnimation(fig1, animate_rel, frames=6, 
                     interval=700, blit=False, repeat=True)

anim2 = FuncAnimation(fig2, animate_porc, frames=6, 
                     interval=700, blit=False, repeat=True)

plt.show()

# ==================== RESUMEN DE RESULTADOS ====================
print("\n" + "="*70)
print(" "*15 + "ANÁLISIS DE ERRORES - OSCILADOR ARMÓNICO")
print("="*70)
print("\n FIGURAS GENERADAS:")
print("  ✓ Figura 1: Error Relativo (6 subgráficas - 2x3)")
print("  ✓ Figura 2: Error Porcentual (6 subgráficas - 2x3)")
print("\n CARACTERÍSTICAS DE LA ANIMACIÓN:")
print("  • Las líneas se dibujan progresivamente punto a punto")
print("  • Los puntos grandes indican el valor actual en cada paso")
print("  • Indicador de tiempo en cada subgráfica")
print("  • Intervalo: 700ms por frame")
print("\n MASAS ANALIZADAS:")
for i, (nombre, _, _, _, _, _) in enumerate(datos_errores, 1):
    print(f"  {i}. {nombre}")
print("\n INTERPRETACIÓN:")
print("  • Error Relativo: diferencia absoluta (numérico - analítico)")
print("  • Error Porcentual: |error relativo / valor analítico| × 100%")
print("  • NaN aparece cuando el valor analítico ≈ 0")
print("="*70 + "\n")