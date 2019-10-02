from pymused import Pitch, Interval
from .utils import chord_intervals, jazz_chord_aliases, academic_aliases, args_type_strings


class Chord:
    def __init__(self, *args):
        self.intervals, self.root, self.voicing = [None] * 3
        arg_types = args_type_strings(args)
        parsing_scheme = {'str': self.from_string, 'str str': self.from_root_and_type,
                          'Pitch str': self.from_root_and_type, 'list': self.from_pitches}
        if len(args) != 0:
            if arg_types not in parsing_scheme:
                raise ValueError('Unknown argument scheme')
            parse_method = parsing_scheme.get(arg_types)
            parse_method(*args)

    def from_string(self, chord_name):
        try:
            self.root = Pitch(chord_name)
        except ValueError:
            pass  # No root found or set
        for chord_type in chord_intervals:
            if chord_type in chord_name:
                intervals = chord_intervals.get(chord_type)
                self.intervals = [Interval(interval) for interval in intervals]

    def from_root_and_type(self, root, chord_type: str):
        self.root = Pitch(root)

        # Check scale type is known
        if chord_type in chord_intervals:
            recipe = chord_intervals.get(chord_type)
            self.voicing = [Interval(interval) for interval in recipe]
        else:
            raise ValueError('Unknown chord type')

    def from_pitches(self, pitches):
        pitches = [Pitch(p) for p in pitches]  # Make all pitches Pitch objects (pitches maybe provided as strings)
        pitches = sorted(pitches, key=lambda p: p.key())

        chord_simple_intervals = []  # Simple interval version of chord_intervals.values(), all intervals under octave
        for chord in chord_intervals.values():
            chord_simple_intervals.append([Interval(e).simple() for e in chord])

        for pitch in pitches:  # Try each pitch as possible root
            intervals = []
            for other_pitch in pitches:  # Find pitch intervals in relation to current possible root
                interval = Interval(pitch, other_pitch).simple()
                coord = interval.coord
                if coord[0] < 0:  # Check for descending intervals, flip and invert them
                    coord[0] *= -1
                    coord[1] *= -1
                    interval = Interval(coord).invert()
                if interval not in intervals:  # Ignore doubled pitches
                    intervals.append(interval)

            sorted_intervals = sort_intervals(intervals)
            if sorted_intervals in chord_simple_intervals:  # Check if simple intervals have a match
                self.root = pitch
                self.intervals = sorted_intervals

                # Find intervals between root and other pitches for voicing
                self.voicing = [Interval(pitch, other_pitch) for other_pitch in pitches]
                return
        raise ValueError('Not a valid known chord')

    def type(self):
        sorted_intervals = sort_intervals(self.intervals)
        interval_names = [e.string() for e in sorted_intervals]
        chords = list(chord_intervals.values())
        if interval_names in chords:
            index = chords.index(interval_names)
            chord_type = list(chord_intervals.keys())[index]
            return chord_type
        else:
            return None

    def name(self):
        root_name = self.root.simple()
        return root_name + self.type()

    def academic(self):
        root_name = self.root.simple()
        academic_type = academic_aliases.get(self.type())
        # TODO: Add inversion support
        return root_name + academic_type

    def jazz(self):
        root_name = self.root.simple()
        bottom_name = self.pitches()[0].simple()
        jazz_type = jazz_chord_aliases.get(self.type())
        if root_name == bottom_name:
            return root_name + jazz_type
        else:
            return f"{root_name}{jazz_type}/{bottom_name}"

    def pitches(self):
        if self.root and self.voicing:
            return [self.root + interval for interval in self.voicing]
        else:
            raise ValueError('Cannot find pitches without both root and voicing')


def sort_intervals(intervals):
    return sorted(intervals, key=lambda e: e.coord[0])  # Order intervals ascending


def simplify_intervals(interval_arr):
    return [interval.simple() for interval in interval_arr]
