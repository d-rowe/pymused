from __future__ import annotations
import re
import pymused
from .utils import *


class Pitch:
    def __init__(self, *args):
        self.coord = None
        arg_types = args_type_strings(args)
        parsing_scheme = {'str': self.from_string, 'list': self.from_coord}
        if arg_types not in parsing_scheme:
            raise ValueError('Unknown argument scheme')
        parse_method = parsing_scheme.get(arg_types)
        parse_method(*args)

    def from_coord(self, coord: [int, int]):
        self.coord = coord
        return self

    def from_string(self, pitch: str):
        spn_pattern = "([a-gA-G])([b|#|x]*)?([0-9])?"  # Regex pattern for scientific pitch notation
        m = re.search(spn_pattern, pitch)
        if not m:
            raise ValueError("Pitch arg must be in scientific note notation (e.g. Ab4)")
        letter_val = letters.index(m.group(1).upper())
        accidental_val = self._accidental_int(m.group(2)) if m.group(2) else 0
        octave_val = int(m.group(3) or 4)
        degree = letter_val + (octave_val * 7) - 4
        semitone = interval_semitones[letter_val] + (octave_val * 12) + accidental_val - 8
        self.coord = [degree, semitone]

    def name(self) -> str:
        return letters[(self.coord[0] + 4) % 7]

    def accidental(self) -> str:
        letter_semitones = interval_semitones[letters.index(self.name())]
        octave_semitones = self.octave() * 12
        offset = self.coord[1] - (letter_semitones + octave_semitones - 8)
        if offset > 0:
            return ('#' * (offset % 2)) + ('x' * (offset // 2))
        elif offset <= 0:
            return 'b' * abs(offset)

    def octave(self) -> int:
        return (self.coord[0] + 4) // 7

    def string(self) -> str:
        return f"{self.name()}{self.accidental()}{self.octave()}"

    def simple(self):
        return f"{self.name()}{self.accidental()}"

    @staticmethod
    def _accidental_int(accidental) -> int:
        accidental_values = {'b': -1, '#': 1, 'x': 2}
        return sum([accidental_values[acc] for acc in accidental])

    def accidental_value(self):
        return self._accidental_int(self.accidental())

    def chroma(self) -> int:
        letter_val = interval_semitones[letters.index(self.name())]
        return (letter_val + self.accidental_value()) % 12

    def key(self, diatonic: bool = False) -> int:
        return self.coord[0] if diatonic else self.coord[1]

    def midi(self) -> int:
        return self.key() + 20

    def frequency(self) -> float:
        concert_a = 440
        distance_from_a = self.key() - 49
        decimal_points = 2
        return round(concert_a * (1.059463094359 ** distance_from_a), decimal_points)

    def letter_value(self) -> int:
        return letters.index(self.name())

    def transpose(self, interval, flip_direction: bool = False) -> Pitch:
        if type(interval) is pymused.Interval:
            coord = interval.coord
        else:
            coord = pymused.Interval(interval).coord
        if not flip_direction:
            return Pitch(add_coords(self.coord, coord))
        else:
            return Pitch(sub_coords(self.coord, coord))

    def scale(self, scale_type: str):
        return pymused.Scale(self, scale_type)

    def __str__(self) -> str:
        return self.string()

    def __repr__(self) -> str:
        return f"Pitch({self.string()})"

    def __eq__(self, other) -> bool:
        return self.coord == other.coord

    def __add__(self, other) -> Pitch:
        return self.transpose(other)

    def __sub__(self, other) -> Pitch:
        return self.transpose(other, True)
