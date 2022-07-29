numer = 0
denom = 0
while denom != -1:
  print("Enter a numerator: ")
  numer = float(input())
  print("Enter a denominator: ")
  denom = float(input())
  if denom == 0:
    continue
  print(numer / denom)


