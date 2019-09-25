# Global helpers


def add_coords(coord1: [int, int], coord2: [int, int]) -> [int, int]:
    return [coord1[i] + coord2[i] for i in range(2)]


def sub_coords(coord1: [int, int], coord2: [int, int]) -> [int, int]:
    return [coord1[i] - coord2[i] for i in range(2)]


def string_arr_to_string(s_arr: list) -> str:
    simple_string = ''
    for i, letter in enumerate(s_arr):
        separator = ', ' if i != 0 else ''
        simple_string = f"{simple_string}{separator}{letter}"
    return simple_string
