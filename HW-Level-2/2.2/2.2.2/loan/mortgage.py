from loan.loan_base import Loan
from loan.loan_base import Loan

class MortgageMixin(object):
    def __init__(self, notional, rate, term, home):
        super(MortgageMixin, self).__init__(notional, rate, term)
        self._home = home

    @property
    def home(self):
        return self._home


    @home.setter
    def home(self, ihome):
        self._home = ihome

    def PMI(self):
        return .000075 * self._notional if (self._notional / self._home) > .8 else 0

    def monthlyPayment(self, period=None):
        return super(MortgageMixin, self).monthlyPayment(period) + self.PMI()

    def principalDue(self, t):
        return self.monthlyPayment() - super(MortgageMixin, self).interestDue(t)