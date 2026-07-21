import numpy as np
import matplotlib.pyplot as plt


d = 500 # metros
v1 = 1500 # camada 1 (m/s) velocidade na água
v2 = 2000 # camada 2 (m/s)
x = np.linspace(0, 5000, 500)

#onda direta 
w_direta = x/v1

#Onda refletida
w_refl = (((x**(2))+(4*d**(2)))**(1/2))/v1


# Critical refraction
theta_c = (np.arcsin(v1/v2)) #resposta em radianos


#Onda refratada
w_refr = (x/v2) + (2*d*np.cos(theta_c))/v1


#plot 
plt.figure(figsize= (8,5))

plt.plot(x, w_direta, label='Onda direta')
plt.plot(x, w_refl, label='Onda refletida')
plt.plot(x, w_refr, label='Onda refratada')
plt.xlabel('Distancia em x (m)')
plt.ylabel('Tempo (s)')
plt.title('Imagem (b)')
plt.grid()
plt.legend()
plt.show()