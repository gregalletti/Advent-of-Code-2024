import time
from utils import print_blue, print_purple
from data import YEAR, DAY

# Setup
start_time = time.time()
path = f"../inputs/{YEAR}_{DAY}.txt"

# Common
def common_function():
    pass

# Part 1
def part_1():
    pass

# Part 2
def part_2():
    pass

# Parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    
    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {(time.time() - start_time) * 1000} ms")