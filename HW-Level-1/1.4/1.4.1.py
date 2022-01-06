"""
Divide mortgages into sub-mortgages and filter them into different category
"""


def main():
    mortgage_amount = [100, 150, 200, 293, 458, 569, 789, 998, 1000]
    miniMortgages = [x for x in mortgage_amount if x < 200]
    standardMortgages = [x for x in mortgage_amount if 200 < x < 467]
    jumboMortgages = [x for x in mortgage_amount if x > 467]

    mini_mortgages_all = all(i for i in mortgage_amount if i < 200)
    print(mini_mortgages_all)
    mini_mortgages_any = any(i for i in mortgage_amount if i < 200)
    print(mini_mortgages_any)



if __name__ == '__main__':
    main()