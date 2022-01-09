from loan.loan_base import Loan


class FixedRateLoan(Loan):
    def rate(self, period=None):
        # Overrides the base class
        return self._rate

class VariableRateLoan(Loan):

    # Initialize function
    def __init__(self, notional, rateDict, term):
        self._rateDict = rateDict if isinstance(rateDict, dict) else print('Rate is not a dictionary')
        super(VariableRateLoan, self).__init__(notional, None, term)

    def getRate(self, startPeriod):
        self.sorted_key = dict(sorted(self._rateDict.items(), key = lambda k:k[1], reverse = False))
        self.closest_key = min(self.sorted_key.keys(), key = lambda k: abs(k - startPeriod))
        while self.closest_key > startPeriod:
            self.sorted_key.pop(self.closest_key, None)
            self.closest_key = min(self.sorted_key.keys(), key=lambda k: abs(k - startPeriod))
        return self._rateDict[self.closest_key]

    def __repr__(self):
        return str(self._rateDict)