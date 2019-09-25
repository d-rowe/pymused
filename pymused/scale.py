from pymused import Pitch, Interval
from .utils import *


class Scale:
    def __init__(self, *args):
        self._intervals = None
        self._root = None

        arg_types = args_type_strings(args)
        parsing_scheme = {'str': self.from_name, 'str str': self.from_root_and_name,
                          'Pitch str': self.from_root_and_name, 'Pitch list': self.from_root_and_intervals,
                          'str list': self.from_root_and_intervals, 'list': self.from_intervals}
        if arg_types not in parsing_scheme:
            raise ValueError('Unknown argument scheme')

        parse_method = parsing_scheme.get(arg_types)
        parse_method(*args)

    def from_name(self, scale_name):
        try:
            self._root = Pitch(scale_name)
        except ValueError:
            pass  # No root found

        for scale in scale_intervals:
            if scale in scale_name:
                intervals = scale_intervals.get(scale)
                self.set_intervals(intervals)
                return

    def from_intervals(self, intervals):
        self.set_intervals(intervals)

    def from_root_and_name(self, root, scale_type: str):
        self.set_root(root)

        # Check scale type is known
        if scale_type in scale_intervals:
            intervals = scale_intervals.get(scale_type)
            self.set_intervals(intervals)
        else:
            raise ValueError('Unknown scale type')

    def from_root_and_intervals(self, root, intervals: list):
        self.set_root(root)
        self.set_intervals(intervals)

    def set_root(self, root):
        if type(root) == Pitch:
            self._root = root
        else:  # Convert root to Pitch object if string
            self._root = Pitch(root)

    def set_intervals(self, intervals: list):
        for interval in intervals:
            if type(interval) != Interval:
                interval = Interval(interval)
        self._intervals = intervals

    def pitches(self):
        if self._root and self._intervals:
            root = self._root
            return [root + interval for interval in self._intervals]
        else:
            return None

    def simple(self):
        render = self.pitches()
        return [pitch.simple() for pitch in render]

    def string(self):
        pitches = self.pitches()
        scale_string = ''
        for i, pitch in enumerate(pitches):
            separator = ', ' if i != 0 else ''
            scale_string = f"{scale_string}{separator}{pitch.string()}"
        return scale_string

    def descend(self):
        intervals = self._intervals[::-1]
        if self._root:
            return Scale(self._root, intervals)
        else:
            return Scale(intervals)

    def transpose(self, interval):
        if type(interval) == str:
            interval = Interval(interval)
        self._root = self._root + interval
        return self

    def __str__(self):
        return self.string()

    def __repr__(self):
        simple_notes_string = string_arr_to_string(self.simple())
        return f"Scale({simple_notes_string})"

    def __getitem__(self, item):
        return self.pitches()[item]
