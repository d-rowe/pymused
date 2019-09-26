from pymused import Pitch, Interval
from .utils import chord_intervals, args_type_strings


class Chord:
    def __init__(self, *args):
        self._intervals = None
        self._root = None
        arg_types = args_type_strings(args)
        parsing_scheme = {'str': self.from_string, 'str str': self.from_root_and_type,
                          'Pitch str': self.from_root_and_type}
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
            self._intervals = [Interval(interval) for interval in recipe]
        else:
            raise ValueError('Unknown chord type')

    def pitches(self):
        if self._root and self._intervals:
            root = self._root
            return [root + interval for interval in self._intervals]
        else:
            return None

    def intervals(self):
        return self._intervals

    def set_intervals(self, intervals):
        for interval in intervals:
            if type(interval) != Interval:
                interval = Interval(interval)
        self._intervals = intervals

    def set_root(self, root):
        if type(root) == Pitch:
            self._root = root
        else:  # Convert root to Pitch object if string
            self._root = Pitch(root)
