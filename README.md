# python

NOMBRE FRANCO ALCONADA

DNI 44960966

# 🕹️ Actividad 2 – Ranking de Jugadores (Seminario Python)

Este repositorio contiene la resolución del ejercicio 10 de la **Actividad 2** del seminario de Python. El programa permite procesar datos de múltiples partidas de un juego, calcular estadísticas por jugador y determinar quién fue el MVP (jugador más valioso) en cada ronda. Los resultados se muestran en forma de ranking ordenado por puntaje.


## ⚙️ Requisitos

Para poder correr este proyecto correctamente, necesitás tener:

- **Python 3.12.9**
- **Jupyter Notebook** (para visualizar y ejecutar el notebook)

Además, si querés instalar todo de una, podés usar el archivo `requirements.txt` que trae las librerías necesarias.

---

## 🚀 Instalación

Cloná este repositorio y luego, desde tu consola, ejecutá:

```bash
pip install -r requirements.txt
```

Esto va a instalar las dependencias necesarias para que todo funcione sin problemas.



## ▶️ Cómo ejecutar el proyecto

1. **Abrir el Jupyter Notebook**  
   Desde la raíz del proyecto, ejecutá:

   ```bash
   jupyter notebook
   ```

   Esto abrirá una interfaz web donde podés navegar a la carpeta `notebooks/` y abrir el archivo `.ipynb` para probar el código.

2. **Visualizar los resultados**  
   Al ejecutar las celdas del notebook, se va a mostrar el ranking por ronda y también se va a identificar al MVP de cada partida.



## 📌 ¿Qué hace este proyecto?

El programa trabaja con datos simulados de varias rondas de un videojuego y realiza lo siguiente:

- Procesa las estadísticas de cada jugador (kills, asistencias, muertes)
- Calcula puntos en base a esos valores
- Ordena a los jugadores por puntaje en cada ronda
- Cuenta cuántas veces cada jugador fue MVP
- Muestra un ranking final con todas las estadísticas acumuladas



## 🧠 Funciones principales

- **`calcular_puntos`**: genera el puntaje de un jugador a partir de sus estadísticas.
- **`generar_ranking`**: crea un ranking por ronda.
- **`determinar_mvp`**: identifica al mejor jugador de la ronda.
- **`procesar_datos`**: actualiza las estadísticas globales y suma los MVPs.
