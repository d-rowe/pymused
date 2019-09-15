from pymused.pitch import Pitch


class Interval:
    def __init__(self, *args):
        self.coord = None
        parsing = {  # Dictionary of arg lengths, types, and parsing methods
            2: {
                Pitch: {Pitch: self.from_between}
            }
        }
        parse_method = parsing[len(args)]
        for arg in args:
            parse_method = parse_method.get(type(arg))
        parse_method(*args)

    def from_between(self, pitch1: Pitch, pitch2: Pitch):
        value = pitch2.white_key() - pitch1.white_key()
        semitones = pitch2.key() - pitch1.key()
        self.coord = [value, semitones]
        return self

    def base(self) -> int:
        abs_base = abs(self.value()) % 7
        if self.coord[0] >= 0:
            return abs_base
        else:
            return abs_base * -1

    def value(self):
        abs_val = abs(self.coord[0]) + 1
        if self.coord[0] >= 0:
            return abs_val
        else:
            return abs_val * -1

    def simple(self) -> str:
        return self.quality() + str(self.base())

    def quality(self) -> str:
        base_index = abs(self.coord[0]) % 7
        ref_degree_intervals = [0, 2, 4, 5, 7, 9, 11]  # Semitones away from root for Major scale
        ref_degree_qualities = ['P', 'M', 'M', 'P', 'P', 'M', 'M']  # Major scale interval qualities
        ref_semitones = ref_degree_intervals[base_index]  # Major semitone distance for reference
        ref_quality = ref_degree_qualities[base_index]  # Major scale interval quality for given degree
        quality_offsets = {
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
        offset = (abs(self.coord[1]) % 12) - ref_semitones  # Distance from Major scale reference interval
        return quality_offsets[ref_quality][offset]

    def semitones(self):
        return self.coord[1]

    def string(self):
        return self.quality() + str(self.value())

    def __str__(self) -> str:
        return self.string()

    def __repr__(self):
        return f"Interval[{self.string()}]"
