import numpy as np
import matplotlib.pyplot as plt

v1 = 1500 
v2 = 2000
z = 500

x = np.arange(150, 8000, 12.5) # offsets

t_refl = (((x**(2))+(4*z**(2)))**(1/2))/v1

t_dir = x/v1

theta =(np.arcsin(v1/v2))
t_refr = (x/v2) + (2*z*np.cos(theta))/v1

plt.figure(figsize=(10, 6))

plt.plot(x, t_refr, label="Onda refratada")
plt.plot(x, t_refl, label ='Onda refletida')
plt.plot(x, t_dir, label ='Onda direta')
plt.xlabel("Offset")
plt.ylabel("Tempo")
plt.title("Tempo da onda refratada")

plt.grid(True)
plt.legend()

plt.show()