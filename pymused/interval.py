from __future__ import annotations
import re
from math import floor
from pymused.pitch import Pitch
from .knowledge import interval_semitones, interval_types, quality_offsets, add_coords, sub_coords


class Interval:
    def __init__(self, *args):
        self._coord = None  # Distance coordinates in [degrees, semitones]
        parsing_scheme = {1: {str: self.from_string, list: self.from_coord}, 2: self.from_between}
        parse_method = parsing_scheme[len(args)]
        if not callable(parse_method):
            for arg in args:  # Traverse with arg types until the parsing method is reached
                parse_method = parse_method.get(type(arg))
        parse_method(*args)

    """
    Argument parsing methods
        from_string: Sets coordinates from pitch in scientific pitch notation (e.g. 'Ab4')
        from_between: Sets coordinates from the interval between two given pitches or pitch strings
        from_coord: Sets coordinates from a given coordinate
    """

    def from_string(self, name: str) -> Interval:  # Sets internal coord from name (e.g. 'P5')
        pattern = "^(P|M|m|d*|A*)(-)?([1-9][0-9]?[0-9]?)$"
        m = re.search(pattern, name)
        if not m:
            raise ValueError("Unknown interval notation")
        direction = -1 if m.group(2) else 1
        degree_index = int(m.group(3)) - 1
        base_index = degree_index % 7
        ref_quality = interval_types[base_index]
        try:
            offset = {q: o for o, q in quality_offsets[ref_quality].items()}[m.group(1)]
        except KeyError:
            raise ValueError("Illegal quality interval combination (e.g. P3)")
        degree = degree_index * direction
        semitones_simple = (interval_semitones[base_index] + offset) * direction
        semitones_octave = (floor(degree_index / 7) * 12) * direction
        coord = [degree, semitones_simple + semitones_octave]
        self._coord = coord
        return self

    def from_between(self, pitch1, pitch2) -> Interval:
        pitch1 = Pitch(pitch1) if type(pitch1) is str else pitch1
        pitch2 = Pitch(pitch2) if type(pitch2) is str else pitch2
        val = pitch2.key(True) - pitch1.key(True)
        semi = pitch2.key() - pitch1.key()
        self._coord = [val, semi]
        return self

    def from_coord(self, coord: [int, int]):
        self._coord = coord
        return self

    def base(self) -> int:
        abs_base = abs(self.value()) % 7
        base = abs_base if self.coord()[0] >= 0 else abs_base * -1
        return base

    def value(self) -> int:
        abs_val = abs(self.coord()[0]) + 1
        return abs_val if self.coord()[0] >= 0 else abs_val * -1

    def simple(self) -> Interval:
        self._coord = self.coord(True)
        return self

    def invert(self) -> Interval:
        coord = self.coord(True)
        if coord[0] != 0:
            degree = 7 - coord[0]
            semitones = 12 - coord[1]
        else:
            degree, semitones = [coord[0], -coord[1]]
        self._coord = [degree, semitones]
        return self

    def coord(self, simple: bool = False) -> [int, int]:
        if not simple:
            return self._coord
        else:
            coord = self._coord
            mods = [7, 12]  # % 7 for degrees, % 12 for semitones
            simple_coord = []
            for i, mod in enumerate(mods):
                simple_coord.append(coord[i] % mod if coord[i] >= 0 else coord[i] % -mod)
            return simple_coord

    def quality(self) -> str:
        base_index = abs(self.coord(True)[0])
        ref_semitones = interval_semitones[base_index]  # Major semitone distance for reference
        ref_quality = interval_types[base_index]  # Major scale interval quality for given degree
        semitones = self.coord(True)[1]
        if self.coord()[0] < 0:
            semitones = abs(semitones)
        offset = semitones - ref_semitones  # Distance from Major scale reference interval
        if offset == 0:
            return ref_quality
        elif ref_quality == 'P':
            if offset < 0:
                return 'd' * abs(offset)
            else:
                return 'A' * abs(offset)
        else:
            if offset < -1:
                return 'd' * (abs(offset) - 1)
            elif offset > 0:
                return 'A' * offset
            else:
                return 'm'

    def semitones(self) -> int:
        return self.coord()[1]

    def string(self) -> str:
        return self.quality() + str(self.value())

    def __str__(self):
        return self.string()

    def __repr__(self):
        return f"Interval[{self.string()}]"

    def __eq__(self, other):
        return self.coord() == other.coord()

    def __add__(self, other):
        return Interval(add_coords(self.coord(), other.coord()))

    def __sub__(self, other):
        return Interval(sub_coords(self.coord(), other.coord()))
