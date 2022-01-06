"""
Flatten the list from a nested list
"""


def main():
    nested_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    flatten_list = [num for sublist in nested_list for num in sublist]
    print(flatten_list)


if __name__ == '__main__':
    main()