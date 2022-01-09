from loan.loan_base import Loan
from loan.loans import FixedRateLoan, VariableRateLoan


class MortgageMixin(object):
    def __init__(self, notional, rate, term, home):
        super(MortgageMixin, self).__init__(notional, rate, term)  # invoke init function if there is a base class
        self._home = home

    @property
    def home(self):
        return self._home

    @home.setter
    def home(self, ihome):
        self._home = ihome

    def __repr__(self):
        return '$' + str(self._notional) + ' at ' + str(self._rate) + ' per year, for ' + str(self._term) + \
               ' years and home value is $' + str(self._home)

    def PMI(self, period = None):
        return .000075 * self._notional if (self._notional / self._home) > .8 else 0

    def monthlyPayment(self, period=None):
        return super(MortgageMixin, self).monthlyPayment(period) + self.PMI(period)

    def principalDue(self, period):
        return self.monthlyPayment(period) - super(MortgageMixin, self).interestDue(period)


class FixedMortgage(MortgageMixin, FixedRateLoan):
    pass


class VariableMortgage(MortgageMixin, VariableRateLoan):
    pass