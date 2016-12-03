import sys


def main(filename):

    line_counter = 0
    triangle_counter = 0
    matrix = []

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:

        line_counter += 1

        line = line.strip()
        line_list = line.split('  ')
        line_list = filter(None, line_list)

        matrix.append(line_list)

        if line_counter == 3:

            for i in range(3):
                edges = column(matrix, i)

                first = edges[0].strip()
                second = edges[1].strip()
                third = edges[2].strip()
                if check_triangle(int(first), int(second), int(third)):
                    triangle_counter += 1

            line_counter = 0
            matrix = []

    print triangle_counter


def column(matrix, i):
    return [row[i] for row in matrix]


def check_triangle(edge_one, edge_two, edge_three):

    sum1 = edge_one + edge_two
    sum2 = edge_one + edge_three
    sum3 = edge_two + edge_three

    if sum1 > edge_three and sum2 > edge_two and sum3 > edge_one:
        return True

    return False


if __name__ == "__main__":
   main(sys.argv[1])
