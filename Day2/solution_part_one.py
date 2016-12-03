import sys


def main(filename):

    current_position = 5

    code = []

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        line.rstrip()

        for direction in line:
            new_position = get_new_position(current_position, direction)

            if new_position:
                current_position = new_position

        code.append(current_position)

    print code


def get_new_position(current_position, direction):

    if current_position == 1:
        return one(direction)

    if current_position == 2:
        return two(direction)

    if current_position == 3:
        return three(direction)

    if current_position == 4:
        return four(direction)

    if current_position == 5:
        return five(direction)

    if current_position == 6:
        return six(direction)

    if current_position == 7:
        return seven(direction)

    if current_position == 8:
        return eight(direction)

    if current_position == 9:
        return nine(direction)


def one(direction):
    return {
        'U': False,
        'D': 4,
        'L': False,
        'R': 2
    }.get(direction)


def two(direction):
    return {
        'U': False,
        'D': 5,
        'L': 1,
        'R': 3
    }.get(direction)


def three(direction):
    return {
        'U': False,
        'D': 6,
        'L': 2,
        'R': False
    }.get(direction)


def four(direction):
    return {
        'U': 1,
        'D': 7,
        'L': False,
        'R': 5
    }.get(direction)


def five(direction):
    return {
        'U': 2,
        'D': 8,
        'L': 4,
        'R': 6
    }.get(direction)


def six(direction):
    return {
        'U': 3,
        'D': 9,
        'L': 5,
        'R': False
    }.get(direction)


def seven(direction):
    return {
        'U': 4,
        'D': False,
        'L': False,
        'R': 8
    }.get(direction)


def eight(direction):
    return {
        'U': 5,
        'D': False,
        'L': 7,
        'R': 9
    }.get(direction)


def nine(direction):
    return {
        'U': 6,
        'D': False,
        'L': 8,
        'R': False
    }.get(direction)

if __name__ == "__main__":
   main(sys.argv[1])
