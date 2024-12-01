# Styles for print
class bcolors:
    OKPURPLE = '\033[95m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'

def print_blue(text):
    print(f"{bcolors.OKCYAN}{text}{bcolors.ENDC}")

def print_purple(text):
    print(f"{bcolors.OKPURPLE}{text}{bcolors.ENDC}")