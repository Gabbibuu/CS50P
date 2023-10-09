import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] == ".csv":
            sort(sys.argv[1], sys.argv[2])
        else:
            sys.exit("Not a CSV file")


def sort(before, after):
    try:
        with open(before) as f_input:
            reader = csv.DictReader(f_input)
            with open(after, "w") as f_output:
                writer = csv.DictWriter(f_output, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == "__main__":
    main()