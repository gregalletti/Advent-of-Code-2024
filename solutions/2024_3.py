import time
from utils import print_blue, print_purple
from data import YEAR, DAY
import re

# Setup
start_time = time.time()
path = f"../inputs/{YEAR}_{DAY}.txt"

# Common
def common_function():
    pass

# Part 1
def part_1():
    valid = re.findall(r"mul\(\d{0,3},\d{0,3}\)", input)
    ans = 0
    for exp in valid:
        r = re.findall(r"\d+", exp)
        ans += int(r[0]) * int(r[1])
        
    return ans

# Part 2
def part_2():
    valid = re.findall(r"mul\(\d{0,3},\d{0,3}\)|do\(\)|don't\(\)", input)
    ans = 0
    enabled = True

    for exp in valid:
        if(exp == "do()"):
            enabled = True
        elif(exp == "don't()"):
            enabled = False
        else:
            if(enabled):
                r = re.findall(r"\d+", exp)
                ans += int(r[0]) * int(r[1])
    
    return ans


# Parsing and execution
with open(path) as f:
    input = (f.read())
    
    print_blue(part_1())
    print(f"Completed {YEAR}-{DAY} PART 1 in {(time.time() - start_time) * 1000} ms\n")

    start_time = time.time()
    print_purple(part_2())
    print(f"Completed {YEAR}-{DAY} PART 2 in {(time.time() - start_time) * 1000} ms")