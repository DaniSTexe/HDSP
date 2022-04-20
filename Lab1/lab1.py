import cv2 
import sys
from os import stat
import numpy

imagen = cv2.imread('./coins.png')
imagen2 = cv2.imread('./coins.jpg')
imagen3 = cv2.imread('./coins5.jpg')
imagen4 = cv2.imread('./parrots.tif')

print(sys.getsizeof(imagen))
print(sys.getsizeof(imagen2))
print(sys.getsizeof(imagen3))
print(sys.getsizeof(imagen4))

nombre = './lab1.mlx'
informacion = stat(nombre)
print(f'tamaño {imagen.nbytes}')
print(f'tamaño {imagen2.nbytes}')
print(f'tamaño {imagen3.nbytes}')
print(f'tamaño {imagen4.nbytes}')



#image_rgb = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
cv2.imshow('ok',imagen)
cv2.waitKey()
cv2.destroyAllWindows()
