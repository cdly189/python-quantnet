from loan.loan_base import Loan


def main():
    mortgage1 = Loan(10000, 0.04, 360)
    print(mortgage1.monthlyPayment())
    print(mortgage1.totalPayments())
    print(mortgage1.totalInterest())


if __name__ == '__main__':
    main()