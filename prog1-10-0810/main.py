def calculate_percentages(self, starting_balance):
    interest_rate = 0.005 # 0.5%
    return starting_balance * interest_rate
customer = Customer()
starting_balance = 1000
percentages = customer.calculate_percentages(starting_balance)
print(percentages) # 5
