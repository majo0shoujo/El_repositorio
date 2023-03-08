
#import cv2

# Lee una imagen y la guarda en una matriz de NumPy
#imagen = cv2.imread('GATITA.jpg')

# Muestra la imagen en una ventana
#cv2.imshow('GATITA.jpg', imagen)

# Espera hasta que el usuario presione una tecla
#cv2.waitKey(0)

# Cierra todas las ventanas abiertas
#cv2.destroyAllWindows()

import cv2
from matplotlib import pyplot as plt

# Lee la imagen
img = cv2.imread('GATITA.jpg')

img=cv2.cvtColor (img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()