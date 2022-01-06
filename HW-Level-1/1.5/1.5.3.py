"""
Create a unique list of mortgage amount
"""


def main():
    mortgage_amount = [1000, 2500, 9800, 4985, 7890, 1000, 5000, 2500, 9800]
    unique_mortgage_amount = list(set(mortgage_amount))
    print(unique_mortgage_amount)


if __name__ == '__main__':
    main()