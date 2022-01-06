"""
Identify the min and max in each sublist
"""


def main():
    mortgage_amount = [100, 150, 200, 293, 458, 569, 789, 998, 1000]

    # Mini Mortgages
    mini_mortgages = [x for x in mortgage_amount if x < 200]
    # Minimum and maximum amount in mini mortgages sub list
    print('Mini Mortgages')
    print(min(mini_mortgages))
    print(max(mini_mortgages))

    # Standard Mortgages
    standard_mortgages = [x for x in mortgage_amount if 200 <= x < 467]
    # Minimum and maximum amount in standard mortgages sub list
    print('Standard Mortgages')
    print(min(standard_mortgages))
    print(max(standard_mortgages))

    # Jumbo Mortgages
    jumbo_mortgages = [x for x in mortgage_amount if x > 467]
    # Minimum and maximum amount in jumbo mortgages sub list
    print('Jumbo Mortgages')
    print(min(jumbo_mortgages))
    print(max(jumbo_mortgages))


if __name__ == '__main__':
    main()