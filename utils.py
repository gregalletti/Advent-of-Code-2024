import requests
from data import SESSION

# Styles for print
class bcolors:
    OKPURPLE = '\033[95m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'

def download_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = requests.get(url, cookies={'session': SESSION})
    with open(f"./inputs/{year}_{day}.txt", "w" ) as f:
        f.write(r.text)

def print_blue(text):
    print(f"{bcolors.OKCYAN}{text}{bcolors.ENDC}")

def print_purple(text):
    print(f"{bcolors.OKPURPLE}{text}{bcolors.ENDC}")