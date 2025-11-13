Teoría y Uso de Git

# ¿Qué es Git?
Git es un sistema de control de versiones distribuido creado por Linus Torvalds en 2005. Es una herramienta fundamental en el desarrollo de software moderno que permite rastrear cambios en archivos y coordinar el trabajo entre múltiples personas.
Conceptos Fundamentales

1. Control de Versiones
Git funciona como una "máquina del tiempo" para tu código. Cada vez que guardas cambios (commit), Git toma una "fotografía" de todos tus archivos en ese momento, permitiéndote volver a cualquier versión anterior.

2. Repositorio (Repository)
Es el contenedor donde Git almacena todo el historial de tu proyecto. Puede ser:

Local: En tu computadora
Remoto: En servidores como GitHub, GitLab o Bitbucket

3. Commits
Son puntos de control en la historia de tu proyecto. Cada commit contiene:

Los cambios realizados
Quién los hizo
Cuándo se hicieron
Un mensaje descriptivo

4. Ramas (Branches)
Permiten trabajar en diferentes versiones del proyecto simultáneamente. La rama principal se llama main o master.

5. Estados de los Archivos

Working Directory: Archivos en los que estás trabajando
Staging Area: Archivos preparados para el próximo commit
Repository: Archivos ya confirmados en el historial

# ¿Por Qué Usar Git?
Ventajas Principales:

Historial Completo: Puedes ver todos los cambios realizados, quién los hizo y por qué
Colaboración Eficiente: Múltiples personas pueden trabajar simultáneamente sin interferir
Respaldo Automático: Cada copia del repositorio es un respaldo completo
Experimentación Segura: Puedes probar nuevas ideas en ramas sin afectar el código principal
Reversión de Cambios: Si algo sale mal, puedes volver a versiones anteriores
Trabajo Distribuido: No necesitas conexión constante al servidor central

# ¿Cuándo Usar Git?
Úsalo SIEMPRE en:

Proyectos de desarrollo de software (cualquier tamaño)
Trabajo colaborativo entre desarrolladores
Proyectos personales que planeas mantener a largo plazo
Documentación técnica que evoluciona con el tiempo
Configuraciones de sistema que necesitas versionar

Especialmente útil cuando:

Necesitas probar nuevas funcionalidades sin romper el código existente
Trabajas con equipos remotos
Quieres mantener diferentes versiones de un producto
Necesitas rastrear quién hizo qué cambios
Requieres integración continua y despliegue automatizado

Comandos Básicos de Git
Configuración Inicial
bash# Configurar nombre y email
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
Crear y Clonar Repositorios
bash# Iniciar nuevo repositorio
git init

# Clonar repositorio existente
git clone <url-del-repositorio>
Flujo de Trabajo Básico
bash# Ver estado de archivos
git status

# Agregar archivos al staging area
git add archivo.txt          # Un archivo específico
git add .                    # Todos los archivos modificados

# Crear commit
git commit -m "Mensaje descriptivo del cambio"

# Ver historial de commits
git log
git log --oneline           # Versión compacta
Trabajar con Ramas
bash# Crear nueva rama
git branch nombre-rama

# Cambiar a una rama
git checkout nombre-rama

# Crear y cambiar a nueva rama (atajo)
git checkout -b nombre-rama

# Ver todas las ramas
git branch

# Fusionar rama en la actual
git merge nombre-rama

# Eliminar rama
git branch -d nombre-rama
Sincronización con Repositorio Remoto
bash# Agregar repositorio remoto
git remote add origin <url>

# Subir cambios
git push origin main

# Descargar cambios
git pull origin main

# Ver repositorios remotos
git remote -v
Comandos Útiles Adicionales
bash# Deshacer cambios en archivo no commiteado
git checkout -- archivo.txt

# Quitar archivo del staging area
git reset HEAD archivo.txt

# Ver diferencias
git diff                    # Cambios no staged
git diff --staged          # Cambios staged

# Guardar cambios temporalmente
git stash
git stash pop              # Recuperar cambios guardados
```

## Flujo de Trabajo Típico

1. **Clonar/Iniciar** el repositorio
2. **Crear rama** para nueva funcionalidad
3. **Hacer cambios** en el código
4. **Agregar archivos** al staging area (`git add`)
5. **Crear commit** con mensaje descriptivo
6. **Subir cambios** al repositorio remoto
7. **Crear Pull Request** (en plataformas como GitHub)
8. **Revisar código** con el equipo
9. **Fusionar** cambios a la rama principal
10. **Eliminar** rama de funcionalidad

## Mejores Prácticas

1. **Commits frecuentes y pequeños**: Es mejor hacer muchos commits pequeños que uno grande
2. **Mensajes descriptivos**: Explica QUÉ y POR QUÉ hiciste el cambio
3. **Usar ramas**: Nunca trabajes directamente en `main`
4. **Pull antes de push**: Siempre descarga cambios antes de subir los tuyos
5. **No commitear archivos sensibles**: Contraseñas, tokens, archivos de configuración local
6. **Usar .gitignore**: Para excluir archivos innecesarios (node_modules, archivos compilados, etc.)

## Ejemplo de .gitignore
```
# Dependencias
node_modules/
vendor/

# Archivos de entorno
.env
.env.local

# Archivos compilados
*.pyc
*.class
dist/
build/

# IDEs
.vscode/
.idea/
*.swp