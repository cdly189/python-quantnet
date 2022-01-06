"""
A function that calculates the variance of a passed-in list
"""


def mean(lists):
    total = 0
    for l in lists:
        total += l
    average = total / len(lists)
    return average

def variance(lists):
    mean_list = mean(lists)
    l_var = [(i - mean_list)**2 for i in lists]
    return sum(l_var) / len(l_var)


def main():
    print(variance([1, 2, 3]))
    print(variance([1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main()