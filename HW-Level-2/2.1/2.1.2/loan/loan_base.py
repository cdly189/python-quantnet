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


