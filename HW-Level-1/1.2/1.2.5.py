"""
Combine an odd and even number list
"""


def main():
    odd_number = list(range(1, 1001, 2))
    even_number = list(range(2, 1001, 2))
    combined_list = list(zip(odd_number, even_number))
    print(combined_list)
    # Create a combined list backwards
    print(combined_list[::-1])


if __name__ == '__main__':
    main()