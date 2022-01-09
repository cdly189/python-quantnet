from loan.loans import AutoLoan, FixedRateLoan


def main():
    autoloan1 = AutoLoan(100000, .050, 30, 100000)
    print('Test block 1: AutoLoan')
    print('The auto loan term is: ', autoloan1.__repr__())
    print('The auto loan rate is: ', autoloan1.rate())
    print()


if __name__ == '__main__':
    main()