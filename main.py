import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Parâmetros do sinal
Fs = 5000           
T = 1.0 / Fs        
N = 8192            
t = np.linspace(0.0, N*T, N, endpoint=False)

f0 = 60  # Hz

signal = (1.0 * np.sin(2.0 * np.pi * f0 * t) +
          0.3 * np.sin(2.0 * np.pi * 2*f0 * t) +
          0.2 * np.sin(2.0 * np.pi * 3*f0 * t) +
          0.1 * np.sin(2.0 * np.pi * 4*f0 * t) +
          0.05 * np.sin(2.0 * np.pi * 5*f0 * t))

window = np.hanning(N)
signal_windowed = signal * window

yf = fft(signal_windowed)
xf = fftfreq(N, T)[:N//2]

magnitude = 2.0 / np.sum(window) * np.abs(yf[:N//2])

max_harmonic = 50
freq_limit = f0 * max_harmonic
indices = xf <= freq_limit

xf_lim = xf[indices]
magnitude_lim = magnitude[indices]

harmonics_freqs = f0 * np.arange(1, max_harmonic+1)
harmonics_mags = []

tolerance = f0 * 0.02  

for hfreq in harmonics_freqs:
    idx_candidates = np.where((xf_lim >= hfreq - tolerance) & (xf_lim <= hfreq + tolerance))[0]
    if len(idx_candidates) == 0:
        harmonics_mags.append(0)
    else:
        peak_idx = idx_candidates[np.argmax(magnitude_lim[idx_candidates])]
        harmonics_mags.append(magnitude_lim[peak_idx])

harmonics_mags = np.array(harmonics_mags)

fundamental_mag = harmonics_mags[0]
if fundamental_mag == 0:
    THD = 0
else:
    THD = np.sqrt(np.sum(harmonics_mags[1:]**2)) / fundamental_mag

print(f"THD: {THD*100:.2f}%")
print("\nHarmônicos detectados (Hz) e Magnitudes:")
for i, mag in enumerate(harmonics_mags, start=1):
    print(f"H{i}: {f0*i} Hz - Magnitude: {mag:.4f}")

plt.figure(figsize=(14,7))

plt.subplot(2,1,1)
plt.plot(t[:5000], signal[:5000])  # <- sinal original sem janela
plt.title('Sinal no domínio do tempo (sinal original)')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

plt.subplot(2,1,2)
plt.stem(harmonics_freqs, harmonics_mags, basefmt=" ")
plt.title('Magnitudes dos Harmônicos até o 50º')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude')
plt.xlim(0, freq_limit)
plt.grid()

plt.tight_layout()
plt.show()
