import re


class Pitch:
    def __init__(self, pitch_name: str):
        note_pattern = "(^[a-gA-G])(b{1,3}|#{1,3}|x)?([0-9])?$"
        m = re.search(note_pattern, pitch_name)
        if not m:
            raise ValueError("pitch_name must be in scientific note notation (e.g. Ab4)")

        self.name = pitch_name
        self.octave = int(m.group(3) or 4)
        self.letter = m.group(1).upper()
        self.accidental = m.group(2) or ''
        self.key = self.__key__()
        self.midi = self.key + 20

    def __key__(self) -> int:  # Returns note's key number on a piano
        letter_semitones = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
        letter_val = letter_semitones[self.letter]
        if self.accidental == '':
            accidental_val = 0
        else:
            accidental_semitones = {'b': -1, '#': 1, 'x': 2}
            accidental_val = sum([accidental_semitones[acc] for acc in self.accidental])
        octave_val = self.octave * 12
        return letter_val + accidental_val + octave_val - 8

    def freq(self) -> float:  # Returns the frequency given A4=440
        concert_a = 440
        distance_from_a = self.key - 49
        decimal_points = 2
        return round(concert_a * (1.059463094359 ** distance_from_a), decimal_points)

    def ord(self) -> int:
        letters = 'CDEFGAB'
        return letters.index(self.letter)

    def diatonic_key(self):
        return self.ord() + (self.octave * 7) - 4

    def __str__(self) -> str:
        return self.name
