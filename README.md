# melody-to-words

Melody-to-Words is an assistive, music-driven speech reinforcement system designed to explore whether melody-based interactions can help encourage language development in early childhood.

This project is personal — I began developing it for my daughter, who is currently undergoing speech therapy and communicates more comfortably through music than spoken words. The goal is not to replace speech therapy, but to experiment with interactive tools that support repetition, association, and confidence through play.

## Project Motivation

Many children with speech delays:

    - Communicate more freely when melody removes pressure

    - Respond strongly to repetition and rhythm

    - Engage well with multisensory feedback (sound + visual + positive reinforcement)

If a child can press keys and hear associated words or sentences, we may create:

    - A playful environment with low verbal pressure

    - Repetition without boredom

    - A sense of control and achievement

This project explores that possibility through software and machine learning.

## How the System Works

1. Child plays melody
2. System captures audio (real-time or file)
3. Note pattern is extracted using FFT + signal processing
4. ML model maps melody → word
5. The app speaks the word using text-to-speech
6. Repetition reinforces association


## How FFT Helps Machine Learning Understand Sound

Raw audio is a continuous, unstructured waveform — machines cannot meaningfully learn from it as-is.

Fast Fourier Transform (FFT) converts sound into frequency components, separating complex waves into individual sine waves with measurable:

    - Frequency (pitch)

    - Amplitude (volume)

    - Phase (timing)

This transforms sound into numerical features — a format suitable for machine learning models.

## Curren Stage: Frequency Peak Extractio

This repository currently includes:

    - A Python script (audio_fft.py) that:

        1. Loads a .wav file

        2. Converts the waveform into frequency domain

        3. Extracts the highest amplitude frequency peaks

        4. Prints the results to the console

This forms the foundation for note detection and melody mapping.

![alt text](<Screenshot 2025-12-06 at 12.28.11 AM.png>)