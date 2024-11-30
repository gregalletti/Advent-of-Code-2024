from utils import download_input
from data import YEAR, DAY
import os.path

# Create the solution file
template_path = "template.py"
solution_path = f"./solutions/{YEAR}_{DAY}.py"

with open(template_path, 'r') as template_file:
    content = template_file.read()

with open(solution_path, 'w') as solution_file:
    solution_file.write(content)

print(f"Content of '{template_path}' copied to '{solution_path}'")

# Download the input file
input_path = f"./inputs/{YEAR}_{DAY}.txt"

if not os.path.isfile(input_path):
    download_input(YEAR, DAY)

print(f"Input file for {YEAR}-{DAY} downloaded to '{input_path}'")