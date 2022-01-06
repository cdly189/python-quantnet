"""
Using a loop to create a list of odd number from 1 to 1000
"""


def main():
    odd_number = []
    for num in range(1, 1001, 2):
        odd_number.append(num)

    print(odd_number)


if __name__ == '__main__':
    main()