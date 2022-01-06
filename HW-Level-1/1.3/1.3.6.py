"""
An alternative mean function to use *args instead of a taking a list of numbers
"""


def argsMean(*args):
    return sum(args) / len(args)


def main():
    print(argsMean(3, 5, 7, 9))
    print(argsMean(*[10.0, 20.0, 30.0, 40.0]))
    print(argsMean(1.3, 4.5, 6.7, 11.2, 100, 987.6))


if __name__ == '__main__':
    main()