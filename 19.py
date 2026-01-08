import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

length = 1000

data = np.random.uniform(-1, 1, length)

autocorr = np.correlate(data, data, mode='full')

# divide by maximum correlation at lag = 0 this will make the data appear as ratio
autocorr = autocorr / np.max(autocorr)

lags = np.arange(-length + 1, length)

fs = 1.0 
frequencies, psd = signal.welch(data, fs, nperseg=20)

fig, axes = plt.subplots(3, 1, figsize=(10, 12))
plt.subplots_adjust(hspace=0.4)

axes[0].plot(data, color='blue', lw=0.5, alpha=0.7)
axes[0].set_title(f"Time Domain: Random Signal")
axes[0].set_ylabel("Amplitude")

axes[1].plot(lags, autocorr, color='green')
axes[1].set_title("Autocorrelation Function")
axes[1].set_xlabel("Lag")
axes[1].set_ylabel("Normalized Correlation")
axes[1].set_xlim([-100, 100])

axes[2].plot(frequencies, psd, color='red')
axes[2].set_title("Power Spectral Density (PSD)")
axes[2].set_xlabel("Frequency (Hz)")
axes[2].set_ylabel("Power/Frequency (Watt/Hz)")

plt.show()