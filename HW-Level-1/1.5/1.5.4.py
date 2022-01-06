"""
A length of mortgage term and perform some set techniques
"""


def main():
    mortgage_term = {10, 15, 30}
    mortgage_term.add(5)
    mortgage_term.remove(15)

    # if I use .remove function to remove any items that are not in the set(45), the IDE will raise error
    # the solution is to use .discard
    mortgage_term.discard(45)
    print(mortgage_term)


if __name__ == '__main__':
    main()
