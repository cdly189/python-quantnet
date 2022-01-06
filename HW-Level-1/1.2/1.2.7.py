"""
Create two lists: players and injured players
Use list comprehension to produce a new list containing non-injured (active) players
"""


def main():
    players = ['John', 'Brady', 'Davis', 'Lebron', 'Kuzma', 'Gronk', 'Messi', 'Ronaldo', 'Rooney',
               'Devin', 'Booker', 'Vogel']
    injured_players = ['Devin', 'Vogel', 'Booker', 'Kuzma', 'John']
    active_players = [x for x in players if x not in injured_players]
    print(active_players)


if __name__ == '__main__':
    main()