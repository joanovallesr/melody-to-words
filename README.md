# melody-to-words

Melody to Words is a proeject to help develop speech through music. This is a very personal project as I did it thinking about my daugher, who has speech delay.

## How it works

The kid plays an instruemnt -> the app listens and identifies the note pattern -> generates a spoken word or short sentence associated with that melody -> reinforces speech through music and repetition.

## The script

This script loads a .wav audio file, converts the time-series waveform into frequency components using Fast Fourier Transform (FFT), and prints the highest amplitude frequency peaks. I learned how digital audio is represented using sample rates and arrays, how FFT transforms sound into measurable frequency data, and how to extract meaningful features for future machine learning steps.