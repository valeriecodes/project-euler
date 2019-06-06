def min_sum(matrix):
    dimensions = len(matrix)
    result = [[float("inf")] * dimensions for i in range(dimensions)]
    # This is janky af. Rewrite w/ Dijkstra's
    for i in [1, 2, 3, 4]:
        for column in range(dimensions):
            for row in range(dimensions):
                if column == 0 and row == 0:
                    result[row][column] = matrix[row][column]
                else:
                    possible_moves = []
                    if row < dimensions - 1:
                        possible_moves.append(result[row + 1][column])
                    if column < dimensions - 1:
                        possible_moves.append(result[row][column + 1])
                    if row > 0:
                        possible_moves.append(result[row - 1][column])
                    if column > 0:
                        possible_moves.append(result[row][column - 1])
                    result[row][column] = matrix[row][column] + min(possible_moves)
            print "Pass: " + str(column)
            print_matrix(result)
            print "\n"
    return result[dimensions - 1][dimensions -1]

test_matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]

def print_matrix(matrix):
    for line in matrix:
        print "\t".join(map(str, line))

# Put in the input matrix string
input_matrix = input_matrix.split("\n")
for i in range(len(input_matrix)):
    input_matrix[i] = input_matrix[i].split(',')
    for j in range(len(input_matrix[i])):
            input_matrix[i][j] = int(input_matrix[i][j])

min_sum(input_matrix)
