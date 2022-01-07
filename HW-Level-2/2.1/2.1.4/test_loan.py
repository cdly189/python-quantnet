from loan.loan_base import Loan


def main():
    loan1 = Loan(100000, 0.050, 30)
    face = 100000
    rate = 0.050
    term = 30
    period = 12

    print('Loan info: ' + str(loan1.notional) + ' loan, at monthly rate of ' + str(loan1.rate) + ' over '
          + str(loan1.term) + ' months.')

    # CalcMonthlyPmt function
    print('Test 1')
    print('The monthly payment of this loan is: ', Loan.calcMonthlyPmt(face, rate, term))
    print()

    # calcBalance function
    print('Test 2')
    print('The outstanding balance of this loan at period ' + str(period) + ' months is: ' +
          str(Loan.calcBalance(face, rate, term, period)))
    print()

    # calcBalance function
    print('Test 3')
    print('The monthly payment of this loan is: ', loan1.monthlyPayment())
    print()

    # calcBalance function
    print('Test 4')
    print('The outstanding balance of this loan at period ' + str(period) + ' months is: ' +
          str(loan1.balance(period)))
    print()

    # Benefits of class methods:
    # Useful for methods that are related to the class but not meant to perform on an instantiated object.


if __name__ == '__main__':
    main()