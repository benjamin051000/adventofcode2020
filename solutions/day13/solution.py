"""
Day 13 initial solution
Benjamin Wheeler
"""


def part1() -> int:
    with open('day13.input', 'r') as f:
        earliest, routes = f.read().splitlines()

    # Format input
    earliest = int(earliest)
    routes = [int(r) for r in routes.split(',') if r != 'x']

    next_buses = [route - earliest % route for route in routes]

    next_bus = min(next_buses)

    return next_bus * routes[next_buses.index(next_bus)]


def part2() -> int:
    pass


if __name__ == '__main__':
    print(f'Running day 13...')
    answer = part1()
    print('Part 1:', answer)

    answer = part2()
    print('Part 2:', answer)

    print('Done.')
