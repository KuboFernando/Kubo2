import numpy as np
import matplotlib.pyplot as plt

sx = 5000 
sy = 50
sz = 7
nt = 5001
dt = 0.001
time = np.linspace(0,nt*dt,nt, endpoint=False)

offset_min = (sx + 150)         # Menos distancia entre o receptor e a fonte
offset_max = (sx + 8150)

drec = 12.5 # Distancia entre receptores

rx = np.linspace(offset_min,offset_max, num = int((offset_max - offset_min)/(drec)),endpoint= False)

ry = np.full(len(rx), sy)

rz = np.full(len(rx), sz)


offset = offset_min + (rx)
vel_agua = 1500
tt = np.abs(offset/vel_agua)

print('Números de receptores:', len(rx))
print('Primeiro receptor', rx[0], ry[0], rz[0])
print('Último receptor', rx[-1], ry[-1], rz[-1])  # -1 é a última posição

plt.figure(figsize = (12,4))
plt.scatter(rx, ry, label = "Receptores")
plt.scatter(sx, sy, marker = "*", s=200, label = "Fonte")

plt.title("Aquisição sísmica")
plt.xlabel("x")
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.figure(figsize = (12,4))
plt.plot(rx,tt,"*-")
plt.show()



# Calcular o tempo de transito da reflexão em cada recptor
