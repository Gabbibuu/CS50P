import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip().title()
        names.append(name)
    except EOFError:
        print("\nAdieu, adieu, to", p.join(names))
        break