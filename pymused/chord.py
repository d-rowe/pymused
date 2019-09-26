from pymused import Pitch, Interval
from .utils import chord_intervals, args_type_strings


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
            if type(pitch) != Pitch:
                norm_pitches.append(Pitch(pitch))
            else:
                norm_pitches.append(pitch)
        pitches = norm_pitches

        chords = []
        for chord in chord_intervals.values():
            chords.append([Interval(e).simple().coord for e in chord])
        for pitch in pitches:
            intervals = []
            for other_pitch in pitches:
                interval = Interval(pitch, other_pitch)
                coord = interval.coord
                if coord[0] < 0:
                    coord[0] *= -1
                    coord[1] *= -1
                    interval = Interval(coord).invert()
                intervals.append(interval)
            # TODO: Set voicing
            intervals = sorted(intervals, key=lambda e: e.coord[0])  # Order intervals ascending
            interval_coords = [e.coord for e in intervals]
            if interval_coords in chords:
                self.root = pitch
                self.intervals = intervals
                return
        raise ValueError('Not a valid known chord')

    def name(self):
        pitch_name = self.root.simple()
        interval_names = [e.string() for e in self.intervals]
        chords = list(chord_intervals.values())
        if interval_names in chords:
            index = chords.index(interval_names)
            chord_type = list(chord_intervals.keys())[index]
            return pitch_name + chord_type
        else:
            return pitch_name

    def pitches(self):
        if self.root and self.intervals:
            root = self.root
            return [root + interval for interval in self.intervals]
        else:
            return None

    def intervals(self):
        return self.intervals

    def set_intervals(self, intervals):
        for interval in intervals:
            if type(interval) != Interval:
                interval = Interval(interval)
        self.intervals = intervals

    def set_root(self, root):
        if type(root) == Pitch:
            self.root = root
        else:  # Convert root to Pitch object if string
            self.root = Pitch(root)
