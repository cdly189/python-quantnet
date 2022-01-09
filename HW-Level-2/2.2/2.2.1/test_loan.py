from loan.loans import FixedRateLoan, VariableRateLoan
from loan.loan_base import Loan
#######################


def main():
    loan1 = FixedRateLoan(100000, .050, 30)
    print('Test 1')
    print('The Fixed Rate is:', loan1.rate())
    print()

    # 2. Testing VariableRateLoan
    # Scenario: Assign a child VariableRateLoan (child of Loan) variable.
    #   In this case, the rate is a dict.
    # Desire result: Print correct result as assigned
    loan2 = VariableRateLoan(100000, {0: .1, 5: .08, 9: .07, 15: .05, 28: .015, 30: .01}, 30)
    print('Test 2')
    print('The Variable Rate is:', loan2.__repr__())
    print()

    #   In this case, the passed-in rate of loan2 is not a dict
    print('Test 3')
    loan2 = VariableRateLoan(100000, .050, 30)
    loan2.getRate()
    print()

    loan2 = VariableRateLoan(100000, {0: .1, 5: .08, 9: .07, 15: .05, 28: .015, 30: .01}, 30)
    print('The Variable Rate is: ', loan2.getRate(26))


if __name__ == '__main__':
    main()