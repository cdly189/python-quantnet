from loan.loan_base import Loan

# Derived classes from Loan:
# FixedRateLoan
class FixedRateLoan(Loan):
    def rate(self, period = None):
        # Overrides the base class
        return self._rate

class VariableRateLoan(Loan):
    def __init__(self, notional, rateDict, term):  # overide the init function in the base class
        self._rateDict = rateDict if isinstance(rateDict, dict) else print('Rate is not a dictionary')
        super(VariableRateLoan, self).__init__(notional, None, term)  # invoke initialization the base class

    # Derived instance method to find the rate of a given period
    # rateDict contains startPeriod as key and rate as value for each rate
    # Methodology:
    #   1. Create a new temporary dict that sort the key (period) by values
    #   2. Of this new temp dict:
    #       a. Find the key that is closest to the passed-in period
    #       b. Compare this key with the passed-in period, if the passed-in value is smaller,
    #           remove the key from the temp dict
    #       c. Find the new closest key based on the new dict.
    #       d. Continue loop until said key is found.
    #   3. Return the corresponded key value (interest rate) of the newly founded closest key. This is the interest
    #       rate we are looking for.
    def getRate(self, startPeriod = None):
        self.sorted_key = dict(sorted(self._rateDict.items(), key = lambda k:k[1], reverse = False))
        self.closest_key = min(self.sorted_key.keys(), key = lambda k: abs(k - startPeriod))
        while self.closest_key > startPeriod:
            self.sorted_key.pop(self.closest_key, None)
            self.closest_key = min(self.sorted_key.keys(), key=lambda k: abs(k - startPeriod))
        return self._rateDict[self.closest_key]

    # Return the repr value of the whole rateDict
    def __repr__(self):
        return str(self._rateDict)