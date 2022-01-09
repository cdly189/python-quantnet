"""
Demonstration of lambda to calculate hypotenuse
"""
from math import sqrt


def main():
    hypo = lambda b,h: sqrt(b**2 + h**2)
    print(hypo(3,4))
    print(hypo(5,12))


if __name__ == '__main__':
    main()