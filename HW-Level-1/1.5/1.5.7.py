"""
Divide mortgages into sub-mortgages and filter them into different category
"""


def main():
    mortgage_dict = {'T57QN1': 523, 'HBB56R': 700, 'PDFI4X': 388, 'HWOYO7': 270, 'ZODTXB': 288,
                     '5ZUZWN': 916, 'OKW3N7': 932, 'QPGUF5': 356, 'NUTSPN': 571, 'V44QSJ': 831,
                     'P4P97U': 204, '6E8LVM': 131, 'LHKCD1': 765, 'X29TBZ': 979, 'ODPVS0': 865,
                     'M1J839': 191, 'VW9MBM': 357, 'C11Z2V': 731, '9081AR': 305, '9CZZML': 419,
                     'VH9006': 900, 'TC8KL7': 999, 'GGFQ09': 787, 'W118BK': 727, 'IDM3MQ': 657,
                     '3UC7G8': 130, 'B0EM69': 567, 'S4P6BI': 240, '1JJ8K1': 240, 'JTEV0H': 751}

    # Filter to three seperate dicts
    miniMortgages = {add: mort for add, mort in mortgage_dict.items() if mort < 200}
    standardMortgages = {add: mort for add, mort in mortgage_dict.items() if 200 < mort < 467}
    jumboMortgages = {add: mort for add, mort in mortgage_dict.items() if mort > 467}

    print("Mini\n", miniMortgages)
    print("Standard\n",standardMortgages)
    print("Jumbo\n",jumboMortgages)

    # Modify one value in Jumbo to see if the original change
    jumboMortgages['X29TBZ'] = 100
    print('The value of mortgage X29TBZ in jumboMortgage is: ', jumboMortgages['X29TBZ'])
    print('The value of mortgage X29TBZ in original ledger is: ', mortgage_dict['X29TBZ'])
    # The original does not change

    # Extract the lists of amounts from each separate dict
    miniValue = list(miniMortgages.values())
    print(miniValue)

    standardValue = list(standardMortgages.values())
    print(standardValue)

    jumboValue = list(jumboMortgages.values())
    print(jumboValue)

    
if __name__ == '__main__':
    main()