import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
v1 = 1500
v2 = 2500
z = 500
f = 20 #hz


x = np.linspace(200, 5000, 24)


dt = 0.002
t = np.arange(0, 3.6, dt)


sismograma = np.zeros((len(t), len(x)))


theta = np.arcsin(v1 / v2)
xcrit = 2 * z * np.tan(theta) #distancia critica

t_dir = x / v1
t_ref = np.sqrt(x**2 + 4*z**2) / v1
t_refr = x/v2 + 2*z*np.cos(theta)/v1

# Wavelet Ricker
def ricker(t, f):
    a = (np.pi * f * t)**2
    return (1 - 2*a) * np.exp(-a)

#construção do sismograma
for i in range(len(x)):

    #onda direta
    sismograma[:, i] += ricker(t - t_dir[i], f)

    #onda refletida
    sismograma[:, i] += ricker(t - t_ref[i], f)

    #onda refratada
    if x[i] >= xcrit:
        sismograma[:, i] += ricker(t - t_refr[i], f)


plt.figure(figsize=(10, 7))

for i in range(len(x)):
    plt.plot(x[i] + 65*sismograma[:, i], t, color="black", linewidth=0.8) #65 para melhorar a imagem da ricker

plt.xlim(0, 5200)
plt.ylim(0, 3.6)

plt.xlabel("Distância (m)")
plt.ylabel("Tempo (s)")
plt.title("(a) Sismograma sintético")

plt.tight_layout()
plt.show()