import numpy as np
import scipy.io.wavfile as wavfile

# Load the audio file
sample_rate, data = wavfile.read('piano.wav')

# If stereo, convert to mono by averaging channels
if len(data.shape) == 2:
    data = np.mean(data, axis=1)

# Perform FFT to convert to frequency domain
fft_result = np.fft.fft(data)
fft_frequencies = np.fft.fftfreq(len(fft_result), d=1/sample_rate)

# Convert complex FFT results to magnitude
magnitude = np.abs(fft_result)

# Keep only the positive frequencies
positive_freqs = fft_frequencies[: len(fft_frequencies) // 2]
positive_magnitude = magnitude[: len(magnitude) // 2]

# Identify the top 5 frequencies with the highest magnitude
top_indices = positive_magnitude.argsort()[-5:][::-1]
top_frequencies = positive_freqs[top_indices]

# Print the top 5 frequencies
print("Top 5 Frequencies (Hz):")
for freq in top_frequencies:
    print(f"{freq:.2f} Hz")