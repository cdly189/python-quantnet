from asset.asset import Asset, Car, HouseBase, Lambourghini, Lexus, Civic, PrimaryHome, VacationHome
#######################


def main():
    print('Test 1')
    asset1 = Asset(1000000)
    print('The asset annual depreciation rate is:', asset1.annualDeprRate(12))
    print()

    print('Test 2')
    car1 = Car(1000000)
    print('The car annual depreciation rate is:', car1.annualDeprRate(12))
    print()

    print('Test 3')
    lambo1 = Lambourghini(1000000)
    print('The car annual depreciation rate is:', lambo1.annualDeprRate(12))
    print()

    print('Test 4')
    lexus1 = Lexus(1000000)
    print('The car annual depreciation rate is:', lexus1.annualDeprRate(12))
    print()

    print('Test 5')
    civic1 = Civic(1000000)
    print('The car annual depreciation rate is:', civic1.annualDeprRate(12))
    print()

    print('Test 6')
    house1 = HouseBase(1000000)
    print('The house annual depreciation rate is:', house1.annualDeprRate(12))
    print()

    print('Test 7')
    primaryhouse1 = PrimaryHome(1000000)
    print('The house annual depreciation rate is:', primaryhouse1.annualDeprRate(12))
    print()

    print('Test 8')
    vacayhouse1 = VacationHome(1000000)
    print('The house annual depreciation rate is:', vacayhouse1.annualDeprRate(12))
    print()

   
if __name__ == '__main__':
    main()