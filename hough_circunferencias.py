import cv2
import numpy as np

# Cargar la imagen del motor y pasarla a escala de grises
img = cv2.imread("motor.png")
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Suavizar para reducir ruido antes de la transformada
gris = cv2.GaussianBlur(gris, (5, 5), 0)

# Transformada de Hough para detectar circunferencias
circunferencias = cv2.HoughCircles(gris, cv2.HOUGH_GRADIENT, dp=1,
minDist=40, param1=100, param2=40, minRadius=15, maxRadius=45)

# Dibujar las circunferencias detectadas sobre la imagen original
salida = img.copy()
if circunferencias is not None:
    circunferencias = np.round(circunferencias[0]).astype(int)
    for (x, y, r) in circunferencias:
        cv2.circle(salida, (x, y), r, (0, 255, 0), 2)
        cv2.circle(salida, (x, y), 2, (0, 0, 255), 3)
    print(f"Circunferencias detectadas: {len(circunferencias)}")
else:
    print("No se detectaron circunferencias, ajustar parametros.")

cv2.imwrite("motor_circunferencias.jpg", salida)