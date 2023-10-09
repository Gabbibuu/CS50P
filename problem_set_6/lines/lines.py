import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] == ".py":
            print(count_lines(sys.argv[1]))
        else:
            sys.exit("Not a Python file")


def count_lines(file):
    try:
        counter = 0
        with open(file, "r") as f:
            for line in f:
                if not (line.lstrip().startswith("#") or line.strip() == ""): #lstrip() espacios en blanco del principio
                    counter += 1
            return counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()