import numpy as np
import matplotlib.pyplot as plt

#função sinc
x = np.linspace(-10, 10, 1000)
fs = np.sinc(x)
#FFT da sinc
S = np.abs(np.fft.fftshift(np.fft.fft(fs)))
#fft coloca o 0 hz no começo
#fftshift é para colocar o 0Hz no centro


# eixo de frequência
dx = x[1]-x[0]
f = np.fft.fftshift(np.fft.fftfreq(len(x),dx))

#plot
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(x,fs)
plt.title("Função sinc")
plt.xlabel("Tempo")
plt.grid()

plt.subplot(1,2,2)
plt.plot(f,S)
plt.title("FFT da sinc")
plt.xlabel("Frequência")
plt.grid()

plt.tight_layout()
plt.show()


#parte 2
N=1000

pulso=np.zeros(N)

#para ser no centro escolhi 12 numeros pra frente e 12 para tras a partir do centro 

#pulso no centro
pulso[500]=1

fft_pulso=np.fft.fftshift(np.fft.fft(pulso))

freq=np.fft.fftshift(np.fft.fftfreq(N,1))


#plot 2
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(pulso)
plt.title("Pulso unitário")

plt.subplot(1,2,2)
plt.plot(freq,np.abs(fft_pulso))
plt.title("FFT do pulso")

plt.tight_layout()
plt.show()

#parte 3
caixa=np.zeros(N)

#frequencia = -10 e +10 Hz
caixa[np.abs(freq)<=0.01]=1

#plot 3
plt.figure()
plt.plot(freq,caixa)
plt.title("Filtro caixa")
plt.xlabel("Frequência")
plt.xlim(-0.05,0.05)
plt.grid()
plt.show()


#parte 4
filtrado=fft_pulso*caixa

#plot 4
plt.figure()
plt.plot(freq,np.abs(filtrado))
plt.title("FFT x Caixa")
plt.xlim(-0.05,0.05)
plt.grid()
plt.show()

#parte tomara q de certo
resultado=np.fft.ifft(np.fft.ifftshift(filtrado))

#plot tomara q de certo
plt.figure()
plt.plot(np.real(resultado))
plt.title("Resultado após IFFT")
plt.grid()
plt.show()