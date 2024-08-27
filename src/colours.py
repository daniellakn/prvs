def print_red(message):
    print(f"\033[91m{message}\033[0m", end='')

def print_green(message):
    print(f"\033[32m{message}\033[0m", end='')

def print_yellow(message):
    print(f"\033[93m{message}\033[0m")

def print_bold(message):
    print(f"\033[1m{message}\033[0m", end='')