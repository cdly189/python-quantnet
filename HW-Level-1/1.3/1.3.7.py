"""
A function that takes name, age as parameters. It should also take **kwargs
"""


def description(name, age, *args, **kwargs):
    print(name)
    print(age)
    print(kwargs.get('state'))
    print(kwargs.get('height'))
    print(kwargs.get('weight'))
    print(args)


def main():
    description('Davis', 27, state='Virginia', height='6ft8', weight='200 lbs')
    description('Luke', 50, 'Black', height='5ft5')
    description('John', 15, 'White',state='FLorida',weight='150 lbs')


if __name__ == '__main__':
    main()