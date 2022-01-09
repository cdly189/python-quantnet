from loan.loan_base import Loan


class FixedRateLoan(Loan):
    def rate(self, period = None):
        return self._rate

class VariableRateLoan(Loan):
    def __init__(self, notional, rateDict, term):
        self._rateDict = rateDict if isinstance(rateDict, dict) else print('Rate is not a dictionary')
        super(VariableRateLoan, self).__init__(notional, None, term)

    def getRate(self, startPeriod = None):
        self.sorted_key = dict(sorted(self._rateDict.items(), key = lambda k:k[1], reverse = False))
        self.closest_key = min(self.sorted_key.keys(), key = lambda k: abs(k - startPeriod))
        while self.closest_key > startPeriod:
            self.sorted_key.pop(self.closest_key, None)
            self.closest_key = min(self.sorted_key.keys(), key=lambda k: abs(k - startPeriod))
        return self._rateDict[self.closest_key]

    def __repr__(self):
        return str(self._rateDict)


class AutoLoan(FixedRateLoan):
    def __init__(self, notional, rate, term, car):
        super(AutoLoan, self).__init__(notional, rate, term)
        self._car = car

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, icar):
        self._car = icar

    def __repr__(self):
        return '$' + str(self._notional) + ' at ' + str(self._rate) + ' per year, for ' + str(self._term) + \
               ' years and car value is $' + str(self._car)