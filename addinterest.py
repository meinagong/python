# addinterest3.py

def addInterest(balances, rate):
  for i in range(len(balances)):
    balances[i] = balances[i] * (1+rate)

def test():
  amounts = [1000, 2200, 800, 360]
  print(amounts)
  rate = 0.05
  addInterest(amounts, rate)
  print(amounts)

test()

# addinterest2.py

# def addInterest(balance, rate):
#   newBalance = balance * (1+rate)
#   return newBalance

# def test():
#   amount = 1000
#   rate = 0.05
#   amount = addInterest(amount, rate)
#   print(amount)

# test()





# addinterest1.py

# def addInterest(balance, rate):
#   newBalance = balance * (1+rate)
#   balance = newBalance

# def test():
#   amount = 1000
#   rate = 0.05
#   addInterest(amount, rate)
#   print(amount)

# test()