# Copilot Instructions for melody-to-words

## Project Purpose
An assistive, music-driven speech reinforcement system designed to help early childhood language development through melody-based interactions. The system converts audio input into frequency domain data (via FFT) to extract note patterns, which an ML model maps to words with text-to-speech output.

## Current Architecture Stage: Frequency Peak Extraction

The project is currently in the foundation phase focused on audio signal processing:

- **`audio_fft.py`**: Loads `.wav` files, applies FFT to convert audio waveform to frequency domain, extracts top 5 frequency peaks by amplitude. This is the **core pattern** for all future audio processing.
- **`mic_stream_fft.py`**: In-progress real-time microphone streaming (currently minimal). This will replace file-based input.
- **Data flow**: WAV → FFT → Magnitude spectrum → Peak frequency extraction → (future: ML model mapping → TTS output)

## Key Patterns & Conventions

### FFT Processing Pipeline
All frequency analysis follows the pattern in `audio_fft.py`:
1. Load/capture audio (mono conversion if stereo)
2. Apply `np.fft.fft()` to convert to frequency domain
3. Extract magnitude via `np.abs()` on complex results
4. Keep only positive frequencies (`fftfreq[:len//2]`)
5. Sort by magnitude to identify dominant frequencies

When extending to mel-scale, pitch detection, or harmonic analysis, **preserve this foundation** and build filters/transforms on top of the magnitude spectrum.

### Dependencies
- **numpy**: All FFT and array operations
- **scipy.io.wavfile**: WAV file I/O
- **sounddevice**: Real-time microphone streaming (placeholder in `mic_stream_fft.py`)

### Audio Format Constraints
- **Sample rate**: Currently tested at standard rates (44.1kHz, 48kHz). When adding new features, validate that `fftfreq` and frequency calculations scale correctly.
- **Bit depth**: Standard 16-bit or 24-bit PCM. Loudness/amplitude normalization not yet implemented.
- **Channels**: Mono preferred; stereo files auto-converted to mono via `np.mean()` in `audio_fft.py`.
- **File format**: Currently `.wav` only via `scipy.io.wavfile`. Future microphone input via `sounddevice` (in-progress in `mic_stream_fft.py`).

### Test Data
- `piano.wav`: Reference WAV file for testing FFT logic; useful for establishing baseline frequency profiles before adding ML components.

## Development Priorities

1. **Complete `mic_stream_fft.py`**: Real-time audio capture and FFT processing (extends `audio_fft.py` pattern to streams)
2. **Note/Pitch Detection**: Map frequency peaks to musical notes. Document note-to-frequency mappings and algorithm choice.
3. **Melody Pattern Extraction**: Temporal sequence of notes → feature vector for ML input
4. **ML Model Training**: Map melody patterns → target words (library choice open; prioritize model-agnostic feature vectors)
5. **TTS Integration**: Speak output words

## AI Agent Guidelines

- **When adding audio features**: Always validate against `piano.wav` with known expected frequencies
- **When modifying FFT logic**: Preserve the magnitude spectrum extraction pattern; document any changes to peak identification (e.g., threshold filtering, harmonic grouping)
- **When choosing audio processing approaches**: Document trade-offs (e.g., manual FFT + peak detection vs. higher-level libraries) and explain choice relative to project goals
- **Naming convention**: Use descriptive names reflecting audio processing intent (e.g., `extract_frequency_peaks()`, `get_magnitude_spectrum()`) not generic utility names

## Context for ML Phase (Upcoming)

The end goal is a mapping function `melody_pattern → target_word`. Design the feature extraction pipeline now to be model-agnostic: output standardized feature vectors (e.g., numpy arrays of note sequences, frequencies, durations) that can feed into different ML architectures. Pitch detection and ML library choices are intentionally open — prioritize modularity and clear interface boundaries.