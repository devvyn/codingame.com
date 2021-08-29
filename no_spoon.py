from itertools import chain, takewhile, dropwhile
from typing import Tuple

NODE_SYMBOL: str = '0'
NULL_SYMBOL: str = '.'
EMPTY_CELL: int = -1
EMPTY_CELL_COORDINATES: Tuple[int, int] = (-1, -1)


def init():
    width: int = int(input())
    height: int = int(input())
    return (width, height, (
        input() for _ in range(height)
    ))


def boolean_cells(grid_lines):
    return enumerate(
        chain.from_iterable(
            parse_line(line)
            for line
            in grid_lines
        )
    )


def parse_line(line: str):
    grid_value = {
        NODE_SYMBOL: True,
        NULL_SYMBOL: False,
    }
    return (grid_value[symbol] for symbol in line)


def partition_first(seq):
    return seq[0], seq[1:]


def neighbour_e(cells, height: int):
    cell, tail = partition_first(cells)
    return next(
        takewhile(
            lambda item: coordinate_y(item, height) == coordinate_y(cell, height),
            tail,
        ),
        EMPTY_CELL
    )


def neighbour_s(cells, width: int, height: int):
    cell, tail = partition_first(cells)
    return next(
        takewhile(
            lambda item: coordinate_x(item, width) == coordinate_x(cell, width),
            dropwhile(
                lambda item: coordinate_y(item, height) == coordinate_y(cell, height),
                tail,
            )
        ),
        EMPTY_CELL
    )


def coordinate_x(index: int, width: int):
    return index % width


def coordinate_y(index: int, height: int):
    return index // height


def coordinates(index: int, width: int, height: int):
    if (index > EMPTY_CELL):
        return (
            coordinate_x(index, width),
            coordinate_y(index, height),
        )
    return EMPTY_CELL_COORDINATES


def output_args(tail, width, height):
    return chain.from_iterable(
        coordinates(cell, width, height)
        for cell
        in (
            tail[0],
            neighbour_e(tail, height),
            neighbour_s(tail, width, height),
        )
    )


if __name__ == '__main__':
    width, height, grid_lines = init()
    occupied_cell_numbers = [
        index
        for index, occupied
        in boolean_cells(grid_lines)
        if occupied
    ]
    for i in range(len(occupied_cell_numbers)):
        tail = occupied_cell_numbers[i:]
        line = ' '.join(
            str(arg)
            for arg
            in output_args(tail, width, height)
        )
        print(line)
