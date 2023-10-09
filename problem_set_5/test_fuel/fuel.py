def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    numerator, denominator = fraction.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    if int(denominator) == 0:
        raise ZeroDivisionError
    elif numerator > denominator:
        raise ValueError
    else:
        return round(numerator / denominator * 100)


def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{int(percentage)}%"
    except (ValueError, ZeroDivisionError):
        pass


if __name__ == "__main__":
    main()
