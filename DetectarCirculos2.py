import cv2
import numpy as np

imRuta = r"C:\Users\guillermo.gavotti\Desktop\IA TP3\imagen.jpg"

imagen = cv2.imread(imRuta, cv2.IMREAD_COLOR)

imGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)# Se convierte la imagen a escala de grises

imLimpia = cv2.GaussianBlur(imGris, (5, 5), 0)# Se reduce el ruido

imCanny = cv2.Canny(imLimpia, 10,10)

cv2.imshow("Im Canny",imCanny)

circulos = cv2.HoughCircles(imCanny, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=80, param2=30, minRadius=80, maxRadius=85) #Se detecta el circulo que cumple con las caracteristicas buscadas en la imagen canny

if circulos is not None:
    x,y,r = circulos[0][0]   
    
    centroRedondeado = (int(round(x)), int(round(y)))
    radioRedondeado = (int(round(r)))

    cv2.circle(imagen,centroRedondeado, radioRedondeado, (0, 500, 0), 3) #Se dibujan los circulos en la imagen original
    cv2.circle(imagen,centroRedondeado, 1, (0, 0, 500), 3)

    cv2.imshow("Círculos ", imagen)
    cv2.waitKey(0)
else:
    print("Error. No se detectó la ranura de ensamble")
