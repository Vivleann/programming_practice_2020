import random

import numpy as np


def generate_indexes(width, height):
    return tuple(
        (w, h) for w in range(width)
        for h in range(height)
    )


def pretty_print(arr, header=None):
    h, w = arr.shape
    w = w * 2 + 1
    if header:
        if len(header) > w:
            print(header)
            print('+' + '-' * w + '+')
        else:
            print('+' + header.center(w, '-') + '+')
    else:
        print('+' + '-' * w + '+')
    for line in arr:
        print('|', *line, '|')
    print('+' + '-' * w + '+')


def count_neigbors(arr, x, y):
    h, w = arr.shape
    l, r = max(0, x - 1), min(w - 1, x + 1) + 1
    t, b = max(0, y - 1), min(h - 1, y + 1) + 1
    return arr[t:b, l:r].sum() - arr[y, x]


def main(width, height, n, iters):
    field = np.zeros((height, width), dtype=np.uint8)
    indexes = generate_indexes(width, height)

    for x, y in random.choices(indexes, k=n):
        field[y, x] = 1

    for i in range(iters):
        pretty_print(field, f'Iteration #{i}')
        field_copy = field.copy()
        for x, y in indexes:
            neigbors = count_neigbors(field_copy, x, y)
            if field[y, x] and neigbors not in (2, 3):
                field[y, x] = 0
            elif not field[y, x] and neigbors == 3:
                field[y, x] = 1
    pretty_print(field, f'Iteration #{i + 1}')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='The life game simulation')
    parser.add_argument(
        '-w', '--width', default=10,
        type=int, help='width of simulation'
    )
    parser.add_argument(
        '-H', '--height', default=10,
        type=int, help='height of simulation'
    )
    parser.add_argument(
        '-n', '--number-lives', default=30,
        type=int, help='number of start live cells',
        dest='n'
    )
    parser.add_argument(
        '-i', '--iterations', default=10,
        type=int, help='number of iterations',
        dest='iters'
    )
    args = parser.parse_args()
    main(**vars(args))
