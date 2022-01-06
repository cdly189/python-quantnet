"""
A set of 20 most common male names in US and UK. Perform several set technique on them
"""


def main():
    # Male first name in the US
    set1 = {'James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles',
            'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew', 'Kenneth'}

    # Male first name in the UK
    set2 = {'Oliver', 'George', 'Harry', 'Noah', 'Jack', 'Leo', 'Arthur', 'Muhammad', 'Oscar', 'Charlie',
            'Jacob', 'Thomas', 'Henry', 'William', 'Alfie', 'Archie', 'Joshua', 'Freddie', 'Theo', 'Issac'}

    # a. First name that appear in both sets
    name_both_sets = set1.intersection(set2)
    print(name_both_sets)

    # b. Name in US but not in UK
    US_not_UK = set1.difference(set2)
    print(US_not_UK)

    # c. Name in UK but not in US
    UK_not_US = set2.difference(set1)
    print(UK_not_US)

    # d. Using set comprehension to create a subset of names that have more than five letters
    set1_5character = {i for i in set1 if len(i) > 5}
    print(set1_5character)
    set2_5character = {i for i in set2 if len(i) > 5}
    print(set2_5character)

if __name__ == '__main__':
    main()
