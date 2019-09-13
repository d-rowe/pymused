from pymused.pitch import Pitch


class Interval:
    def __init__(self, pitch1: Pitch, pitch2: Pitch):
        self.pitches = [pitch1, pitch2]
        self.s_pitches = sorted(self.pitches, key=lambda k: k.key)  # Sort pitches from low -> high
        self.semitones = self.s_pitches[1].key - self.s_pitches[0].key
        self.degree = self.s_pitches[1].diatonic_key() - self.s_pitches[0].diatonic_key() + 1
        self.base = self.degree % 7  # Set interval in bases

        self.toString = self.__str__

    def quality(self) -> str:
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
        return quality_offsets[ref_quality][offset]

    def __str__(self) -> str:
        return self.quality() + str(self.degree)
