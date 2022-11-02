class InvalidWithdrawl(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance

# raise InvalidWithdrawl(25,50)

try:
    raise InvalidWithdrawl(25,50)
except InvalidWithdrawl as e:
    print("I'm sorry, but you withdrawl is more than your balance"
            "${}".format(e.overage()))