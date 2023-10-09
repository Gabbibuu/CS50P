grocery_list = {}
while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        print()
        break
grocery_list = sorted(grocery_list.items()) #Sort alphabetically
for item, count in grocery_list:
    print(f"{count} {item}")