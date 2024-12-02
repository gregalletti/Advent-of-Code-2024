import time
from utils import print_blue, print_purple
from data import YEAR, DAY

# Setup
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

# Common
def is_safe(level):
    diffs = [a - b for a, b in zip(level, level[1:])]
    return all(-3 <= n <=-1 for n in diffs) or all(1 <= n <= 3 for n in diffs)

# Part 1
def part_1():
    ans = 0
    for line in input:
        level = [int(n) for n in line.strip().split()]
        ans += is_safe(level)
    return ans

# Part 2
def part_2():
    ans = 0
    for line in input:
        level = [int(n) for n in line.strip().split()]
        ans += any(is_safe(level[:i] + level[i + 1:]) for i in range(len(level))) # just check if it's safe for all the levels (excluding one)
    return ans

# Parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    
    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {(time.time() - start_time) * 1000} ms")