from pymused.pitch import Pitch


class Interval:
    def __init__(self, pitch1: Pitch, pitch2: Pitch):
        self.pitches = [pitch1, pitch2]
        self.s_pitches = sorted([pitch1, pitch2], key=lambda k: k.key)  # Sort pitches from low -> high
        self.semitones = self.s_pitches[1].key - self.s_pitches[0].key
        self.toString = self.__str__
        low_ord, hi_ord = [ord(p.letter) for p in self.s_pitches]  # Find pitches' ordinal num based off of letter
        base = hi_ord - low_ord + 1
        if base < 1:
            base += 7
        self.base = base  # Set interval in bases
        self.degree = self.base + ((self.s_pitches[1].octave - self.s_pitches[0].octave) * 7)

    def __str__(self) -> str:
        base_index = self.base - 1
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
        offset = (self.semitones % 12) - ref_semitones  # Distance from Major scale reference interval
        quality = quality_offsets[ref_quality][offset]
        return quality + str(self.degree)
