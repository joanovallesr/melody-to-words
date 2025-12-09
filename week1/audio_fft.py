import sys
import os

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the week3 directory
week3_path = os.path.join(current_dir, '../week3')

# Add the week3 directory to the system path
sys.path.append(week3_path)

import numpy as np
import scipy.io.wavfile as wavfile
import melody_to_notes as mtn

# Load the audio file
sample_rate, data = wavfile.read('piano.wav')

# If audio has 2 channels (stereo), convert to mono by averaging channels
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

# Convert top frequencies to note names and print them
print("Detected Notes:")
for freq in top_frequencies:
    print(mtn.frequency_to_note_name(freq))