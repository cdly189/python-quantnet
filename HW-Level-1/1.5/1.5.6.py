"""
Find a mode of a dictionary
"""
import collections


def freqmap(values):
    map_value = {}
    for v in values:
        if not map_value.get(v):
            map_value[v] = 1
        else:
            map_value[v] += 1
    return map_value


def mode(map):
    data = collections.Counter(map)
    max_value = max(list(data.values()))
    mode_value = [num for num, freq in freqmap(map).items() if freq == max_value]
    if len(mode_value) == len(map):
        print('No mode in the list')
    else:
        print(mode_value)


def main():
    mode([1, 2, 4, 1, 2])
    mode([1, 2, 3, 4])
    mode([1, 2, 3, 4, 1])


if __name__ == '__main__':
    main()
