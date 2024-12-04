import time
from utils import print_blue, print_purple
from data import YEAR, DAY

# Setup
start_time = time.time()
path = f"../inputs/{YEAR}_{DAY}.txt"

# Common
def search(puzzle, target, coordinates, move):
    row, col = coordinates
    for char in list(target):
        if row < 0 or row > maxRow - 1:
            return False
        if col < 0 or col > maxCol - 1:
            return False
        if puzzle[row][col] != char:
            return False
        
        row += move[0]
        col += move[1]
    
    return True

# Part 1
def part_1():
    ans = 0
    for row in range(maxRow):
        for col in range(maxCol):
            moves = [(0,1), (0,-1), (-1,0), (1,0), (-1,1), (-1,-1), (1,1), (1,-1)]
            for move in moves:
                if search(puzzle, "XMAS", (row,col), move):
                    ans += 1
                
    return ans

# Part 2
def part_2():
    ans = 0
    for row in range(maxRow):
        for col in range(maxCol):
            # search for target in diagonal (down-righ)
            if search(puzzle, "MAS", (row,col), (1,1)) or search(puzzle, "SAM", (row,col), (1,1)):
                # search in other diagonal (down-left)
                if search(puzzle, "MAS", (row,col + 2), (1,-1)) or search(puzzle, "SAM", (row,col + 2), (1,-1)):
                    ans += 1
    
    return ans

# Parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    puzzle = []
    for i, line in enumerate(input):
        puzzle.append(list(line))

    maxRow = len(puzzle)
    maxCol = len(puzzle[0])

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {(time.time() - start_time) * 1000} ms")