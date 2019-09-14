import re


class Pitch:
    def __init__(self, pitch: str = None):
        self.string, self.name, self.accidental, self.octave = [None] * 4
        self.__empty = True
        if pitch:
            self.from_string(pitch)

    def from_string(self, pitch: str):
        pattern = "(^[a-gA-G])(b{1,3}|#{1,3}|x)?([0-9])?$"
        m = re.search(pattern, pitch)
        if not m:
            raise ValueError("pitch arg must be in scientific note notation (e.g. Ab4)")

        self.string = pitch
        self.name = m.group(1).upper()
        self.accidental = m.group(2) or ''
        self.octave = int(m.group(3) or 4)
        self.__empty = False

    def key(self) -> int:  # Returns note's key number on a piano
        self.__raise_if_empty()
        octave_val = self.octave * 12
        return self.chroma() + octave_val - 8

    def midi(self) -> int:
        self.__raise_if_empty()
        return self.key() + 20

    def chroma(self) -> int:  # Returns the pitch class of the note (0-11)
        self.__raise_if_empty()
        letter_semitones = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
        letter_val = letter_semitones[self.name]
        if self.accidental == '':
            accidental_val = 0
        return (letter_val + self.accidental_val()) % 12

    def accidental_val(self) -> int:
        self.__raise_if_empty()
        semitones = {'bbb': -3, 'bb': -2, 'b': -1, '#': 1, '##': 2, '###': 3, 'x': 2}
        return sum([semitones[acc] for acc in self.accidental])

    def freq(self) -> float:  # Returns the frequency given A4=440
        self.__raise_if_empty()
        concert_a = 440
        distance_from_a = self.key() - 49
        decimal_points = 2
        return round(concert_a * (1.059463094359 ** distance_from_a), decimal_points)

    def deg(self) -> int:
        self.__raise_if_empty()
        letters = 'CDEFGAB'
        return letters.index(self.name)

    def diatonic_key(self):
        return self.deg() + (self.octave * 7) - 4

    def __str__(self):
        return self.string

    def __repr__(self) -> str:
        return f"Pitch('{self.string}')"

    def __raise_if_empty(self):
        if self.__empty:
            raise NameError("returning functions cannot be called on empty Pitch")
