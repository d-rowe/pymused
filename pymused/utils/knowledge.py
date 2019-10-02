letters = 'CDEFGAB'
interval_semitones = [0, 2, 4, 5, 7, 9, 11]  # Semitones away from root for Major scale
interval_types = ['P', 'M', 'M', 'P', 'P', 'M', 'M']  # Major scale interval qualities

scale_intervals = {
    'major': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'M7', 'P8'],
    'natural minor': ['P1', 'M2', 'm3', 'P4', 'P5', 'm6', 'm7', 'P8'],
    'harmonic minor': ['P1', 'M2', 'm3', 'P4', 'P5', 'm6', 'M7', 'P8'],
    'melodic minor': ['P1', 'M2', 'm3', 'P4', 'P5', 'M6', 'M7', 'P8'],
    'major pentatonic': ['P1', 'M2', 'M3', 'P5', 'M6', 'P8'],
    'minor pentatonic': ['P1', 'm3', 'P4', 'P5', 'm7', 'P8'],
    'ionian': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'M7', 'P8'],
    'dorian': ['P1', 'M2', 'm3', 'P4', 'P5', 'M6', 'm7', 'P8'],
    'phrygian': ['P1', 'm2', 'm3', 'P4', 'P5', 'm6', 'm7', 'P8'],
    'lydian': ['P1', 'M2', 'M3', 'A4', 'P5', 'M6', 'M7', 'P8'],
    'mixolydian': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'm7', 'P8'],
    'aeolian': ['P1', 'M2', 'm3', 'P4', 'P5', 'm6', 'm7', 'P8'],
    'locrian': ['P1', 'm2', 'm3', 'P4', 'd5', 'm6', 'm7', 'P8'],
}

chord_intervals = {
    'major': ['P1', 'M3', 'P5'],
    'minor': ['P1', 'm3', 'P5'],
    'augmented': ['P1', 'M3', 'A5'],
    'diminished': ['P1', 'm3', 'd5'],
    'dominant7': ['P1', 'M3', 'P5', 'm7'],
    'minor7': ['P1', 'm3', 'P5', 'm7'],
    'major7': ['P1', 'M3', 'P5', 'M7'],
    'augmented7': ['P1', 'M3', 'A5', 'm7'],
    'diminished7': ['P1', 'm3', 'd5', 'd7'],
    'major7diminished5': ['P1', 'm3', 'd5', 'm7'],
    'suspended2': ['P1', 'P5', 'P8', 'M2'],
    'suspended4': ['P1', 'P5', 'P8', 'P4'],
    'open5': ['P1', 'P5', 'P8']
}

academic_aliases = {
    'major': 'M',
    'minor': 'm',
    'augmented': '+',
    'diminished': '°',
    'dominant7': 'Mm7',
    'minor7': 'mm7',
    'major7': 'MM7',
    'augmented7': '+7',
    'diminished7': '°7',
    'major7diminished5': 'ø7',
    'suspended2': 'sus2',
    'suspended4': 'sus4',
    'open5': '5'
}

jazz_chord_aliases = {
    'major': 'M',
    'minor': 'm',
    'augmented': '+',
    'diminished': '°',
    'dominant7': '7',
    'minor7': 'm7',
    'major7': 'M7',
    'augmented7': '+7',
    'diminished7': '°7',
    'major7diminished5': 'm7b5',
    'suspended2': 'sus2',
    'suspended4': 'sus4',
    'open5': '5'
}
