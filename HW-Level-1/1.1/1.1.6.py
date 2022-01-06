"""
Take input to calculate the area of the triangle
"""


def main():
    area = 0
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))

    if base < 0 or height < 0:
        print("Please enter a positive number")
    else:
        area = 0.5 * base * height

    print("The area of the triangle is",area)


if __name__ == '__main__':
    main()