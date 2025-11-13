Teoria y uso de Poetry

# ¿Qué es Poetry?
Poetry es una herramienta para gestión de dependencias y empaquetado en Python Poetry. Poetry reemplaza setup.py, requirements.txt, setup.cfg, MANIFEST.in y Pipfile con un formato simple basado en pyproject.toml GitHub.

# ¿Por qué usar Poetry?
1. Gestión Determinista de Dependencias
Poetry incluye un resolutor exhaustivo de dependencias que siempre encontrará una solución si existe Poetry. Esto elimina los conflictos de versiones que son comunes con pip.

2. Archivo de Bloqueo (Lock File)
Cuando ejecutas poetry install, todos y todo funcionan con las mismas dependencias, lo que mitiga el potencial de errores que afectan solo a algunas partes de los despliegues Poetry.

3. Entornos Virtuales Automáticos
Poetry viene con soporte integrado para entornos virtuales que asegura que nunca interfiera con tu instalación global de Python Real Python.

4. Todo en Uno
Poetry puede construir y empaquetar proyectos con un solo comando y publicar en PyPI Poetry.

5. Sintaxis Moderna
Utiliza el estándar pyproject.toml (PEP 518/621), que es el formato de configuración acordado para paquetes Python.

# ¿Cuándo usar Poetry?
La regla general es: usa Poetry para cualquier proyecto que será compartido, desplegado o mantenido a largo plazo. Usa pip para experimentos rápidos o ejercicios de aprendizaje DataCamp.
Casos ideales para Poetry:

Proyectos profesionales o de equipo
Bibliotecas que publicarás en PyPI
Aplicaciones que desplegarás en producción
Cuando necesitas reproducibilidad exacta entre entornos
Proyectos con dependencias complejas

# ¿Cómo usar Poetry?

 Instalación
Poetry requiere Python 3.9+ y funciona en Linux, macOS y Windows Poetry. La forma recomendada es con pipx:
bash# Instalar pipx primero (si no lo tienes)
pip install pipx
pipx ensurepath

# Instalar Poetry
pipx install poetry
O con el instalador oficial:
bash# Linux/macOS/WSL
curl -sSL https://install.python-poetry.org | python3 -

# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
Comandos Básicos
1. Crear un nuevo proyecto:
bashpoetry new mi-proyecto
```

Esto crea la estructura:
```
mi-proyecto/
├── pyproject.toml
├── README.md
├── mi_proyecto/
│   └── __init__.py
└── tests/
    └── __init__.py
2. Inicializar Poetry en un proyecto existente:
bashcd mi-proyecto-existente
poetry init
3. Agregar dependencias:
bash# Dependencia principal
poetry add requests

# Con versión específica
poetry add "pandas>=2.0.0,<3.0.0"

# Dependencia de desarrollo
poetry add --group dev pytest

4. Instalar dependencias:
bashpoetry install

5. Ejecutar comandos en el entorno virtual:
bashpoetry run python mi_script.py
poetry run pytest

6. Activar el shell del entorno virtual:
bashpoetry shell

7. Actualizar dependencias:
bash# Actualizar todas
poetry update

# Actualizar una específica
poetry update requests

8. Ver dependencias instaladas:
bashpoetry show
poetry show --tree  # Ver como árbol de dependencias
Estructura del pyproject.toml
toml[project]
name = "mi-proyecto"
version = "0.1.0"
description = "Descripción del proyecto"
requires-python = ">=3.9"
dependencies = [
    "requests>=2.28.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = ["pytest>=7.0.0", "black>=23.0.0"]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
Grupos de Dependencias
Poetry proporciona una forma de organizar dependencias por grupos, donde las dependencias declaradas en project.dependencies son parte de un grupo principal implícito requerido durante el tiempo de ejecución Poetry:
toml[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
black = "^23.0"

[tool.poetry.group.docs.dependencies]
sphinx = "^5.0"
Publicar en PyPI
bash# Construir el paquete
poetry build

# Publicar (requiere credenciales de PyPI)
Publicar en PyPI
bash# Construir el paquete
poetry build

# Publicar (requiere credenciales de PyPI)
poetry publish

#  ambos en un comando
poetry publish --build
Ventajas vs pip tradicional
Aspectopip + requirements.txtPoetryResolución de dependenciasManual/básicaAutomática y completaLock fileNo (o manual)Sí (poetry.lock)Entornos virtualesManualAutomáticoEmpaquetadosetup.py complejopyproject.toml simplePublicaciónMúltiples pasosUn comando

Poetry moderniza significativamente el flujo de trabajo de desarrollo en Python, haciéndolo más parecido a gestores de dependencias de otros lenguajes como npm (JavaScript) o cargo (Rust).ReintentarClaude aún no tiene la capacidad de ejecutar el código que genera.