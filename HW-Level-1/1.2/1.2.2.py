"""
Ask for user input and calculate the average
"""


def main():
    list_numbers = [1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0]
    # display the first two numbers
    print(list_numbers[0:2])
    # display the last two numbers
    print(list_numbers[-2:])
    # display all the number except the last number
    print(list_numbers[0:-1])
    # display all the number except the first number
    print(list_numbers[1:])
    # display all the numbers besides the first two and last three numbers
    print(list_numbers[2:-3])
    # Append one number to the end of the list
    list_numbers.append(11)
    # Append five numbers to the end of the list, using a single operation
    list_numbers.extend([12.0, 13, 14.0, 15, 16.0])
    # Insert one number right after the third number in the list
    list_numbers.insert(3, 3.5)
    # Modify the fourth-to-last number in the list
    list_numbers[-1] = list_numbers[3]
    # Display the list backward, using slicing
    print(list_numbers[::-1])
    # Display every second item in the list
    print(list_numbers[::2])
    # Display every second item in the list, backwards
    print(list_numbers[::-2])


if __name__ == '__main__':
    main()