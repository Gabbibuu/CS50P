#REQUIREMENTS
#start with at least two letters
#maximum of 6 characters (letters or numbers) and a minimum of 2 characters
#numbers cannot be used in the middle of a plate; they must come at the end
#the first number used cannot be a ‘0’
#no periods, spaces, or punctuation marks are allowed

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
        if s[i].isdigit() and i != len(s) - 1:
            if (s[i] == "0" and first_digit) or s[i + 1].isalpha():
                return False
            first_digit = False
    return True

main()