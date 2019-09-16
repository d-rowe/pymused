interval_semitones = [0, 2, 4, 5, 7, 9, 11]  # Semitones away from root for Major scale
interval_types = ['P', 'M', 'M', 'P', 'P', 'M', 'M']  # Major scale interval qualities
quality_offsets = {  # Interval types and their offset in semitones from reference
    'P': {
        -2: 'dd',
        -1: 'd',
        0: 'P',
        1: 'A',
        2: 'AA'
    },
    'M': {
        -3: 'dd',
        -2: 'd',
        -1: 'm',
        0: 'M',
        1: 'A',
        2: 'AA'
    }
}
letters = 'CDEFGAB'
accidentals = {'bbb': -3, 'bb': -2, 'b': -1, '#': 1, '##': 2, '###': 3, 'x': 2}


def add_coords(coord1: [int, int], coord2: [int, int]) -> [int, int]:
    return [coord1[i] + coord2[i] for i in range(2)]


def sub_coords(coord1: [int, int], coord2: [int, int]) -> [int, int]:
    return [coord1[i] - coord2[i] for i in range(2)]
