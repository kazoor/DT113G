def changeChar(str, index, char):
    # Start with an empty string and append the characters before the index,
    # when our index is hit, replace the character and then append the remaining characters of the string.
    return str[:index] + char + str[index+1:]


def main():
    # Print test cases.
    print(changeChar("This is a string", 0, "X"))
    print(changeChar("This is a string", 5, "X"))
    print(changeChar("This is a string", 10, "X"))


main()
