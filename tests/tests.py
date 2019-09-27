import unittest
from pymused import *


class TestPitch(unittest.TestCase):
    def test_parsing(self):
        for name in 'CDEFGAB':
            for accidental in ['bbb', 'bb', 'b', '#x', '#', 'x', '']:
                for octave in range(0, 9):
                    note_name = name + accidental + str(octave)
                    self.assertEqual(Pitch(note_name).name(), name)
                    self.assertEqual(Pitch(note_name).accidental(), accidental)
                    self.assertEqual(Pitch(note_name).octave(), octave)
                    self.assertEqual(Pitch(note_name).string(), note_name)
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
        self.assertEqual(Pitch('c0').frequency(), 16.35)
        self.assertEqual(Pitch('A4').frequency(), 440)
        self.assertEqual(Pitch('Bb5').frequency(), 932.33)
        self.assertEqual(Pitch('B8').frequency(), 7902.13)

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
        self.assertEqual(Pitch('A0').key(True), 1)
        self.assertEqual(Pitch('Bb4').key(True), 30)
        self.assertEqual(Pitch('C8').key(True), 52)

    def test_transpose(self):
        self.assertEqual(Pitch('C4').transpose('M10'), Pitch('E5'))
        self.assertEqual(Pitch('A3').transpose('P-12'), Pitch('D2'))
        self.assertEqual(Pitch('E5').transpose('A2'), Pitch('Fx5'))
        self.assertEqual(Pitch('Db3').transpose(Interval('A6')), Pitch('B3'))
        self.assertEqual(Pitch('A5').transpose(Interval('d-11')), Pitch('E#4'))

    def test_add(self):
        self.assertEqual(Pitch('C4') + 'M10', Pitch('E5'))
        self.assertEqual(Pitch('A3') + 'P-12', Pitch('D2'))
        self.assertEqual(Pitch('E5') + 'A2', Pitch('Fx5'))
        self.assertEqual(Pitch('Db3') + 'A6', Pitch('B3'))
        self.assertEqual(Pitch('A5') + 'd-11', Pitch('E#4'))

    def test_sub(self):
        self.assertEqual(Pitch('C4') - 'M10', Pitch('Ab2'))
        self.assertEqual(Pitch('A3') - 'P-12', Pitch('E5'))
        self.assertEqual(Pitch('E5') - 'A2', Pitch('Db5'))
        self.assertEqual(Pitch('Db3') - 'A6', Pitch('Fbb2'))
        self.assertEqual(Pitch('A5') - 'd-11', Pitch('Db7'))


class TestInterval(unittest.TestCase):
    def test_from_string(self):
        self.assertEqual(Interval('dd2').string(), 'dd2')
        self.assertEqual(Interval('d2').string(), 'd2')
        self.assertEqual(Interval('AA2').string(), 'AA2')
        self.assertEqual(Interval('m-3').coord, [-2, -3])
        self.assertEqual(Interval('P-11').coord, [-10, -17])
        self.assertEqual(Interval('P11').coord, [10, 17])

    def test_coord(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('F4')).coord, [3, 5])
        self.assertEqual(Interval(Pitch('F4'), Pitch('C4')).coord, [-3, -5])
        self.assertEqual(Interval(Pitch('Bb3'), Pitch('C5')).coord, [8, 14])
        self.assertEqual(Interval(Pitch('A4'), Pitch('G4')).coord, [-1, -2])

    def test_coord_simple(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('F5')).coord_simple(True), [3, 5])
        self.assertEqual(Interval(Pitch('F4'), Pitch('C3')).coord_simple(True), [-3, -5])
        self.assertEqual(Interval(Pitch('Bb3'), Pitch('C5')).coord_simple(True), [1, 2])
        self.assertEqual(Interval(Pitch('A4'), Pitch('G3')).coord_simple(True), [-1, -2])

    def test_base(self):
        self.assertEqual(Interval(Pitch('F4'), Pitch('C4')).base(), -4)
        self.assertEqual(Interval(Pitch('C4'), Pitch('F5')).base(), 4)

    def test_quality(self):
        self.assertEqual(Interval(Pitch('F4'), Pitch('C#7')).quality(), 'A')
        self.assertEqual(Interval(Pitch('Bb3'), Pitch('C#4')).quality(), 'A')
        self.assertEqual(Interval(Pitch('A4'), Pitch('G2')).quality(), 'M')
        self.assertEqual(Interval(Pitch('B3'), Pitch('Bbb3')).quality(), 'dd')
        self.assertEqual(Interval('dd1').quality(), 'dd')
        self.assertEqual(Interval('ddddddddddddd5').quality(), 'ddddddddddddd')
        self.assertEqual(Interval('AAAAAA4').quality(), 'AAAAAA')
        self.assertEqual(Interval('Cx4', 'Gbbbbbbbbbbbbbb').quality(), 'dddddddddddddddd')

    def test_simple(self):
        self.assertEqual(Interval(Pitch('C4'), Pitch('F5')).simple().string(), 'P4')
        self.assertEqual(Interval(Pitch('Bb4'), Pitch('Ab2')).simple().string(), 'M-2')

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

    def test_invert(self):
        self.assertEqual(Interval('M2').invert().coord, Interval('m7').coord)
        self.assertEqual(Interval('d1').invert().coord, Interval('A1').coord)
        self.assertEqual(Interval('dd11').invert().coord, Interval('AA5').coord)
        self.assertEqual(Interval('AA3').invert().coord, Interval('dd6').coord)

    def test_between_strings(self):
        self.assertEqual(Interval('C4', 'F4').coord, Interval('P4').coord)
        self.assertEqual(Interval('E3', 'B#4').coord, Interval('A12').coord)
        self.assertEqual(Interval('F6', 'D5').coord, Interval('m-10').coord)


class TestScale(unittest.TestCase):
    def test_string(self):
        self.assertEqual(Scale('C4', 'dorian').string(), 'C4, D4, Eb4, F4, G4, A4, Bb4, C5')
        self.assertEqual(Scale('Db3', 'lydian').string(), 'Db3, Eb3, F3, G3, Ab3, Bb3, C4, Db4')

    def test_descend(self):
        self.assertEqual(Scale('C4', 'dorian').descend().string(), 'C5, Bb4, A4, G4, F4, Eb4, D4, C4')
        self.assertEqual(Scale('Db3', 'lydian').descend().string(), 'Db4, C4, Bb3, Ab3, G3, F3, Eb3, Db3')


if __name__ == '__main__':
    unittest.main()
