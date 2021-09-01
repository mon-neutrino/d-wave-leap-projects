# NOT MY CODE, JUST TESTING

from __future__ import print_function
import dimod
import math
import sys
import copy
from dimod.generators.constraints import combinations
from hybrid.reference import KerberosSampler


def get_label(row,col,digit):
    #returns a string of cell coordinates and cell value in standard format
    return "{row},{col}_{digit}".format(**locals())

def get_matrix(filename):
    # returns list of lists containing content of input text file
    with open(filename, "r") as f: #"r" = read
        content = f.readlines()

    lines = []
    for line in content:
        new_line = line.rstrip() #strip any whitespace after last value

        if new_line:
            new_line = list(map(int, new_line.split(' '))) #make list of row by separating by ' '
            lines.append(new_line)

    return lines

def is_correct(matrix):
    # verify matrix satisies constraints
    # args: matrix: list contains 'n' lists where each of the 'n' lists contains 'n digits (refer to sudoku structure)

    n = len(matrix) # no of rows/columns
    m = int(math.sqrt(n)) # no of subsquare rows/columns
    unique_digits = set(range(1, n+1)) # digits in a solution set of (1-9)

    # verifying rows
    for row in matrix:
        if set(row) != unique_digits:
            print("error in row: ", row)
            return False

    # verifying columns
    for j in range(n):
        col = [matrix[i][j] for i in range(n)]
        if set(col) != unique_digits:
            print("error in col: ", col)
            return False

    # verifying subsquares
    subsquare_coords = [(i, j) for i in range(m) for j in range(m)]
    for r_scalar in range(m):
        for c_scalar in range(m):
            subsquare = [matrix[i + r_scalar * m][j + c_scalar * m] for i, j
                         in subsquare_coords]
            if set(subsquare) != unique_digits:
                print("Error in sub-square: ", subsquare)
                return False
    
    return True

def build_bqm(matrix):
    # building bqm w sudoku constraints

    # set up
    n = len(matrix) # no. of rows/colomn in sudoku
    m = int(math.sqrt(n)) # no. of rows/column in subsquare
    digits = range(1, n+1)

    bqm = dimod.BinaryQuadraticModel({}, {}, 0.0, dimod.SPIN) # dimod.SPIN is variable type i think

    # C1: each node can only select one digit
    for row in range(n):
        for col in range(n):
            node_digits = [get_label(row, col, digit) for digit in digits]
            one_digit_bqm = combinations(node_digits, 1) # "creates minimized bqm when k (1) of n (node_digits) is selected"
            bqm.update(one_digit_bqm)

    # C2: each row of nodes can't have duplicate digits
    for row in range(n):
        for digit in digits:
            row_nodes = [get_label(row, col, digit) for col in range(n)]
            row_bqm = combinations(row_nodes, 1) # "creates minimized bqm when k (1) of n (node_digits) is selected"
            bqm.update(row_bqm)

    # C3: each column of nodes can't have duplicate digits
    for col in range(n):
        for digit in digits:
            col_nodes = [get_label(row, col, digit) for row in range(n)]
            col_bqm = combinations(col_nodes, 1) # "creates minimized bqm when k (1) of n (node_digits) is selected"
            bqm.update(col_bqm)

    # C4: each subsquare can't have duplicates
    # builds indices of basic subsquares
    subsquare_indices = [(row, col) for row in range(m) for col in range(m)]

    # build full sudoku array
    for r_scalar in range(m):
        for c_scalar in range(m):
            for digit in digits:
                # shifts for moving subsquare space inside sudoku matrix - I DONT RLLY UNDERSTAND WHY
                row_shift = r_scalar * m
                col_shift = c_scalar * m

                # build labels for subsquare
                subsquare = [get_label(row + row_shift, col + col_shift, digit) for row, col in subsquare_indices]
                subsquare_bqm = combinations(subsquare, 1)
                bqm.update(subsquare_bqm)

    # C5: fix known values
    for row, line in enumerate(matrix):
        for col, value in enumerate(line):
            if value > 0:
                bqm.fix_variable(get_label(row, col, value), 1)
                # we specificy 1 in the fixed_variable function for same reason as the rest on top
                # we only want 1 value to be picked

    return bqm

def solve_sudoku(bqm, matrix):
    """Solve BQM and return matrix with solution."""
    solution = KerberosSampler().sample(bqm,
                                        max_iter=10,
                                        convergence=3,
                                        qpu_params={'label': 'Example - Sudoku'})
    best_solution = solution.first.sample
    solution_list = [k for k, v in best_solution.items() if v == 1]

    result = copy.deepcopy(matrix)

    for label in solution_list:
        coord, digit = label.split('_')
        row, col = map(int, coord.split(','))

        if result[row][col] > 0:
            # the returned solution is not optimal and either tried to
            # overwrite one of the starting values, or returned more than
            # one value for the position. In either case the solution is
            # likely incorrect.
            continue

        result[row][col] = int(digit)

    return result

if __name__ == '__main__':
    #read user input
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sudoku.txt"
        print("Warning: using default problem file, '{}'. Usage: python "
              "{} <sudoku filepath>".format(filename, sys.argv[0]))

    # read sudoku problem as matrix
    matrix = get_matrix(filename)

    # solve bqm and update matrix
    bqm = build_bqm(matrix)
    result = solve_sudoku(bqm, matrix)

    #print solution
    for line in result:
        print(*line, sep=" ") # print list w/o commas or bracket
    
    # verify
    if is_correct(result):
        print("The solution is correct")
    else:
        print("The solution is incorrect")