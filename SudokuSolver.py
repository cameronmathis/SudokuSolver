# SudokuSolver.py

def load_puzzle(txt_file):
    # Open .txt file
    file = open(txt_file, 'r')
    # Declare puzzle
    puzzle = [[0 for x in range(9)] for y in range(9)]
    x, y = 0, 0
    # Load in puzzle values from txt_file
    while True:
        char = file.read(1)
        if not char:
            break
        elif char == "," or char == " " or char == "\n":
            continue
        else:
            puzzle[x][y] = int(char)
            y += 1
            if y == 9:
                y = 0
                x += 1
    return puzzle


def find_empty(puzzle):
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            if puzzle[x][y] == 0:
                return x, y  # row, col


def print_puzzle(puzzle):
    for x in range(len(puzzle)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - -")
        for y in range(len(puzzle[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")
            if y == 8:
                print(puzzle[x][y])
            else:
                print(str(puzzle[x][y]) + " ", end="")


puzzle = load_puzzle("SudokuPuzzle.txt")
print_puzzle(puzzle)
