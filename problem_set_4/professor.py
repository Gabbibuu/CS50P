import random


def main():
    problems = 10
    score = 0
    chances = 3
    lvl = get_level()
    while problems != 0:
        if chances == 3:
            x = generate_integer(lvl)
            y = generate_integer(lvl)
        try:
            input_answer = int(input(f"{x} + {y} = "))
            if input_answer == (x + y):
                problems -= 1
                score += 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances -= 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {(x + y)}"))
            chances = 3
            problems -= 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    elif level == 3:
        n = random.randint(100, 999)
    return n


if __name__ == "__main__":
    main()
