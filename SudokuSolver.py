# SudokuSolver.py

def load_puzzle(txt_file):
    # Open .txt file
    file = open(txt_file, 'r')
    # Declare puzzle
    puzzle = [[0 for x in range(9)] for y in range(9)]
    y, x = 0, 0
    # Load in puzzle values from txt_file
    while True:
        char = file.read(1)
        if not char:
            break
        elif char == "," or char == " " or char == "\n":
            continue
        else:
            puzzle[y][x] = int(char)
            x += 1
            if x == 9:
                x = 0
                y += 1

    return puzzle


def solve(puzzle):
    find = find_empty(puzzle)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if valid(puzzle, i, (row, column)):
            puzzle[row][column] = i

            if solve(puzzle):
                return True

            puzzle[row][column] = 0

    return False


def find_empty(puzzle):
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            if puzzle[x][y] == 0:
                return (x, y)  # row, col

    return None


def valid(puzzle, number, position):
    # Check row
    for y in range(len(puzzle[0])):
        if puzzle[position[0]][y] == number and position[1] != y:
            return False

    # Check column
    for y in range(len(puzzle)):
        if puzzle[y][position[1]] == number and position[0] != y:
            return False

    # Check 3x3 box
    box_y = position[0] // 3
    box_x = position[1] // 3
    for x in range(box_y*3, box_y*3 + 3):
        for y in range(box_x*3, box_x*3 + 3):
            if puzzle[x][y] == number and (x, y) != position:
                return False

    return True


def store_puzzle(puzzle):
    for y in range(len(puzzle)):
        if y % 3 == 0 and y != 0:
            print("- - - - - - - - - - - -")
        for x in range(len(puzzle[0])):
            if x % 3 == 0 and x != 0:
                print(" | ", end="")
            if x == 8:
                print(puzzle[y][x])
            else:
                print(str(puzzle[y][x]) + " ", end="")


puzzle = load_puzzle("SudokuPuzzle.txt")
solve(puzzle)
store_puzzle(puzzle)
