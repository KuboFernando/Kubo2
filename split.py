import numpy as np
import matplotlib.pyplot as plt

sx = 0  # source 
sy = 0

d_rec = 12.5 # metros
offset_min = 150 # metros
offset_max = 400 # metros

rx_esq = np.arange(-offset_max, -offset_min + d_rec, d_rec)
rx_dir = np.arange(offset_min, offset_max + d_rec, d_rec)

rx = rx_dir + rx_esq

ry = np.full(len(rx), sy)

plt.figure(figsize= (12,4))

plt.scatter(rx, ry, label = 'Receptores')
plt.scatter(sx, sy, marker= '*', s = 200, label = 'Fonte')

plt.xlabel('Distância')
plt.ylabel('Y')
plt.grid(True)
plt.legend()

plt.show()