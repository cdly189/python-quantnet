class Loan(object):
    def __init__(self, notional, rate, term):
        # Main attributes
        self._notional = notional
        self._rate = rate
        self._term = term

    @property
    def notional(self):
        return self._notional

    @notional.setter
    def notional(self, inotional):
        self._notional = inotional

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, irate):
        self._rate = irate

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, iterm):
        self._term = iterm

    def monthlyPayment(self, period=None):
        return self.calcMonthlyPmt(self._notional, self.getRate(period), self._term)

    def totalPayments(self):
        return self.monthlyPayment() * self._term * 12

    def totalInterest(self):
        return self.totalPayments() - self._notional

    def interestDue(self, t):
        # Calculate payment using the formula interestDue = r * loan balance bal
        # r = monthly rate, P = notional value, N = term in months
        return Loan.monthlyRate(self.getRate(t)) * self.balance(t - 1)

    def principalDue(self, t):
        # Calculate payment using the formula principalDue = monthlyPayment - interestDue
        # r = monthly rate, P = notional value, N = term in months
        return self.monthlyPayment() - self.interestDue(t)

    def balance(self, t):
        # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r = monthly rate, P = notional value, N = term in months
        return self.calcBalance(self._notional, self.getRate(t), self._term, t)

    # This method use the recursive function
    def interestDueRecursive(self, t):
        if t == 1:
            return self._notional * Loan.monthlyRate(self.getRate(t))
        else:
            return self.balanceRecursive(t - 1) * Loan.monthlyRate(self.getRate(t))

    def principalDueRecursive(self, t):
        # Calculate payment using recursive functions
        return self.monthlyPayment() - self.interestDueRecursive(t)

    def balanceRecursive(self, t):
        # Calculate payment using recursive functions
        if t == 1:
            return self._notional - self.principalDueRecursive(t)
        else:
            return self.balanceRecursive(t - 1) - self.principalDueRecursive(t)

    def getRate(self, period=None):
        return self._rate

    @classmethod
    def calcMonthlyPmt(cls, face, rate, term):
        return (Loan.monthlyRate(rate) * face * (1 + Loan.monthlyRate(rate)) ** (term * 12)) / \
               (((1 + Loan.monthlyRate(rate)) ** (term * 12)) - 1)

    # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcBalance(cls, face, rate, term, period):
        return face * ((1 + Loan.monthlyRate(rate)) ** period) - \
               (Loan.calcMonthlyPmt(face, rate, term) * (((1 + Loan.monthlyRate(rate)) ** period - 1) /
                                                         Loan.monthlyRate(rate)))

    @staticmethod
    def monthlyRate(annualRate):
        return annualRate / 12

    @staticmethod
    def annualRate(monthlyRate):
        return monthlyRate * 12
