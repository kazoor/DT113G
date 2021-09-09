# Function to convert an integer to binary using recursion.
def int2binary(num):
    # If the number is negative theres nothing we can do conversion wise.
    if num < 0:
        return "Failed to convert negative number to binary."

    # The base case is if the number is 0 so in that case we just return 0
    elif num == 0:
        return 0

    # Otherwise return a recursive call that uses modulo and division to do the conversion.
    else:
        return str(int2binary(num // 2)) + str((num % 2))


def main():
    # Print test cases
    print(int2binary(0))
    print(int2binary(10))


main()
