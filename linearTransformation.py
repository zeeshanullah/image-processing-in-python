import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

image = np.fromfile("image.raw", dtype='int16', sep="").reshape([512,512])

imagecopy = image.copy()

minimum = np.min(image)
maximum = np.max(image)

for i in range(len(image)):
    for j in range(len(image[i])):
        pixel = (image[i][j] - minimum)/(maximum - minimum) * 255
        imagecopy[i][j] = pixel

ax = plt.subplots(figsize=(10, 10))
plt.imshow(imagecopy)
plt.title("Linear transformation")
plt.show()
