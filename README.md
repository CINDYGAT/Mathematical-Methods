# Mathematical-Methods

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
