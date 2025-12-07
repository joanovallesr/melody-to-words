import sounddevice as sd
import numpy as np

# Settings
duration = 10  # seconds
sample_rate = 44100  # Cd quality audio
chunksize = 2048  # samples

def process_audio(indata, frames, time, status):
    """Callback function to process audio chunks."""
    if status:
        print(status)
    
    audio = indata[:, 0]  # Use the first channel
    fft_result = np.fft.rfft(audio)
    magnitude = np.abs(fft_result[: len(fft_result) // 2])
    
    # Simplified band analysis
    bands = np.array_split(magnitude, 5)
    band_levels = [int(np.max(b)) for b in bands]
    print("Low -> High:", band_levels)

print("Listening... Press Ctrl+C to stop.")
with sd.InputStream(callback=process_audio,
                    channels=1,
                    samplerate=sample_rate,
                    blocksize=chunksize):
    sd.sleep(duration * 1000)