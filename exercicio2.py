import numpy as np
import matplotlib.pyplot as plt
#ricker central
def ricker_peak(t, fp):
    return (1 - 2*(np.pi*f*t)**2) * np.exp(-(np.pi*f*t)**2)

#ricker frequencia de corte
def ricker_cut(t,fc):
    fc = f/(3*np.sqrt(np.pi))
    return -(2*np.pi*(np.pi*fc*t)**2 - 1) * np.exp(-np.pi*(np.pi*fc*t)**2)

def seno(t,f):
    return np.sin(2*np.pi*f*t)

#programa principal
dt = 0.001
T = 0.5
t = np.arange(-T, T, dt)
f = 80

ricker_corte = ricker_cut(t,f)
ricker_central = ricker_peak(t,f)
sin = seno(t,f)
#plot
plt.figure(figsize=(8,5))
#plt.plot(t, sin , label ='Seno')
plt.plot(t, ricker_central, label='Ricker pela frequência central')
plt.plot(t, ricker_corte, label='Ricker pela frequência de corte')
plt.plot(t, sin, label='seno')
plt.title('Comparação entre Ricker por frequência central e frequência de corte')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
#plt.show()

#frequencias
freq = np.fft.fftfreq(len(t), dt)

#FFT wavelets
fft_central = np.fft.fft(ricker_central)
fft_corte = np.fft.fft(ricker_corte)
fft_sin = np.abs(np.fft.fft(sin))


fft_sin_power = np.real(fft_sin**2)
fft_central_power = np.real(fft_central**2)
fft_corte_power = np.real(fft_corte**2)

fft_sin_power = fft_sin_power/np.max(fft_sin_power)
fft_central_power = fft_central_power/np.max(fft_central_power)
fft_corte_power = fft_corte_power/np.max(fft_corte_power)

#amplitude
#amp_central = np.fft.fft(fft_central)
#mp_corte = np.fft.fft(fft_corte)


#melhorar a frequencia
#freq = np.fft.fftshift(freq)
#amp_central = np.fft.fftshift(amp_central)
#amp_corte = np.fft.fftshift(amp_corte)

#normalizar
#amp_central = amp_central / np.max(amp_central)
#amp_corte = amp_corte / np.max(amp_corte)

#plot
plt.figure(figsize = (8,5))

plt.plot(freq, fft_central_power, label = 'Espectro Ricker frequencia central')
plt.plot(freq, fft_corte_power, label = 'Espectro Ricker frequencia de corte' )
plt.plot(freq, fft_sin, label = 'Espectro seno' )
plt.title('Espectro das wavelets Ricker')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude normalizada')
plt.xlim(0, 150)
plt.grid(True)
plt.legend()
plt.show()


#calcular o espectro a partir do grafico de cada uma das rickers
#Usando FFT
#Resposta : no cara azul q tem pico de amplitudo 45Hz 
#No cara laranja tem q ter o minimo em 45Hz


#resolver o problema do grafico do espectro(normalização)


# Prox etapa estudar metodo de aquisição CMP + levantamento OBN  
#Voltar ao Kearey


#ler seção 3.7
#Reproduzir a figura 3.13 (b)