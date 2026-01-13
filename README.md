# Mathematical-Methods

# Primer Proyecto: Simulación de Trayectoria de Proyectiles

Este proyecto simula el movimiento de un proyectil en un entorno con y sin resistencia del aire, utilizando métodos numéricos para resolver las ecuaciones de movimiento. El objetivo es analizar cómo factores como el ángulo de lanzamiento y la resistencia afectan la trayectoria, alcance y velocidad del proyectil.

## Características Principales:

1. **Simulación Física Completa**: 
   - Modela el movimiento con aceleración gravitacional y resistencia del aire proporcional al cuadrado de la velocidad
   - Implementa ecuaciones diferenciales usando el método de Euler para integración temporal

2. **Visualización Gráfica**:
   - Gráficos de posición vs tiempo (ejes X e Y)
   - Gráficos de velocidad vs tiempo (componentes X e Y)
   - Comparación visual de trayectorias con y sin resistencia del aire
   - Análisis de trayectorias para múltiples ángulos de lanzamiento

3. **Análisis Comparativo**:
   - Efecto de la resistencia del aire en el alcance máximo
   - Determinación del ángulo óptimo de lanzamiento en ambos escenarios
   - Visualización de múltiples trayectorias para diferentes condiciones iniciales

## Resultados Destacados:

- **Sin resistencia del aire**: El ángulo que maximiza el alcance es aproximadamente 45°, confirmando la teoría clásica
- **Con resistencia del aire**: El ángulo óptimo se reduce significativamente debido a la disipación de energía
- La resistencia del aire reduce notablemente el alcance total y altera la forma de la trayectoria

## Aplicaciones:
- Educación en física y métodos numéricos
- Análisis balístico básico
- Ejemplo de simulación computacional en Python
- Demostración de efectos de resistencia en movimientos parabólicos

Este proyecto combina conceptos de física, programación y visualización de datos, proporcionando una herramienta educativa para entender el movimiento de proyectiles en condiciones realistas e ideales.

# Segundo Proyecto: Precesión y el Perihelio de Mercurio

Este proyecto simula la órbita de Mercurio alrededor del Sol, teniendo en cuenta la precesión de su perihelio, un fenómeno explicado por la relatividad general. Se implementa una solución numérica utilizando el método de Runge-Kutta de 4to orden para resolver las ecuaciones de movimiento con una fuerza gravitacional modificada.
Características principales:

    Modelado físico: Incluye una fuerza gravitacional con un término adicional (α) para simular efectos relativistas.

    Método numérico: Integración temporal con Runge-Kutta para calcular posición, velocidad, ángulo y distancia radial.

    Visualización: Genera gráficas de la órbita y de la distancia entre Mercurio y el Sol a lo largo del tiempo.

    Análisis: Calcula la derivada temporal de la distancia radial para identificar los puntos de perihelio y afelio.

Resultados esperados:

    La órbita elíptica de Mercurio con precesión.

    La distancia promedio entre Mercurio y el Sol (≈0.399 UA).

    Identificación de los puntos de máxima y mínima distancia mediante la derivada de la distancia radial.

Tecnologías utilizadas:

    Python con librerías como NumPy, Matplotlib y SciPy.

    Métodos numéricos avanzados para la resolución de ecuaciones diferenciales.

Este proyecto ilustra la aplicación de métodos computacionales en la astrofísica, específicamente en la simulación de órbitas planetarias con correcciones relativistas.

# Proyecto Final: Simulación del Modelo de Ising 2D

Este proyecto implementa una simulación computacional del modelo de Ising en dos dimensiones, un sistema fundamental en física estadística que describe fenómenos de magnetización y transiciones de fase. El código utiliza el algoritmo de Metrópolis para estudiar el comportamiento de una red de espines bajo diferentes condiciones termodinámicas.

## Características Principales:

1. **Implementación Completa del Modelo de Ising**:
   - Cálculo de energía y magnetización para configuraciones de espines
   - Simulación de interacciones entre vecinos más cercanos con acoplamiento J
   - Inclusión de campo magnético externo H

2. **Algoritmo de Metrópolis**:
   - Implementación eficiente del método Monte Carlo para muestreo de configuraciones
   - Condiciones de frontera periódicas para minimizar efectos de borde
   - Mecanismo de aceptación/rechazo basado en el factor de Boltzmann

3. **Análisis Termodinámico**:
   - Estudio de la evolución temporal de energía y magnetización
   - Comparación entre arranques en frío (todos los espines +1) y caliente (aleatorio)
   - Cálculo de cantidades termodinámicas: calor específico y susceptibilidad magnética

4. **Identificación de Transiciones de Fase**:
   - Determinación del punto crítico Tc a partir de picos en el calor específico
   - Comparación con el valor teórico exacto para red cuadrada 2D
   - Estudio de efectos de tamaño finito en la transición de fase

## Resultados Destacados:

- **Comportamiento de la magnetización**: Disminución desde valores altos a bajos con aumento de temperatura
- **Punto crítico teórico**: Tc ≈ 2.269 (en unidades de J/kB) para el modelo de Ising 2D
- **Comportamiento del calor específico**: Divergencia en el punto crítico indicando transición de fase de segundo orden
- **Dependencia del tamaño**: El máximo del calor específico escala con el tamaño de la red

## Aplicaciones:
- Educación en física estadística y mecánica estadística
- Estudio de transiciones de fase y fenómenos críticos
- Introducción a métodos de Monte Carlo en sistemas interactuantes
- Análisis de sistemas magnéticos y su comportamiento colectivo

Este proyecto combina conceptos fundamentales de física teórica con técnicas computacionales avanzadas, proporcionando una herramienta educativa para entender fenómenos colectivos en sistemas complejos y la implementación de algoritmos de simulación estadística.
