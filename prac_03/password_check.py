"""Chelsea Lynch"""

MINIMUM_LENGTH = 5

def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    input("Enter a password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        get_password(minimum_length)
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
