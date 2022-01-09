from loan.loanpool import LoanPool
from loan.loan_base import Loan
#######################


def main():
    loan1 = Loan(100000, .050, 30)
    loan2 = Loan(100000, .050, 30)
    loan3 = Loan(100000, .050, 30)
    loan4 = Loan(100000, .050, 30)
    loans = [loan1, loan2, loan3, loan4]
    loanpool1 = LoanPool(loans)

    print('Test 1')
    print('The total loan principal is: ', loanpool1.totalPrincipal())
    print()

    print('Test 2')
    print('The total loan balance is: ', loanpool1.totalPayments(26))
    print()

    print('Test 3')
    print('The aggregate loan payment due is: ', loanpool1.paymentDue(26))
    print()

    print('Test 4')
    print('The aggregate interest due is: ', loanpool1.totalInterest(26))
    print()

    print('Test 5')
    print('The aggregate principal due is: ', loanpool1.principalDue(26))
    print()

    print('Test 6')
    print('The number of active loans is: ', loanpool1.activeLoanCount(26))
    print()

    print('Test 7')
    print('The Weighted Average Maturity is: ', loanpool1.WAM())
    print()

    print('Test 8')
    print('The Weighted Average Maturity is: ', loanpool1.WAR())
    print()


if __name__ == '__main__':
    main()