class Budget:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance = amount
        return f"Deposit successful, your current balance in {self.name} budget is ${self.balance}"

    def withdrawal(self, amount):
        if self.balance < amount:
            return "insufficient funds"
        else:
            self.balance -= amount
            return f"Transaction successful, \n"\
                   f"your current balance in {self.name} budget is ${self.balance}"

    def check_balance(self):
        balance = f"your current balance in {self.name} budget is ${self.balance}"
        return balance

    def transfer(self, amount, section):
        if self.name == section.name:
            return "Error!, you cannot transfer from a section into the same section.\n" \
                   " You can only transfer from one section to another"

        elif self.balance < amount:
            return "insufficient funds"
        else:
            self.balance -= amount
            return f"Transaction successful, \n"\
                   f"your current balance in {self.name} budget is ${self.balance}"


food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")

print(food.check_balance())
print(clothing.check_balance())
print(entertainment.check_balance())

print(food.deposit(5000))
print(clothing.deposit(10000))
print(entertainment.deposit(8000))

print(food.withdrawal(2000))
print(clothing.withdrawal(4000))
print(entertainment.withdrawal(1500))

print(clothing.transfer(500, food))
print(clothing.transfer(1000, clothing))
print(food.transfer(1500, entertainment))
