"""
Using list comprehension to create squared number from 0 to 100
Filter list to contain number greater than 1000
Filter to create another list that contain even numbers
"""


def main():
    # Create a list of squared numbers from 0 to 100
    squared_number = [i**2 for i in range(101)]
    print(squared_number)

    # Filter list to only contain number that is greater than 1000
    greater_thousand = [i**2 for i in range(101) if i**2 > 1000]
    print(greater_thousand)

    # Even number
    even_number = [i**2 for i in range(101) if i**2 %2 == 0 and i**2 > 1000 ]
    print(even_number)


if __name__ == '__main__':
    main()