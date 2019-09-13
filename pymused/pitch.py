import re


class Pitch:
    def __init__(self, note_name: str):
        note_pattern = "(^[a-gA-G])(b{1,3}|#{1,3}|x)?([0-9])?$"
        m = re.search(note_pattern, note_name)
        if not m:
            raise ValueError("note_name must be in scientific note notation (e.g. Ab4)")

        self.name = note_name
        self.octave = int(m.group(3) or 4)
        self.letter = m.group(1).upper()
        self.accidental = m.group(2) or ''
        self.__key = None  # cache for key
        self.__freq = None  # cache for freq

    def key(self) -> int:  # Returns note's key number on a piano
        if self.__key:
            return self.__key
        else:
            letter_semitones = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
            letter_val = letter_semitones[self.letter]
            if self.accidental == '':
                accidental_val = 0
            else:
                accidental_semitones = {'b': -1, '#': 1, 'x': 2}
                accidental_val = sum([accidental_semitones[acc] for acc in self.accidental])
            octave_val = self.octave * 12
            return letter_val + accidental_val + octave_val - 8

    def midi(self) -> int:
        return self.key() + 20

    def freq(self) -> float:  # Returns the frequency given A4=440
        if self.__freq:
            return self.__freq
        else:
            concert_a = 440
            distance_from_a = self.key() - 49
            decimal_points = 2
            return round(concert_a * (1.059463094359 ** distance_from_a), decimal_points)

    def __str__(self) -> str:
        return self.name
