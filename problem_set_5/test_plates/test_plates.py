from plates import is_valid


#Start with at least two letters
def test_begintwoletters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False


#Maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def test_length():
    assert is_valid("HICS50") == True
    assert is_valid("CS") == True
    assert is_valid("HELLOCS50") == False


#Numbers cannot be used in the middle of a plate
#The first number used cannot be a ‘0’
def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


#No periods, spaces, or punctuation marks
def test_punct():
    assert is_valid("CS50!") == False