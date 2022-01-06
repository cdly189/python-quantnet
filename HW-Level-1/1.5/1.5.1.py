"""
Use set instead of lists from 1.2.7
"""


def main():
    players = set(['John', 'Brady', 'Davis', 'Lebron', 'Kuzma', 'Gronk', 'Messi', 'Ronaldo', 'Rooney',
               'Devin', 'Booker', 'Vogel'])
    injured_players = set(['Devin', 'Vogel', 'Booker', 'Kuzma', 'John'])
    active_player = players.difference(injured_players)
    print(active_player)


if __name__ == '__main__':
    main()