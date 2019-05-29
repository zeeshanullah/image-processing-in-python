import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

image = np.fromfile("image.raw", dtype='int16', sep="").reshape([512,512])

imagecopy = image.copy()

for i in range(5,len(image)-5):
    for j in range(5,len(image[i])-5):
        sum = 0
      
        for k in range(-5,6):
            for l in range(-5,6):
                sum = sum + image[i+k][j+l]
                
        imagecopy[i][j] = int(sum/121)
        
ax = plt.subplots(figsize=(10, 10))
plt.title("Boxcar smoothing filter 11x11")
plt.imshow(imagecopy)
