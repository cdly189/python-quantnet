from loan.loan_base import Loan
from utils.timer import Timer


def main():
    print('Test 1')
    loan1 = Loan(100000, 0.050, 30)
    t = 20
    run_time = Timer(0, 0, 0)

    print('Calculation using formulas:')
    print('Loan info: ' + str(loan1.notional) + ' loan, at monthly rate of ' + str(loan1.rate) + ' over '
          + str(loan1.term) + ' months.')

    run_time.start()
    print('The interest due of this loan is: ', loan1.interestDue(t))
    run_time.end()
    print()

    # Test 2
    # Demo principalDue function
    print('Test 2')
    run_time.start()
    print('The principal due of this loan is: ', loan1.principalDue(t))
    run_time.end()
    print()

    # Test 3
    # Demo balance function
    print('Test 3')
    run_time.start()
    print('The remaining balance of this loan is: ', loan1.balance(t))
    run_time.end()
    print()

    # Test 4
    # Demo interestDue function
    print('Test 4')
    run_time.start()
    print('The interest due of this loan is: ', loan1.interestDueRecursive(t))
    run_time.end()
    print()

    # Test 5
    # Demo principalDue function
    print('Test 5')
    run_time.start()
    print('The principal due of this loan is: ', loan1.principalDueRecursive(t))
    run_time.end()
    print()

    # Test 6
    # Demo balanceRecursive function
    print('Test 6')
    run_time.start()
    print('The remaining balance of this loan is: ', loan1.balanceRecursive(t))
    run_time.end()
    print()


    # Comments on run time: Calculations using direct formula takes no time to run at all (0.0 seconds).
    # Calculations using recursive functions takes significantly more time to run. As time period increases,
    
if __name__ == '__main__':
    main()