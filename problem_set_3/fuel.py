while True:
    try:
        fraction = input("Fraction: ")
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)
        percentage = round(numerator / denominator * 100)
        if numerator <= denominator:
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
    except (ValueError, ZeroDivisionError):
        pass