"""
A Loan class that contain functions such as monthly payment, total payment and total interest
"""

class Loan(object):
    def __init__(self,notional,rate,term):
        self._notional = notional
        self._rate = rate
        self._term = term

    # Add getter/setter function
    @property
    def notional(self):
        return self._notional

    @notional.setter
    def notional(self,inotional):
        self._notional = inotional

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self,irate):
        self._rate = irate

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self,iterm):
        self._term = iterm

    def monthlyPayment(self,period=None):
        # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
        # r = monthly rate, P = notional value, N = term in months
        return ((self._rate / 12) * self._notional * (1 + (self._rate / 12)) ** (self._term * 12)) \
               / (((1 + (self._rate / 12)) ** (self._term * 12)) - 1)

    def totalPayments(self):
        # Calculate total payment using the formula total = monthlyPayment * term * 12
        # r = monthly rate, P = notional value, N = term in months
        return self.monthlyPayment() * self._term * 12

    def totalInterest(self):
        # Calculate payment using the formula total_interest = totalpayment - notional value
        return self.totalPayments() - self._notional

    def balance(self,t):
        # Calculate payment using the formula bal = P*(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r = monthly rate, P = notional value, N = term in months
        return self._notional * ((1 + self._rate / 12) ** t) - \
               (self.monthlyPayment() * (((1 + (self._rate / 12)) ** t - 1) / (self._rate / 12)))

    def interestDue(self,t):
        # Calculate payment using the formula interestDue = r * loan balance bal
        # r = monthly rate, P = notional value, N = term in months
        return (self._rate / 12) * self.balance(t - 1)

    def principalDue(self, t):
        # Calculate payment using the formula principalDue = monthlyPayment - interestDue
        # r = monthly rate, P = notional value, N = term in months
        return self.monthlyPayment() - self.interestDue(t)

    # This method use the recursive function
    def interestDueRecursive(self, t):
        # Calculate payment using recursive functions
        if t == 1:
            return self._notional * (self._rate / 12)
        else:
            return self.balanceRecursive(t - 1) * (self._rate / 12)

    # Instance method to calculate principal due at time t
    # This method use the recursive function
    def principalDueRecursive(self, t):
        # Calculate payment using recursive functions
        return self.monthlyPayment() - self.interestDueRecursive(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the recursive function
    def balanceRecursive(self, t):
        # Calculate payment using recursive functions
        if t == 1:
            return self._notional - self.principalDueRecursive(t)
        else:
            return self.balanceRecursive(t-1) - self.principalDueRecursive(t)

