# Global helpers


def add_coords(coord1: [int, int], coord2: [int, int]) -> [int, int]:
    return [coord1[i] + coord2[i] for i in range(2)]


def sub_coords(coord1: [int, int], coord2: [int, int]) -> [int, int]:
    return [coord1[i] - coord2[i] for i in range(2)]
