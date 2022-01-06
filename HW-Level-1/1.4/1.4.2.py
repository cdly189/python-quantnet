"""
Find the length of sub list and verify if length of sublist is add up to length of full list
"""


def main():
    mortgage_amount = [100, 150, 200, 293, 458, 569, 789, 998, 1000]
    length_amount = len(mortgage_amount)

    # Mini Mortgages
    mini_mortgages = [x for x in mortgage_amount if x < 200]
    length_mini_mortgages = len(mini_mortgages)
    print(length_mini_mortgages)

    # Standard Mortgages
    standard_mortgages = [x for x in mortgage_amount if 200 <= x < 467]
    length_standard_mortgages = len(standard_mortgages)
    print(length_standard_mortgages)

    # Jumbo Mortgages
    jumbo_mortgages = [x for x in mortgage_amount if x > 467]
    length_jumbo_mortgages = len(jumbo_mortgages)
    print(length_jumbo_mortgages)

    if (length_amount == length_mini_mortgages + length_standard_mortgages + length_jumbo_mortgages):
        print('The lengths of all three lists indeed add up to the length of the full list')


if __name__ == '__main__':
    main()
