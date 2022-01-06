"""
A function that calculates the mean of a passed-in list
"""


def mean(lists):
    total = 0
    for l in lists:
        total += l
    average = total / len(lists)
    return average


def main():
    print(mean([1, 2, 3]))
    print(mean([1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main()
