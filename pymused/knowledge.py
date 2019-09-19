interval_semitones = [0, 2, 4, 5, 7, 9, 11]  # Semitones away from root for Major scale
interval_types = ['P', 'M', 'M', 'P', 'P', 'M', 'M']  # Major scale interval qualities
letters = 'CDEFGAB'


def add_coords(coord1: [int, int], coord2: [int, int]) -> [int, int]:
    return [coord1[i] + coord2[i] for i in range(2)]


def sub_coords(coord1: [int, int], coord2: [int, int]) -> [int, int]:
    return [coord1[i] - coord2[i] for i in range(2)]
