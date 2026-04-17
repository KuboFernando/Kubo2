import numpy as np
import matplotlib.pyplot as plt

# 1. Modelo geológico (camadas)
nz = 1200 
dz = 1
d = np.linspace(0,(nz*dz),nz)


vel = np.zeros(nz)
rho = np.zeros(nz)

sdv = 1800
shv = 1400
lmv = 2600
igv = 3200

vel[0:150] = sdv
vel[150:300] = shv
vel[300:450] = sdv
vel[450:600] = shv
vel[600:750] = lmv
vel[750:900] = sdv
vel[900:1050] = igv
vel[1050:] = sdv

sdr = 2000
shr = 1900
lmr = 2200
igr = 2350

rho[0:150] = sdr
rho[150:300] = shr
rho[300:450] = sdr
rho[450:600] = shr
rho[600:750] = lmr
rho[750:900] = sdr
rho[900:1050] = igr
rho[1050:] = sdr

# 2. Impedância acústica (modelo em degraus)
Z = rho * vel


# 3. Coeficientes de reflexão

R = np.zeros(nz)
for i in range(1, nz):
    R[i] = (Z[i] - Z[i-1]) / (Z[i] + Z[i-1])

# 4. Função refletividade
refletividade = R

# 5. Pulso sísmico
hz = 30
dt = 0.001
length = (3/hz)

tw = np.arange(-length/2, length/2, dt)
wavelet = (1 - 2*(np.pi*hz*tw)**2) * np.exp(-(np.pi*hz*tw)**2)


# 6. Traço sísmico
traco_sismico = np.convolve(refletividade, wavelet, mode='same')


# 7. Plots
fig, ax = plt.subplots(1,5, figsize=(16,8))

ax[0].plot(Z, d)
ax[0].set_title("Acoustic Impedance")
ax[0].invert_yaxis()

ax[1].plot(R, d)
ax[1].set_title("Reflection Coefficient")
ax[1].invert_yaxis()

ax[2].plot(refletividade, d)
ax[2].set_title("Reflectivity")
ax[2].invert_yaxis()

ax[3].plot(wavelet, tw)
ax[3].set_title("Input Pulse")

ax[4].plot(traco_sismico, d)
ax[4].set_title("Seismic Trace")
ax[4].invert_yaxis()

# Ajustar o espaçamento
plt.tight_layout() 
# Mostrar o plot
plt.show()
