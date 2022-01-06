"""
A function that calculates the variance of a passed-in list
With Degree of Freedom = 0 = Population Variance
Degree of Freedom = 1 = Sample Variance
"""


def mean(lists):
    total = 0
    for l in lists:
        total += l
    average = total / len(lists)
    return average

def variance(lists,degofFreedom = 1):
    mean_list = mean(lists)
    l_var = [(i - mean_list)**2 for i in lists]
    return sum(l_var) / (len(l_var) - degofFreedom)


def main():
    l = [1, 2, 3, 4, 5, 6]
    # Test Sample Variance
    print(variance(l,degofFreedom=1))
    # Test Population Variance
    print(variance(l,degofFreedom=0))


if __name__ == '__main__':
    main()