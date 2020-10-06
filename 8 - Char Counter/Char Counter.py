def char_count(string):
    chars = 0
    digits = 0
    symbols = 0
    for index in range(len(string)):
        if string[index].isalpha():
            chars += 1
        elif string[index].isdigit():
            digits += 1
        else:
            symbols += 1

    print("Chars: " + str(chars))
    print("Digits: " + str(digits))
    print("Symbols: " + str(symbols))


str1 = "P@#yn26at^&i5ve"
char_count(str1)
