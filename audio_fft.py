import numpy as np
import scipy.io.wavfile as wavfile

sample_rate, data = wavfile.read('piano.wav')

if len(data.shape) == 2:
    data = np.mean(data, axis=1) # Convert to mono by averaging channels

fft_result = np.fft.fft(data)
fft_frequencies = np.fft.fftfreq(len(fft_result), d=1/sample_rate)

magnitude = np.abs(fft_result)

positive_freqs = fft_frequencies[: len(fft_frequencies) // 2]
positive_magnitude = magnitude[: len(magnitude) // 2]

top_indices = positive_magnitude.argsort()[-5:][::-1]
top_frequencies = positive_freqs[top_indices]

print("Top 5 Frequencies (Hz):")
for freq in top_frequencies:
    print(f"{freq:.2f} Hz")