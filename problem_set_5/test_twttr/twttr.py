def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    short = []
    for c in word:
        if c.lower() not in vowels:
            short.append(c)
    output = str("".join(short))
    return output


if __name__ == "__main__":
    main()
