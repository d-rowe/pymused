# Basic pitch and interval positional data
letters = 'CDEFGAB'
interval_semitones = [0, 2, 4, 5, 7, 9, 11]  # Semitones away from root for Major scale
interval_types = ['P', 'M', 'M', 'P', 'P', 'M', 'M']  # Major scale interval qualities

# Basic scale data
scale_recipes = {
    'major': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'M7'],
    'natural minor': ['P1', 'M2', 'm3', 'P4', 'P5', 'm6', 'm7'],
    'harmonic minor': ['P1', 'M2', 'm3', 'P4', 'P5', 'm6', 'M7'],
    'melodic minor': ['P1', 'M2', 'm3', 'P4', 'P5', 'M6', 'M7'],
    'major pentatonic': ['P1', 'M2', 'M3', 'P5', 'M6'],
    'minor pentatonic': ['P1', 'm3', 'P4', 'P5', 'm7'],
    # greek modes:
    'ionian': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'M7'],
    'dorian': ['P1', 'M2', 'm3', 'P4', 'P5', 'M6', 'm7'],
    'phrygian': ['P1', 'm2', 'm3', 'P4', 'P5', 'm6', 'm7'],
    'lydian': ['P1', 'M2', 'M3', 'A4', 'P5', 'M6', 'M7'],
    'mixolydian': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'm7'],
    'aeolian': ['P1', 'M2', 'm3', 'P4', 'P5', 'm6', 'm7'],
    'locrian': ['P1', 'm2', 'm3', 'P4', 'd5', 'm6', 'm7'],
}
