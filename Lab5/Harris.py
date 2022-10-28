import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('img_2.png')

operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# изменить тип данных
# установка 32-битной плавающей запятой
operatedImage = np.float32(operatedImage)

# применить метод cv2.cornerHarris
# для определения углов с соответствующими
# значения в качестве входных параметров
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.2)

# Результаты отмечены через расширенные углы
dest = cv2.dilate(dest, None)

# Возвращаясь к исходному изображению,
# с оптимальным пороговым значением
image[dest > 0.01 * dest.max()] = [139, 0, 255]
# Возвращаясь к исходному изображению,
# с оптимальным пороговым значением
img_blank = np.zeros(image.shape)
img_blank[dest > 0.05 * dest.max()] = [139, 0, 255]
image = cv2.resize(image, dsize=(1200, 700), interpolation=cv2.INTER_CUBIC)

# окно с выводимым изображением с углами
cv2.imshow('Image with Borders', image)
# окно с выводимым изображением с углами
img_blank = cv2.resize(img_blank, dsize=(1200, 700), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image with Borders2', img_blank)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()




