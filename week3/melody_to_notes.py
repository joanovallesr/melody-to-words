import math

def frequency_to_note_name(frequency):
    """Convert a frequency in Hz to the nearest musical note name."""
    if frequency <= 0:
        return None

    # Reference frequency for A4
    A4_FREQ = 440.0
    # Note names in an octave
    NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Calculate the number of semitones from A4
    semitones_from_A4 = 12 * math.log2(frequency / A4_FREQ)
    # Round to the nearest whole number of semitones
    nearest_semitone = round(semitones_from_A4)

    # Calculate the octave and note index
    note_index = (nearest_semitone + 9) % 12  # +9 to shift A to index 9
    octave = 4 + ((nearest_semitone + 9) // 12)

    note_name = NOTE_NAMES[note_index] + str(octave)
    return note_name