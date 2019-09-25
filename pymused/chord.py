from pymused import Pitch, Interval
from .utils import chord_intervals


class Chord:
    def __init__(self, *args):
        self._intervals = None
        self._root = None
        self.from_root_and_type(*args)

    def from_root_and_type(self, root, chord_type: str):
        self.set_root(root)

        # Check scale type is known
        if chord_type in chord_intervals:
            recipe = chord_intervals.get(chord_type)
            self._intervals = [Interval(interval) for interval in recipe]
        else:
            raise ValueError('Unknown chord type')

    def set_root(self, root):
        if type(root) == Pitch:
            self._root = root
        else:  # Convert root to Pitch object if string
            self._root = Pitch(root)

    def pitches(self):
        if self._root and self._intervals:
            root = self._root
            return [root + interval for interval in self._intervals]
        else:
            return None
