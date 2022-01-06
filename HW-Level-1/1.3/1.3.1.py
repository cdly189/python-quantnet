"""
A function that can print out the day of the week for a given number
I.e. Sunday is 1, Monday is 2, etc
"""

def dayofWeek(num):
    day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', ' Thursday', 'Friday', ' Saturday']
    day_th = day[num - 1]
    print(day_th + ' is ' + str(num))
    
def main():
    dayofWeek(1)
    dayofWeek(2)
    dayofWeek(3)


if __name__ == '__main__':
    main()