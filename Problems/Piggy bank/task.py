class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

    def _cents_to_dollars(self):
        quotient = self.cents // 100
        remainder = self.cents % 100
        if self.cents >= 100:
            self.dollars += quotient
            self.cents = remainder

    def add_money(self, deposit_dollars: int, deposit_cents: int):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        self._cents_to_dollars()
