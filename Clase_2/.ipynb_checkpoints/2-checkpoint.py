import cv2 #librería necesaria para importar imagenes
import numpy as np
from matplotlib import pyplot as plt

#images: imagen de estrada, puede ser a escala de grises o colores.
#channels: índice de canal para el cual deseamos calcular el histograma, en una imagen a escala de grises [0], si la imagen es a colores podemos indicar [0], [1], [2] para los canales B, G, R respectivamente.
#mask: mascara que define la región sobre la que deseamos calcular el histograma, es opcional.
#histSize: intensidad máxima, para nosotros [256].
#ranges: nuestro rango de valores, usaremos [0, 256].

img1 = cv2.imread('GATITA.jpg')
#Se convierte la imagen leida de BGR A RGB
img1= cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2 = cv2.imread('GATITA.jpg')
#Se convierte la imagen leida de BGR A RGB
img2= cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img3 = cv2.imread('GATITA.jpg')
#Se convierte la imagen leida de BGR A RGB
img3= cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)

img4 = cv2.imread('GATITA.jpg')
#Se convierte la imagen leida de BGR A RGB
img4= cv2.cvtColor(img4,cv2.COLOR_BGR2RGB)


#diseñamos los subplots
fig, axs= plt.subplots(nrows=2, ncols=2, figsize=(8,8))

#Mostrar las imagenes en cada subplot

axs[0,0].imshow(img1)
axs[0,0].axis("off")

axs[1,0].imshow(img2)
axs[1,0].axis("off")

axs[0,1].imshow(img3)
axs[0,1].axis("off")

axs[1,1].imshow(img4)
axs[1,1].axis("off")


plt.show()

cv2.destroyAllWindows()