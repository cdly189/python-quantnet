"""
A list comprehension number 0 to 10,000,000
Use loop to filter a list with number ending with 0
Use list comprehension
Use time module to compare the time of two methods
"""
import time


def main():
    list_number = [i for i in range(10000001)]
    # Using a for loop
    start = time.time()
    multiple_of_ten = []
    for num in list_number:
        if num % 10 == 0:
            multiple_of_ten.append(num)
    end = time.time()
    print('Using for loop')
    print("Seconds: " + str(end - start))

    # Using list comprehension
    start = time.time()
    multiple_of_ten2 = [i for i in list_number if i % 10 == 0]
    end = time.time()
    print('Using list comprehension')
    print("Seconds: " + str(end - start))


if __name__ == '__main__':
    main()