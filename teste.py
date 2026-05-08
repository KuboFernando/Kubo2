import numpy as np
import matplotlib.pyplot as plt


dt = 0.001              # 1 ms
tmax = 0.2              # 200 ms
t = np.arange(-tmax, tmax, dt)

freq = np.arange(0, 140, 1)

# 1. RICKER WAVELET

f = 25

ricker = (1 - 2*(np.pi*f*t)**2) * np.exp(-(np.pi*f*t)**2)

# FFT
R = np.abs(np.fft.fft(ricker))
R = R[:len(freq)]
R = R / np.max(R)

# 2. ORMSBY WAVELET

f1, f2, f3, f4 = 5, 10, 40, 45

def sinc(x):
    return np.sinc(x/np.pi)

ormsby = (
    (np.pi*f4)**2 * sinc(np.pi*f4*t)**2
    - (np.pi*f3)**2 * sinc(np.pi*f3*t)**2
    - (np.pi*f2)**2 * sinc(np.pi*f2*t)**2
    + (np.pi*f1)**2 * sinc(np.pi*f1*t)**2
)

ormsby = ormsby / np.max(np.abs(ormsby))

# FFT
O = np.abs(np.fft.fft(ormsby))
O = O[:len(freq)]
O = O / np.max(O)

# 3. KLAUDER WAVELET

f0 = 25
f1k = 10
f2k = 40
T = 0.2

k = (f2k - f1k)/T

f0 = (f2k + f1k)/2

klauder = np.real((np.sin(np.pi*k*t*(T - t))/(np.pi*k*t))*np.exp(2j*np.pi*f0*t))
###Foi oq deu problema
# FFT
K = np.abs(np.fft.fft(klauder))
K = K[:len(freq)]
K = K / np.max(K)

# 4. BUTTERWORTH WAVELET
n = 4
fc = 25

butter = 1 / np.sqrt(1 + (freq/fc)**(2*n))
butter = butter / np.max(butter)

# Transformada inversa
bw_time = np.real(np.fft.ifft(butter, n=len(t)))
bw_time = np.fft.fftshift(bw_time)
bw_time = bw_time / np.max(np.abs(bw_time))


fig, ax = plt.subplots(4, 2, figsize=(16,9))

ax[0,0].plot(t*1000, ricker)
ax[0,0].set_title("25 Hz Ricker Wavelet")
ax[0,0].set_xlabel("time (ms)")
ax[0,0].set_ylabel("amplitude")

ax[0,1].plot(freq, R)
ax[0,1].set_title("Ricker Spectrum")
ax[0,1].set_xlabel("frequency (Hz)")
ax[0,1].set_ylabel("density")


ax[1,0].plot(t*1000, ormsby)
ax[1,0].set_title("5-10-40-45 Hz Ormsby Wavelet")
ax[1,0].set_xlabel("time (ms)")
ax[1,0].set_ylabel("amplitude")

ax[1,1].plot(freq, O)
ax[1,1].set_title("Ormsby Spectrum")
ax[1,1].set_xlabel("frequency (Hz)")
ax[1,1].set_ylabel("density")

ax[2,0].plot(t*1000, klauder)
ax[2,0].set_title("Klauder Wavelet")
ax[2,0].set_xlabel("time (ms)")
ax[2,0].set_ylabel("amplitude")

ax[2,1].plot(freq, K)
ax[2,1].set_title("Klauder Spectrum")
ax[2,1].set_xlabel("frequency (Hz)")
ax[2,1].set_ylabel("density")


ax[3,0].plot(t*1000, bw_time)
ax[3,0].set_title("Butterworth Wavelet")
ax[3,0].set_xlabel("time (ms)")
ax[3,0].set_ylabel("amplitude")

ax[3,1].plot(freq, butter)
ax[3,1].set_title("Butterworth Spectrum")
ax[3,1].set_xlabel("frequency (Hz)")
ax[3,1].set_ylabel("density")


plt.tight_layout()
plt.show()


#fazer o gráfico de uma sinc sozinha e da transformada de fourier dela (igual ao livro pag 17)
#2 grafico, um pulso unitario e aplicar a transformada de fourier nele
# Desenhar uma caixa no dominio da frequencia de 10 Hz a caixa termine 
# dps pega a caixa e multiplica pela transformada de fourier do pulso unitario
# No resultado aplicar a inversa da transformada de fourier
