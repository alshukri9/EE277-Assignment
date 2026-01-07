import numpy as np
import matplotlib.pyplot as plt

# 1. Generate a random signal (White Noise filtered to create correlation)
np.random.seed(42)
fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)
# Creating a signal: White noise smoothed by a moving average (adds correlation)
raw_noise = np.random.normal(0, 1, len(t))
signal = np.convolve(raw_noise, np.ones(50)/50, mode='same')

# 2. Calculate Autocorrelation
# We use np.correlate; 'same' ensures the output size matches input
autocorr = np.correlate(signal, signal, mode='full')
lags = np.arange(-len(signal) + 1, len(signal))

# 3. Calculate PSD using FFT
# Periodogram estimate: |FFT|^2 / N
sig_fft = np.fft.fft(signal)
psd = (np.abs(sig_fft)**2) / len(signal)
freqs = np.fft.fftfreq(len(signal), 1/fs)

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Autocorrelation Plot
ax1.plot(lags, autocorr)
ax1.set_title("Autocorrelation Function")
ax1.set_xlabel("Lag")
ax1.set_ylabel("Amplitude")

# PSD Plot (only showing positive frequencies)
idx = np.where(freqs >= 0)
ax2.semilogy(freqs[idx], psd[idx])
ax2.set_title("Power Spectral Density (PSD)")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Power/Frequency")

plt.tight_layout()
plt.show()