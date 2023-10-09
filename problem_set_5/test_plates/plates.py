def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_digit = True
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha():
        return False
    if s[0] == "0":
        return False
    for i in range(1, len(s)):
        if not s[i].isalpha() and not s[i].isdigit():
            return False
        if i < 2 and s[i].isdigit():
            return False
        if s[i].isdigit() and i != len(s) - 1:
            if (s[i] == "0" and first_digit) or s[i + 1].isalpha():
                return False
            first_digit = False
    return True


if __name__ == "__main__":
    main()