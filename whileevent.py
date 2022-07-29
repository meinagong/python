total = 0
count = 0
average = 0.0

print("Enter a grade (-1 to quit)")
grade = int(input())

while grade != -1:
  total = total + grade
  count = count + 1
  print("Enter a grade (-1 to quit)")
  grade = int(input())

average = total / count
print("The average is: " + str(average))
