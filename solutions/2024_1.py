import time
from utils import print_blue, print_purple
from data import YEAR, DAY

# Setup
start_time = time.time()
path = f"./inputs/{YEAR}_{DAY}.txt"

# Common
def common_function(input):
    left, right = [], []
    for line in input:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    return left, right

# Part 1
def part_1():
    ans = 0
    for i in range(len(left)):
        ans += abs(left[i] - right[i])
    return ans

# Part 2
def part_2():
    freq = {}
    for n in right:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    ans = 0
    for i in range(len(left)):
        if left[i] in freq:
            ans += left[i] * freq[right[i]]
    return ans

# Parsing and execution
with open(path) as f:
    input = (f.read().splitlines())
    
    left, right = common_function(input)

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {(time.time() - start_time) * 1000} ms")