import re


class Pitch:
    def __init__(self, pitch_name: str):
        note_pattern = "(^[a-gA-G])(b{1,3}|#{1,3}|x)?([0-9])?$"
        m = re.search(note_pattern, pitch_name)
        if not m:
            raise ValueError("pitch_name must be in scientific note notation (e.g. Ab4)")

        self.string = pitch_name
        self.octave = int(m.group(3) or 4)
        self.name = m.group(1).upper()
        self.accidental = m.group(2) or ''
        self.key = self.__key__()
        self.midi = self.key + 20

    def __key__(self) -> int:  # Returns note's key number on a piano
        octave_val = self.octave * 12
        return self.chroma() + octave_val - 8

    def chroma(self) -> int:  # Returns the pitch class of the note (0-11)
        letter_semitones = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
        letter_val = letter_semitones[self.name]
        if self.accidental == '':
            accidental_val = 0
        else:
            accidental_semitones = {'bbb': -3, 'bb': -2, 'b': -1, '#': 1, '##': 2, '###': 3, 'x': 2}
            accidental_val = sum([accidental_semitones[acc] for acc in self.accidental])
        return (letter_val + accidental_val) % 12

    def freq(self) -> float:  # Returns the frequency given A4=440
        concert_a = 440
        distance_from_a = self.key - 49
        decimal_points = 2
        return round(concert_a * (1.059463094359 ** distance_from_a), decimal_points)

    def deg(self) -> int:
        letters = 'CDEFGAB'
        return letters.index(self.name)

    def diatonic_key(self):
        return self.deg() + (self.octave * 7) - 4

    def __str__(self) -> str:
        return self.string
