class Asset(object):
    def __init__(self,initialValue):
        self._initialValue = initialValue

    @property
    def initialValue(self):
        return self._initialValue

    @initialValue.setter
    def initialValue(self,dinitialValue):
        self._initialValue = dinitialValue

    def annualDepr(self):
        return .10

    def monthlyDepr(self):
        return self.annualDepr() / 12

    def value(self,t):
        return self._initialValue * ((1 - self.monthlyDepr())**t)

