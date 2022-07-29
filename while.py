print("Here is a guessing game. You get 3 tries.")

tries = 0
while tries <= 3:
  print("What is the name of the computer that played on Jeopardy?")
  answer = input()
  tries = tries + 1
  if answer == 'Waston':
    print("That is right!")
    break
  elif tries == 3:
    print("Sorry. No more guesses. The answer is Waston.")
    break
  else:
    print("Sorry. Guess again.")



# print("Here is a guessing game. You get three tries.")
# print("What is the name of the computer that played on Jeopardy?")
# response = input()
# answer = "happy"
# if response == answer:
#   print("That is right!")
# else:
#   print("Sorry. Guess again:")
#   response = input()
#   if response == answer:
#     print("That is right!")
#   else:
#     print("Sorry, One more guess:")
#     response = input()
#     if response == answer:
#       print("That is right!")
#     else:
#       print("Sorry. No more guesses. The answer is happy.")

