import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
sx = 0
sy = 0

offset_min = 0
offset_max = 8000
d_rec = 12.5

v1 = 1500
v2 = 2000
z = 500
zeta = np.radians(10)

# Geometria Split Spread
rx_esq = np.arange(-offset_max, -offset_min + d_rec, d_rec)
rx_dir = np.arange(offset_min, offset_max + d_rec, d_rec)

rx = np.concatenate((rx_esq, rx_dir))
ry = np.full(len(rx), sy)

# Plot da geometria
plt.figure(figsize=(12, 4))

plt.scatter(rx, ry, s=5, label="Receptores")
plt.scatter(sx, sy, marker="*", s=200, label="Fonte")

plt.xlabel("Distância (m)")
plt.ylabel("Y")
plt.title("Geometria Split Spread")
plt.grid(True)
plt.legend()
plt.show()

# Offset
x = rx - sx
offset = np.abs(x)

# Onda direta
t_dir = offset / v1

# Onda refletida horizontal
t_refl = np.sqrt(offset**2 + 4*z**2) / v1

# Onda refletida inclinada
t_refl_inclinado = np.sqrt(offset**2 + 4*z**2 + 4*z*x*np.sin(zeta))/v1

# Onda refratada
theta = np.arcsin(v1 / v2)

t_refr = offset/v2 + (2*z*np.cos(theta))/v1

# Plot dos tempos
plt.figure(figsize=(12, 7))

plt.plot(x, t_dir, label="Onda direta")
plt.plot(x, t_refr, label="Onda refratada")
plt.plot(x, t_refl, label="Onda refletida")
plt.plot(x, t_refl_inclinado, label="Onda refletida inclinada")

plt.xlabel("Offset (m)")
plt.ylabel("Tempo (s)")
plt.title("Split Spread")

plt.grid(True)
plt.legend()
plt.show()