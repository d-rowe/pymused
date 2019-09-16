from __future__ import annotations
import re
import pymused
from .knowledge import letters, accidentals, interval_semitones


class Pitch:
    def __init__(self, *args):
        self._coord = None
        if len(args) > 0:
            parsing_scheme = {1: {str: self.from_string, list: self.from_coord}}
            parse_method = parsing_scheme[len(args)]
            for arg in args:  # Traverse with arg types until the parsing method is reached
                parse_method = parse_method.get(type(arg))
            parse_method(*args)

    def from_coord(self, coord: [int, int]):
        self._coord = coord
        return self

    def from_string(self, pitch: str):
        pattern = "(^[a-gA-G])(b{1,3}|#{1,3}|x)?([0-9])?$"
        m = re.search(pattern, pitch)
        if not m:
            raise ValueError("Pitch arg must be in scientific note notation (e.g. Ab4)")
        letter_val = letters.index(m.group(1).upper())
        accidental_val = accidentals[m.group(2)] if m.group(2) else 0
        octave_val = int(m.group(3) or 4)
        degree = letter_val + (octave_val * 7) - 4
        semitone = interval_semitones[letter_val] + (octave_val * 12) + accidental_val - 8
        self._coord = [degree, semitone]

    def name(self) -> str:
        return letters[(self.coord()[0] + 4) % 7]

    def accidental(self) -> str:
        letter_val = interval_semitones[letters.index(self.name())]
        octave_val = self.octave() * 12
        difference = self.coord()[1] - (letter_val + octave_val - 8)
        return {v: a for a, v in accidentals.items()}[difference] if difference != 0 else ''

    def octave(self) -> int:
        return (self.coord()[0] + 4) // 7

    def string(self) -> str:
        return f"{self.name()}{self.accidental()}{self.octave()}"

    def accidental_value(self) -> int:
        acc = self.accidental()
        return accidentals[acc] if acc != '' else 0

    def chroma(self) -> int:  # Returns the pitch class of the note (0-11)
        letter_val = interval_semitones[letters.index(self.name())]
        return (letter_val + self.accidental_value()) % 12

    def key(self) -> int:
        return self.coord()[1]

    def midi(self) -> int:
        return self.key() + 20

    def freq(self) -> float:  # Returns the frequency given A4=440
        concert_a = 440
        distance_from_a = self.key() - 49
        decimal_points = 2
        return round(concert_a * (1.059463094359 ** distance_from_a), decimal_points)

    def letter_value(self) -> int:
        return letters.index(self.name())

    def white_key(self):
        return self.coord()[0]

    def coord(self):
        return self._coord

    def interval(self, name: str) -> Pitch:
        coord = pymused.Interval(name).coord()
        degree = coord[0] + self.coord()[0]
        semitone = coord[1] + self.coord()[1]
        return Pitch([degree, semitone])

    def __str__(self):
        return self.string()

    def __repr__(self) -> str:
        return f"Pitch[{self.string()}]"

    def __eq__(self, other):
        return self.coord() == other.coord()
