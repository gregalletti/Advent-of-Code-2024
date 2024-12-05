import time
from utils import print_blue, print_purple
from data import YEAR, DAY
from collections import defaultdict

# Setup
start_time = time.time()
path = f"../inputs/{YEAR}_{DAY}.txt"

# Common
def custom_sort(to_sort):
    return sorted(to_sort, key=lambda num: -len([rule for rule in rules[num] if rule in to_sort]))

# Part 1
def part_1():
    ans = 0
    for update in updates:
        target = custom_sort(update)
        if update == target:
            middle = update[len(update) // 2]
            ans += middle
    return ans

# Part 2
def part_2():
    ans = 0
    for update in updates:
        target = custom_sort(update)
        if update != target:
            middle = target[len(update) // 2]
            ans += middle
    return ans

# Parsing and execution
with open(path) as f:
    input = [section.strip().splitlines() for section in f.read().split("\n\n") if section.strip()]
    
    rules =  defaultdict(list)

    for rule in input[0]:
        first, second = map(int, rule.split('|'))
        rules[first].append(second)

    updates = [list(map(int, line.split(','))) for line in input[1]]

    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {(time.time() - start_time) * 1000} ms")