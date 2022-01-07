from loan.loan_base import Loan


def main():
    print('Test 1')
    annual_rate = .007
    monthly_rate_math = annual_rate / 12
    monthly_rate_function = Loan.monthlyRate(annual_rate)
    print('Does the Loan.monthlyRate() function works? ', monthly_rate_math == monthly_rate_function)
    print()

    print('Test 2')
    monthly_rate = .007
    annual_rate_math = annual_rate * 12
    annual_rate_function = Loan.annualRate(monthly_rate)
    print('Does the Loan.annualRate() function works? ', annual_rate_math == annual_rate_function)
    print()

    loan1 = Loan(100000, 0.050, 30)
    face = 100000
    rate = 0.050
    term = 30
    period = 12
    print('Loan info: ' + str(loan1.notional) + ' loan, at monthly rate of ' + str(loan1.rate) + ' over '
          + str(loan1.term) + ' months.')

    # calcMonthlyPmt function
    print('Test 3')
    print('The monthly payment of this loan is: ', Loan.calcMonthlyPmt(face, rate, term))
    print()

    # calcBalance function
    print('Test 4')
    print('The outstanding balance of this loan at period ' + str(period) + ' months is: ' +
          str(Loan.calcBalance(face, rate, term, period)))
    print()

    # calcBalance function
    print('Test 5')
    print('The monthly payment of this loan is: ', loan1.monthlyPayment())
    print()

    # calcBalance function
    print('Test 6')
    print('The outstanding balance of this loan at period ' + str(period) + ' months is: ' +
          str(loan1.balance(period)))
    print()

    # Benefits of static methods:
    # 1. Useful to group related methods that should be executed at global level.
    # 2. Increase code readability.


if __name__ == '__main__':
    main()