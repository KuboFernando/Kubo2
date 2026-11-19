import numpy as np
import matplotlib.pyplot as plt

v = 1500
z = 500
zeta = np.radians(10)

x = np.linspace(-2000, 2000, 1000)

t_refl = np.sqrt(x**2 + 4*z**2) / v
t_refl_inclinado = np.sqrt(x**2 + 4*z**2 + 4*z*x*np.sin(zeta)) / v

plt.figure(figsize=(12, 7))

#plt.plot(rx, t_refr, label="Onda refratada")
plt.plot(x, t_refl, label="Onda refletida")
#plt.plot(rx, t_dir, label="Onda direta")
plt.plot(x, t_refl_inclinado, label="Onda Refletida Inclinada")
plt.xlabel("Offset (m)")
plt.ylabel("Tempo (s)")
plt.title("Split Spread")

plt.grid(True)
plt.legend()

plt.show()