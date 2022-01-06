"""
Using a loop to create a list of even number from 1 to 1000
"""


def main():
    even_number = []
    for num in range(2,1001,2):
        even_number.append(num)

    print(even_number)


if __name__ == '__main__':
    main()