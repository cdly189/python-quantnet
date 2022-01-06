"""
Divide mortgages into sub-mortgages and filter them into different category
"""

def weightedaverageRate(loan):
    total_loan = sum(i[0] for i in loan)
    for i in loan:
        WAR = i[0] * i[1] / total_loan
        return round(WAR, 3)

def weightedaverageMaturity(loan):
    total_loan = sum(i[0] for i in loan)
    for i in loan:
        WAM = i[0] * i[2] / total_loan
        return round(WAM, 3)



def main():
    mortgage_dict = {'T57QN1': (523000, .030, 360), 'HBB56R': (700000, .025, 302), 'PDFI4X': (388000, .050, 240),
                     'HWOYO7': (270000, .030, 200), 'ZODTXB': (288000, .020, 260), '5ZUZWN': (916000, .030, 318),
                     'OKW3N7': (932000, .045, 350), 'QPGUF5': (356000, .040, 312), 'NUTSPN': (571000, .015, 355),
                     'V44QSJ': (831000, .010, 123), 'P4P97U': (204000, .035, 341), '6E8LVM': (131000, .025, 272),
                     'LHKCD1': (765000, .020, 201), 'X29TBZ': (979000, .350, 207), 'ODPVS0': (865000, .070, 364),
                     'M1J839': (191000, .015, 205), 'VW9MBM': (357000, .030, 187), 'C11Z2V': (731000, .060, 129)}

    # Extract the list of tuple values and sorted by amount
    mortgage_val_list = list(mortgage_dict.values())
    mortgage_val_list.sort(key=lambda x: x[0], reverse=True)
    print(mortgage_val_list)

    print(weightedaverageRate(mortgage_val_list))
    print(weightedaverageMaturity(mortgage_val_list))

    # Create new dict with term as key
    term_as_key = {i[2]: (i[0], i[1]) for i in mortgage_dict.values()}
    print(term_as_key)


if __name__ == '__main__':
    main()