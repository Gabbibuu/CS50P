import sys
import os #File extension
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        input = os.path.splitext(sys.argv[1])
        output = os.path.splitext(sys.argv[2])
        if output[1].lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid output")
        elif input[1].lower() == output[1].lower():
            edit(sys.argv[1], sys.argv[2])
        else:
            sys.exit("Input and output have different extensions")


def edit(before, after):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(before) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, shirt)
            input_cropped.save(after)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


if __name__ == "__main__":
    main()