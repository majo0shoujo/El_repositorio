import cv2
from matplotlib import pyplot as plt


img = cv2.imread('yeah.jpg', 0)
img2 = img.copy()


(row, col) = img.shape
for i in range(row):
    for j in range(col):
        if (img[i][j] < 10):
            img2[i][j] = 10
        if (img[i][j] > 240):
            img2[i][j] = 240


f_max = img2.max()
f_min = img2.min()
img3 = img2.copy()
for i in range(row):
    for j in range(col):
        img3[i][j] = ((img2[i][j] - f_min) / (f_max - f_min)) * 256


fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(8, 8))


axs[0][0].imshow(img, cmap="gray")
axs[0][0].axis("off")

axs[0][1].hist(img.ravel(), 256, [0, 256], color='gray')
axs[0][1].set_title('Histograma de la imagen original')


axs[1][0].imshow(img2, cmap="gray")
axs[1][0].axis("off")

axs[1][1].hist(img2.ravel(), 256, [0, 256], color='gray')
axs[1][1].set_title('Histograma de la imagen sin estirar')



axs[2][0].imshow(img3, cmap="gray")
axs[2][0].axis("off")

axs[2][1].hist(img3.ravel(), 256, [0, 256], color='gray')
axs[2][1].set_title('Histograma de la imagen normalizada')



plt.show()
