from pymused import Pitch, Interval
from .utils import chord_intervals, jazz_chord_aliases, academic_aliases, args_type_strings


class Chord:
    def __init__(self, *args):
        self.intervals = None
        self.root = None
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
            self.set_root(Pitch(chord_name))
        except ValueError:
            pass  # No root found or set
        for chord_type in chord_intervals:
            if chord_type in chord_name:
                self.set_intervals(chord_intervals.get(chord_type))

    def from_root_and_type(self, root, chord_type: str):
        self.set_root(root)

        # Check scale type is known
        if chord_type in chord_intervals:
            recipe = chord_intervals.get(chord_type)
            self.intervals = [Interval(interval) for interval in recipe]
        else:
            raise ValueError('Unknown chord type')

    def from_pitches(self, pitches):
        # Make all pitches Pitch objects (pitches maybe provided as strings)
        norm_pitches = []
        for pitch in pitches:
            if isinstance(pitch, Pitch):
                norm_pitches.append(pitch)
            else:
                norm_pitches.append(Pitch(pitch))
        pitches = norm_pitches

        chord_simple_intervals = []  # Simple interval version of chord_intervals.values(), all intervals under octave
        for chord in chord_intervals.values():
            chord_simple_intervals.append([Interval(e).simple() for e in chord])
        for pitch in pitches:
            intervals = []
            for other_pitch in pitches:
                interval = Interval(pitch, other_pitch)
                coord = interval.coord
                if coord[0] < 0:
                    coord[0] *= -1
                    coord[1] *= -1
                    interval = Interval(coord).invert()
                if interval not in intervals:  # Ignore doubled notes
                    intervals.append(interval)
            # TODO: Set voicing
            sorted_intervals = self.sort_intervals(intervals)
            if sorted_intervals in chord_simple_intervals:  # Check if simple intervals have a match
                self.root = pitch
                self.intervals = intervals
                return
        raise ValueError('Not a valid known chord')

    def type(self):
        sorted_intervals = self.sort_intervals(self.intervals)
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
        if self.root and self.intervals:
            root = self.root
            return [root + interval for interval in self.intervals]
        else:
            return None

    @staticmethod
    def sort_intervals(intervals):
        return sorted(intervals, key=lambda e: e.coord[0])  # Order intervals ascending

    def intervals(self):
        return self.intervals

    def set_intervals(self, intervals):
        for interval in intervals:
            if not isinstance(interval, Interval):
                interval = Interval(interval)
        self.intervals = intervals

    def set_root(self, root):
        if isinstance(root, Pitch):
            self.root = root
        else:  # Convert root to Pitch object if string
            self.root = Pitch(root)
