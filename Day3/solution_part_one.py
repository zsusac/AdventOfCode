import sys


def main(filename):

    counter = 0

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:

        line = line.strip()
        line_list = line.split('  ')
        line_list = filter(None, line_list)

        first = line_list[0].strip()
        second = line_list[1].strip()
        third = line_list[2].strip()
        if check_triangle(int(first), int(second), int(third)):
            counter += 1

    print counter


def check_triangle(edge_one, edge_two, edge_three):

    sum1 = edge_one + edge_two
    sum2 = edge_one + edge_three
    sum3 = edge_two + edge_three

    if sum1 > edge_three and sum2 > edge_two and sum3 > edge_one:
        return True

    return False


if __name__ == "__main__":
   main(sys.argv[1])
