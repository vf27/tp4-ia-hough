# TP4 IA - Transformada de Hough

Prototipos en Python con OpenCV para detectar rectas y circunferencias
en la imagen de un block de motor.
Corresponde al Trabajo Practico 4 de Inteligencia Artificial.

## Archivos

- `hough_rectas.py`: detecta rectas con la transformada de Hough probabilistica.
- `hough_circunferencias.py`: detecta circunferencias con la transformada de Hough.
- `motor.png`: imagen de entrada. Fuente: Walter Tools.
- `resultados/`: imagenes generadas por los prototipos.

## Requisitos

- Python 3
- opencv-python
- numpy

## Ejecucion
- pip install opencv-python numpy
- python hough_rectas.py
- python hough_circunferencias.py

Cada script carga `motor.png`, la procesa y guarda las imagenes resultantes en la carpeta del proyecto.
