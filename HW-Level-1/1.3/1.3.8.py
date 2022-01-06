"""
Using **kwargs to display all pass-in keywords
"""


def description(name, age, *args, **kwargs):
    print(name)
    print(age)
    print(kwargs)


def main():
    description('Davis', 27, state='Virginia', height='6ft8', weight='200 lbs')
    description('Luke', 50, 'Black', height='5ft5')
    description('John', 15, 'White', state='Florida', weight='150 lbs')


if __name__ == '__main__':
    main()