import numpy as np
import matplotlib.pyplot as plt


sx = 4000
sy = 0

offset_min = 150
offset_max = 8000
d_rec = 12.5
zeta = np.radians(50)
rx_esq = np.arange(- offset_max, - offset_min + d_rec, d_rec)
rx_dir = np.arange(offset_min, offset_max + d_rec, d_rec)

rx = np.concatenate((rx_esq, rx_dir))
ry = np.full(len(rx), sy)

plt.figure(figsize=(12,4))

plt.scatter(rx, ry, label = 'Receptores')
plt.scatter(sx, sy, marker= '*', s = 200, label = 'Fonte')

plt.xlabel('Distancia')
plt.ylabel('Y')
plt.grid(True)
plt.legend()

offset = np.abs(rx - sx)
dist = np.abs(offset)
v1 = 1500
v2 = 2000
z = 500

t_dir = offset / v1


t_refl = np.sqrt(dist**2 + 4*z**2) / v1
t_refl_inclinado = np.sqrt(dist**2 + 4*z**2 + 4*z*dist*np.sin(zeta)) / v1

#t_refl_inclinado = (2*z)/v1 * np.sqrt(1 + (offset**2 + 4*z*offset*np.sin(zeta))/4*(z)**2)
theta = np.arcsin(v1 / v2)

t_refr = ((offset / v2 )+ (2*z*np.cos(theta)) / v1)


plt.figure(figsize=(12, 7))

#plt.plot(rx, t_refr, label="Onda refratada")
plt.plot(rx, t_refl, label="Onda refletida")
#plt.plot(rx, t_dir, label="Onda direta")
plt.plot(rx, t_refl_inclinado, label="Onda Refletida Inclinada")
plt.xlabel("Offset (m)")
plt.ylabel("Tempo (s)")
plt.title("Split Spread")

plt.grid(True)
plt.legend()

plt.show()


