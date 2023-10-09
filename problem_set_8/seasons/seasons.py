import sys
import operator
import inflect
from datetime import date


p = inflect.engine()


def main():
    try:
        birth = input("Date of Birth: ")
        sub = operator.sub(date.today(), date.fromisoformat(birth))
        print(convert(sub.days))
    except ValueError:
        sys.exit("Invalid date")


def convert(time):
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()