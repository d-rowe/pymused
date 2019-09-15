import unittest
from pymused import *


class TestPitch(unittest.TestCase):
    def test_parsing(self):
        for name in 'CDEFGAB':
            for accidental in ['bbb', 'bb', 'b', '###', '##', '#', 'x', '']:
                for octave in range(0, 9):
                    note_name = name + accidental + str(octave)
                    self.assertEqual(Pitch(note_name).name, name)
                    self.assertEqual(Pitch(note_name).accidental, accidental)
                    self.assertEqual(Pitch(note_name).octave, octave)
                    self.assertEqual(Pitch(note_name).string, note_name)
                    self.assertEqual(str(Pitch(note_name)), note_name)

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

    def test_deg(self):
        self.assertEqual(Pitch('C4').letter_value(), 0)
        self.assertEqual(Pitch('D4').letter_value(), 1)
        self.assertEqual(Pitch('E4').letter_value(), 2)
        self.assertEqual(Pitch('F4').letter_value(), 3)
        self.assertEqual(Pitch('G4').letter_value(), 4)
        self.assertEqual(Pitch('A4').letter_value(), 5)
        self.assertEqual(Pitch('B4').letter_value(), 6)

    def test_chroma(self):
        self.assertEqual(Pitch('C4').chroma(), 0)
        self.assertEqual(Pitch('Cb4').chroma(), 11)
        self.assertEqual(Pitch('Bb1').chroma(), 10)
        self.assertEqual(Pitch('Dx4').chroma(), 4)
        self.assertEqual(Pitch('Cbb4').chroma(), 10)

    def test_diatonic_key(self):
        self.assertEqual(Pitch('A0').white_key(), 1)
        self.assertEqual(Pitch('Bb4').white_key(), 30)
        self.assertEqual(Pitch('C8').white_key(), 52)


class TestInterval(unittest.TestCase):
    def test_coord(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('F4')).coord, [3, 5])
        self.assertEqual(Interval(Pitch('F4'), Pitch('C4')).coord, [-3, -5])
        self.assertEqual(Interval(Pitch('Bb3'), Pitch('C5')).coord, [8, 14])
        self.assertEqual(Interval(Pitch('A4'), Pitch('G4')).coord, [-1, -2])

    def test_base(self):
        self.assertEqual(Interval(Pitch('F4'), Pitch('C4')).base(), -4)
        self.assertEqual(Interval(Pitch('C4'), Pitch('F5')).base(), 4)

    def test_quality(self):
        self.assertEqual(Interval(Pitch('F4'), Pitch('C#7')).quality(), 'A')
        self.assertEqual(Interval(Pitch('Bb3'), Pitch('C#4')).quality(), 'A')
        self.assertEqual(Interval(Pitch('A4'), Pitch('G2')).quality(), 'M')

    def test_simple(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('F5')).simple(), 'P4')
        self.assertEqual(Interval(Pitch('F5'), Pitch('C4')).simple(), 'P-4')
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('E2')).simple(), 'd-5')
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('E7')).simple(), 'A4')

    def test_value(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('F5')).value(), 11)
        self.assertEqual(Interval(Pitch('F5'), Pitch('C4')).value(), -11)
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('E3')).value(), -12)
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('E7')).value(), 18)

    def test_semitones(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('F#4')).semitones(), 6)
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('Eb4')).semitones(), -7)

    def test_string(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('F5')).string(), 'P11')
        self.assertEqual(Interval(Pitch('F5'), Pitch('C4')).string(), 'P-11')
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('E3')).string(), 'd-12')
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('E7')).string(), 'A18')


if __name__ == '__main__':
    unittest.main()
