from __future__ import annotations
import re
from math import floor
from pymused.pitch import Pitch
from .utils import *


class Interval:
    def __init__(self, *args):
        self.coord = None  # Distance coordinates in [degrees, semitones]
        arg_types = args_type_strings(args)
        parsing_scheme = {'str': self.from_string, 'list': self.from_coord, 'Pitch Pitch': self.from_between,
                          'str str': self.from_between, 'Pitch str': self.from_between,
                          'str Pitch': self.from_between, 'Interval': interval_pass_through}
        if arg_types not in parsing_scheme:
            raise ValueError('Unknown argument scheme')

        parse_method = parsing_scheme.get(arg_types)
        parse_method(*args)

    def from_string(self, name: str) -> Interval:  # Sets internal coord from name (e.g. 'P5')
        # Search for a pitch against the scientific pitch notation format
        pattern = "^(P|M|m|d*|A*)(-)?([1-9][0-9]?[0-9]?)$"
        m = re.search(pattern, name)

        # Check if given name matches scientific pitch notation format
        if not m:
            raise ValueError("Unknown interval notation")

        # Set variables from regex match
        direction = -1 if m.group(2) else 1
        degree_index = int(m.group(3)) - 1
        quality = m.group(1)
        base_index = degree_index % 7
        ref_quality = interval_types[base_index]

        # Check if the given interval is a real interval (e.g. no P3)
        illegal_qualities = {'M': 'P', 'P': ['M', 'm']}
        if quality in illegal_qualities.get(ref_quality):
            raise ValueError(f"Illegal quality interval combination '{m.group(0)}'")

        # Find semitone offset from reference (Perfect of Major) interval (e.g. d4's offset would be -1)
        general_offsets = {'P': 0, 'M': 0, 'm': -1}
        if quality in general_offsets.keys():
            offset = general_offsets.get(quality)
        elif 'A' in quality:
            offset = len(quality)
        else:  # If diminished
            d_offset = {'P': 0, 'M': -1}
            offset = -len(quality) + d_offset.get(ref_quality)

        # Use all base information to create interval coordinate
        degree = degree_index * direction
        semitones_simple = (interval_semitones[base_index] + offset) * direction
        semitones_octave = (floor(degree_index / 7) * 12) * direction
        coord = [degree, semitones_simple + semitones_octave]
        self.coord = coord
        return self

    def from_between(self, pitch1, pitch2) -> Interval:
        pitch1 = Pitch(pitch1) if type(pitch1) is str else pitch1
        pitch2 = Pitch(pitch2) if type(pitch2) is str else pitch2
        val = pitch2.key(True) - pitch1.key(True)
        semi = pitch2.key() - pitch1.key()
        self.coord = [val, semi]
        return self

    def from_coord(self, coord: [int, int]):
        self.coord = coord
        return self

    def value(self) -> int:
        abs_val = abs(self.coord[0]) + 1
        return abs_val if self.coord[0] >= 0 else abs_val * -1

    def base(self) -> int:
        abs_base = abs(self.value()) % 7
        base = abs_base if self.coord[0] >= 0 else abs_base * -1
        return base

    def simple(self) -> Interval:
        return Interval(self.coord_simple(True))

    def invert(self) -> Interval:
        coord = self.coord_simple(True)
        if coord[0] != 0:
            degrees = 7 - coord[0]
            semitones = 12 - coord[1]
        else:
            degrees, semitones = [coord[0], -coord[1]]
        return Interval([degrees, semitones])

    def quality(self) -> str:
        base_index = abs(self.coord_simple(True)[0])
        ref_semitones = interval_semitones[base_index]  # Major semitone distance for reference
        ref_quality = interval_types[base_index]  # Major scale interval quality for given degree
        semitones = self.coord_simple(True)[1]
        if self.coord[0] < 0:
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
        return self.coord[1]

    def string(self) -> str:
        return self.quality() + str(self.value())

    def coord_simple(self, simple: bool = False) -> [int, int]:
        if not simple:
            return self.coord
        else:  # If simple, flatten coordinate to within an octave
            degrees, semitones = self.coord
            octaves = degrees // 7 if degrees >= 0 else -(degrees // -7)
            degree_excess, semitone_excess = octaves * 7, octaves * 12
            degrees_simple, semitones_simple = degrees - degree_excess, semitones - semitone_excess
            return [degrees_simple, semitones_simple]

    def ascending(self) -> bool:
        if self.coord[0] > 0:
            return True
        elif self.coord[0] < 0:
            return False
        else:
            return self.coord[1] >= 0

    def descending(self) -> bool:
        return not self.ascending()

    def flip(self) -> Interval:
        coord = self.coord
        coord[0] *= -1
        coord[1] *= -1
        return Interval(coord)

    def __str__(self):
        return self.string()

    def __repr__(self):
        return f"Interval({self.string()})"

    def __eq__(self, other):
        if isinstance(other, Interval):
            return self.coord == other.coord
        else:
            return False

    def __add__(self, other):
        return Interval(add_coords(self.coord, other.coord_simple()))

    def __sub__(self, other):
        return Interval(sub_coords(self.coord, other.coord_simple()))


# If arg is interval, simply return the interval supplied
def interval_pass_through(pitch):
    return pitch
