import cv2
import numpy as np

# Cargar la imagen del motor y pasarla a escala de grises
img = cv2.imread("motor.png")
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Suavizar para reducir ruido y detectar bordes con Canny
gris = cv2.GaussianBlur(gris, (5, 5), 0)
bordes = cv2.Canny(gris, 50, 150)
cv2.imwrite("motor_bordes.jpg", bordes)

# Transformada de Hough probabilistica para detectar rectas
rectas = cv2.HoughLinesP(bordes, 1, np.pi/180, threshold=80, minLineLength=60, maxLineGap=10)
# Dibujar las rectas detectadas sobre la imagen original
salida = img.copy()
if rectas is not None:
    for linea in rectas:
        x1, y1, x2, y2 = linea
        cv2.line(salida, (x1, y1), (x2, y2), (0, 255, 0), 2)
    print(f"Rectas detectadas: {len(rectas)}")
else:
    print("No se detectaron rectas, ajustar parametros.")

cv2.imwrite("motor_rectas.jpg", salida)
