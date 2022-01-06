"""
List of names and ages and zip them
Use list comprehension to produce name for whom age is greater than 18
"""


def main():
    list_of_names = ['Devin', 'Vogel', 'Booker', 'Kuzma', 'John']
    ages = [23, 49, 25, 17, 10]
    combined_list = list(zip(list_of_names,ages))
    print(combined_list)

    adult = [name for name,age in combined_list if age >= 18]
    print(adult)


if __name__ == '__main__':
    main()