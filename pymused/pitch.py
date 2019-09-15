import re
from .knowledge import letters, accidentals, interval_semitones


class Pitch:
    def __init__(self, name: str = None):
        self.coord = None
        if name:
            self.from_string(name)

    def from_string(self, pitch: str):
        pattern = "(^[a-gA-G])(b{1,3}|#{1,3}|x)?([0-9])?$"
        m = re.search(pattern, pitch)
        if not m:
            raise ValueError("Pitch arg must be in scientific note notation (e.g. Ab4)")
        letter_val = letters.index(m.group(1).upper())
        accidental_val = accidentals[m.group(2)] if m.group(2) else 0
        octave_val = int(m.group(3) or 4)
        self.coord = [letter_val, accidental_val, octave_val]

    def name(self) -> str:
        return letters[self.coord[0]]

    def accidental(self) -> str:
        accidental_val = self.coord[1]
        if accidental_val == 0:
            return ''
        else:
            return {val: acc for acc, val in accidentals.items()}[accidental_val]

    def string(self) -> str:
        return f"{self.name()}{self.accidental()}{self.octave()}"

    def octave(self) -> int:
        return self.coord[2]

    def key(self) -> int:
        octave_val = self.octave() * 12
        return self.chroma() + octave_val - 8

    def midi(self) -> int:
        return self.key() + 20

    def chroma(self) -> int:  # Returns the pitch class of the note (0-11)
        letter_val = interval_semitones[self.coord[0]]
        return (letter_val + self.accidental_value()) % 12

    def accidental_value(self) -> int:
        return self.coord[1]

    def freq(self) -> float:  # Returns the frequency given A4=440
        concert_a = 440
        distance_from_a = self.key() - 49
        decimal_points = 2
        return round(concert_a * (1.059463094359 ** distance_from_a), decimal_points)

    def letter_value(self) -> int:
        return letters.index(self.name())

    def white_key(self):
        return self.letter_value() + (self.octave() * 7) - 4

    def __str__(self):
        return self.string()

    def __repr__(self) -> str:
        return f"Pitch[{self.string()}]"
