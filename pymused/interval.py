import re
from math import floor
from pymused.pitch import Pitch

interval_semitones = [0, 2, 4, 5, 7, 9, 11]  # Semitones away from root for Major scale
interval_types = ['P', 'M', 'M', 'P', 'P', 'M', 'M']  # Major scale interval qualities
quality_offsets = {  # Interval types and their offset in semitones from reference
    'P': {
        -2: 'dd',
        -1: 'd',
        0: 'P',
        1: 'A',
        2: 'AA'
    },
    'M': {
        -3: 'dd',
        -2: 'd',
        -1: 'm',
        0: 'M',
        1: 'A',
        2: 'AA'
    }
}


def reduce_interval(value: int, mod_val: int) -> int:
    return value % mod_val if value >= 0 else value % -mod_val


class Interval:
    def __init__(self, *args):
        self.coord = None  # Distance coordinates in [degrees, semitones]
        # Dictionary of arg schemas and their parsing methods
        parsing = {1: {str: self.from_string}, 2: {Pitch: {Pitch: self.from_between}}}
        parse_method = parsing[len(args)]
        for arg in args:  # Traverse with arg types until the parsing method is reached
            parse_method = parse_method.get(type(arg))
        parse_method(*args)  # Pass args into appropriate parsing method

    def from_string(self, name: str):
        pattern = "^(P|M|m|d{1,2}|A{1,3})(-)?([1-9][0-9]?[0-9]?)$"
        m = re.search(pattern, name)
        if not m:
            raise ValueError("Unknown interval notation")
        direction = -1 if m.group(2) else 1  # Check for minus symbol
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
        self.coord = coord
        return self

    def from_between(self, pitch1: Pitch, pitch2: Pitch):
        val = pitch2.white_key() - pitch1.white_key()
        semi = pitch2.key() - pitch1.key()
        self.coord = [val, semi]
        return self

    def base(self) -> int:
        abs_base = abs(self.value()) % 7  # Absolute value base
        base = abs_base if self.coord[0] >= 0 else abs_base * -1
        return base

    def value(self):
        abs_val = abs(self.coord[0]) + 1
        return abs_val if self.coord[0] >= 0 else abs_val * -1

    def simple(self):
        self.coord = self.coord_simple()
        return self

    def coord_simple(self):
        degree = reduce_interval(self.coord[0], 7)
        semitone = reduce_interval(self.coord[1], 12)
        return [degree, semitone]

    def quality(self) -> str:
        base_index = abs(self.coord_simple()[0])
        ref_semitones = interval_semitones[base_index]  # Major semitone distance for reference
        ref_quality = interval_types[base_index]  # Major scale interval quality for given degree
        if self.coord[0] < 0:
            semitones = abs(self.coord_simple()[1])
        else:
            semitones = self.coord_simple()[1]
        offset = semitones - ref_semitones  # Distance from Major scale reference interval
        return quality_offsets[ref_quality][offset]

    def semitones(self):
        return self.coord[1]

    def string(self):
        return self.quality() + str(self.value())

    def __str__(self) -> str:
        return self.string()

    def __repr__(self):
        return f"Interval[{self.string()}]"
