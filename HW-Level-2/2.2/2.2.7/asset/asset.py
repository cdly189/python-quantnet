class Asset(object):
    def __init__(self, initialValue):
        self._initialValue = initialValue

    @property
    def initialValue(self):
        return self._initialValue

    @initialValue.setter
    def initialValue(self, dinitialValue):
        self._initialValue = dinitialValue

    def annualDeprRate(self, period=None):
        raise NotImplementedError

    def monthlyDeprRate(self, period=None):
        return self.annualDeprRate(period) / 12

    # Formula: current value = initial value * [(1-monthlyDeprRate)**t]
    def value(self, t):
        return self._initialValue * ((1 - self.monthlyDeprRate(t)) ** t)


class Car(Asset):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .05

# Derived classes from Car
class Lambourghini(Car):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .20

# Lexus
# Derived from CarMixin and FixedRateLoan
class Lexus(Car):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .08

# Civic
# Derived from CarMixin and FixedRateLoan
class Civic(Car):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .01


##########################################################
# HouseBase
# Derived from Asset
class HouseBase(Asset):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .005

# Derived classes from HouseBase
# PrimaryHome
# Derived from HouseBase
class PrimaryHome(HouseBase):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .007

# VacationHome
# Derived from HouseBase
class VacationHome(HouseBase):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .001