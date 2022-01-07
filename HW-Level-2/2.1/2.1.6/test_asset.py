from asset.asset import Asset


def main():
    asset1 = Asset(10000)
    print('Test 1')
    print('The annual depreciation rate is:', asset1.annualDepr())
    print()

    print('Test 2')
    print('The monthly depreciation rate is:', asset1.monthlyDepr())
    print()

    print('Test 3')
    t = 10
    print('The current value of the asset at time t=' + str(t) + ' is: ' + str(asset1.value(t)))
    print()


if __name__ == '__main__':
    main()