"""
Display the type of the variable that contains the value that the user entered
"""


def main():
    user_input = input("What's your favorite color? ")
    print(user_input)
    print(type(user_input))


if __name__ == '__main__':
    main()