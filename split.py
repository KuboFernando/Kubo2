import numpy as np
import matplotlib.pyplot as plt

sx = 120  # source 
sy = 0
d_rec = 12.5 # metros
offset_min = 0 # metros
offset_max = 400 # metros

rx_esq = np.arange(-offset_max, -offset_min + d_rec, d_rec)
rx_dir = np.arange(offset_min, offset_max + d_rec, d_rec)

rx = np.concatenate((rx_esq,rx_dir))

ry = np.full(len(rx), sy)

plt.figure(figsize= (12,4))

plt.scatter(rx, ry, label = 'Receptores')
plt.scatter(sx, sy, marker= '*', s = 200, label = 'Fonte')

plt.xlabel('Distância')
plt.ylabel('Y')
plt.grid(True)
plt.legend()


offset = np.abs(rx - sx)

v1 = 1500 
v2 = 3000
z = 1000

x = np.arange(150, 8000, 12.5) # offsets

t_refl = np.sqrt(offset**2 + 4*z**2)/v1


theta = np.degrees(np.arcsin(v1/v2))
t_refr = (offset/v2) + (2*z*np.cos(theta))/v1

t_dir = offset / v1
plt.figure(figsize=(12, 7))
plt.plot(rx, t_dir, label="Onda direta")
plt.plot(rx, t_refl, label="Onda refletida")
plt.plot(rx, t_refr, label="Onda refratada")
plt.xlabel("Offset (m)")
plt.ylabel("Tempo (s)")

plt.grid(True)
plt.legend()

plt.show()