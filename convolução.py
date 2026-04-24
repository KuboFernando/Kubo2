import numpy as np
import matplotlib.pyplot as plt

# 1. Tempo
t = np.linspace(0, 2*np.pi, 200)

# 2. Sinais
f = np.sin(t)      # seno
g = np.cos(t)      # cosseno

# 3. Tamanho da convolução
N = len(f) + len(g) - 1

# 4. FFT
F = np.fft.fft(f, N)
G = np.fft.fft(g, N)

# 5. Multiplicação (domínio da frequência)
H = F * G

# 6. Transformada inversa
h = np.fft.ifft(H)
h = np.real(h)

# 7. Comparação com convolução direta
h_direto = np.convolve(f, g, mode='full')

# 8. Gráficos
plt.figure(figsize=(10,7))

plt.subplot(4,1,1)
plt.plot(t, f)
plt.title("Sinal 1: seno")

plt.subplot(4,1,2)
plt.plot(t, g)
plt.title("Sinal 2: cosseno")

plt.subplot(4,1,3)
plt.plot(h)
plt.title("Convolução via FFT")

plt.subplot(4,1,4)
plt.plot(h_direto, '--')
plt.title("Convolução direta")

plt.tight_layout()
plt.show()
