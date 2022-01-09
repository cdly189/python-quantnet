from loan.loan_base import Loan


class LoanPool(object):
    def __init__(self, loans=None):
        self._loans = loans
        self._loan = [loan for loan in self._loans]
        self._notional = [loan.notional for loan in self._loans]
        self._rate = [loan.rate for loan in self._loans]
        self._term = [loan.term for loan in self._loans]

    @property
    def loans(self):
        return self._loans

    @loans.setter
    def loans(self, iloans):
        self._loans = iloans

    def unpackNotionals(self):
        return [loan.notional for loan in self._loans]

    def unpackRates(self):
        return [loan.rate for loan in self._loans]

    def unpackTerms(self):
        return [loan.term for loan in self._loans]

    def totalPayments(self, t=0):
        return sum([loan.balance(t) for loan in self._loans])

    def totalPrincipal(self):
        return sum(self._notional)

    def paymentDue(self, t=0):
        return sum([loan.monthlyPayment(t) for loan in self._loans])

    def totalInterest(self, t=0):
        return sum([loan.interestDue(t) for loan in self._loans])

    def principalDue(self, t=0):
        return self.paymentDue(t) - self.totalInterest(t)

    def activeLoanCount(self, t):
        count = 0
        for loan in self._loans:
            if loan.balance(t) > 0:
                count += 1
        return count

    def WAM(self):
        sum_amount = self.totalPrincipal()
        WAM_rate = 0
        for loan in self._loans:
            WAM_rate += loan.notional * loan.term / sum_amount
        return WAM_rate

    def WAR(self):
        sum_amount = self.totalPrincipal()
        WAR_rate = 0
        for loan in self._loans:
            WAR_rate += loan.notional * loan.rate / sum_amount
        return WAR_rate