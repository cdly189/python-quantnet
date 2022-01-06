"""
Keep asking the user for a number, until the user enter s
"""


def main():
    user_input = []

    while True:
        num = ''
        while num == '':
            num = input("Enter a number (enter s to stop): ")
        if num != 's':
            user_input.append(float(num))
        else:
            break

    total = 0.0
    for num in user_input:
        total += num

    average = total / len(user_input)

    print('The average is ' + str(average))


if __name__ == '__main__':
    main()
