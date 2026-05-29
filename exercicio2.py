import numpy as np
import matplotlib as plt
dt = 0.001
t = np.arange(-0.1, 0.1, dt)
f = 45
#ricker
ricker = (1 - 2*(np.pi*f*t)**2) * np.exp(-(np.pi*f*t)**2)

#frequencia de corte - frequencia que delimita a banda da passagem de um filtro 
corte = (1/2)**0.5
fc = np.fft.rfftfreq(len(t), dt)
am = np.abs(np.fft.rfft(ricker))
am = am/am.max()

x = np.where(am >= corte)

fcmin = fc[x[0]]
fcmax = fc[x[-1]]
print(fcmin,fcmax)


#frequencia central - frequencia onde o espectro da wavelet é o máximo
