import unittest
from pymused import *


class TestPitchFunctions(unittest.TestCase):
    def test_parsing(self):
        for letter in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
            for accidental in ['bbb', 'bb', 'b', '###', '##', '#', 'x', '']:
                for octave in range(0, 9):
                    note_name = letter + accidental + str(octave)
                    self.assertEqual(Pitch(note_name).letter, letter)
                    self.assertEqual(Pitch(note_name).accidental, accidental)
                    self.assertEqual(Pitch(note_name).octave, octave)
                    self.assertEqual(Pitch(note_name).name, note_name)

    def test_key(self):
        self.assertEqual(Pitch('A0').key(), 1)
        self.assertEqual(Pitch('D#1').key(), 7)
        self.assertEqual(Pitch('Gb2').key(), 22)
        self.assertEqual(Pitch('Fx3').key(), 35)
        self.assertEqual(Pitch('A4').key(), 49)
        self.assertEqual(Pitch('Gbb5').key(), 57)
        self.assertEqual(Pitch('C8').key(), 88)

    def test_freq(self):
        self.assertEqual(Pitch('c0').freq(), 16.35)
        self.assertEqual(Pitch('A4').freq(), 440)
        self.assertEqual(Pitch('Bb5').freq(), 932.33)
        self.assertEqual(Pitch('B8').freq(), 7902.13)


if __name__ == '__main__':
    unittest.main()
    print("Passed all tests")
