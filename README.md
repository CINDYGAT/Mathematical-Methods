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
