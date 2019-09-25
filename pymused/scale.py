from pymused import Pitch, Interval
from .utils import scale_recipes


class Scale:
    def __init__(self, *args):
        self._intervals = None
        self._root = None
        self.from_root_and_name(*args)

    def from_root_and_name(self, root, scale_type: str):
        self.set_root(root)

        # Check scale type is known
        if scale_type in scale_recipes:
            recipe = scale_recipes.get(scale_type)
            self._intervals = [Interval(interval) for interval in recipe]
        else:
            raise ValueError('Unknown scale type')

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

    def __str__(self):
        return self.string()

    def __repr__(self):
        return f"Scale[{self.string()}]"
