class Car:
    def __init__(self, gas_level):
        self.gas_level = gas_level

    def add_gas(self, fl):
        return self.gas_level + fl

    def fill_up(self):
        if self.gas_level < 13.0:
            gas_left = self.gas_level - 13.0
            self.add_gas(gas_left)
        else:
            return 0