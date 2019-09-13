import unittest
from pymused import *


class TestPitch(unittest.TestCase):
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
        self.assertEqual(Pitch('A0').key, 1)
        self.assertEqual(Pitch('D#1').key, 7)
        self.assertEqual(Pitch('Gb2').key, 22)
        self.assertEqual(Pitch('Fx3').key, 35)
        self.assertEqual(Pitch('A4').key, 49)
        self.assertEqual(Pitch('Gbb5').key, 57)
        self.assertEqual(Pitch('C8').key, 88)

    def test_freq(self):
        self.assertEqual(Pitch('c0').freq(), 16.35)
        self.assertEqual(Pitch('A4').freq(), 440)
        self.assertEqual(Pitch('Bb5').freq(), 932.33)
        self.assertEqual(Pitch('B8').freq(), 7902.13)


class TestInterval(unittest.TestCase):
    def test_semitones(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('D4')).semitones, 2)
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('C5')).semitones, 2)
        self.assertEqual(Interval(Pitch('Bb5'), Pitch('C5')).semitones, 10)
        self.assertEqual(Interval(Pitch('Ax4'), Pitch('C6')).semitones, 13)
        self.assertEqual(Interval(Pitch('Gbb0'), Pitch('Ax8')).semitones, 102)

    def test_base(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('E4')).base, 3)
        self.assertEqual(Interval(Pitch('Bb3'), Pitch('D4')).base, 3)
        self.assertEqual(Interval(Pitch('Abb2'), Pitch('Cx8')).base, 3)

    def test_degree(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('E5')).degree, 10)
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('D5')).degree, 10)
        self.assertEqual(Interval(Pitch('A3'), Pitch('D4')).degree, 4)


if __name__ == '__main__':
    unittest.main()
