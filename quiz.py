print("This is a T/F quiz.")
print("For each question, enter 'T' or 'F'")
print("")

# Initialize Variable
questions = ( "True or False, Booleans represent one of two values: True or False", "True or False, The earth if flat", "True or False, There are 53 weeks in a year?", "True or False, Trees get their mass from carbon captured from the air?")
answers = ("T", "F", "F", "T")

q1Correct =q2Correct = q3Correct = q4Correct = False
q1Answer = q2Answer = q3Answer = q4Answer = ""

num_correct = 0

take_again = True
while(take_again == True):

  for x in questions:
    cnt = 0
    print(x)
    user_answer = input(": ")
    invalid = True
    while (invalid):
      if ((user_answer != "T" and user_answer != "F"):
        print("Invalid Entry: For each question, enter 'T' or 'F'")
        user_answer = input(": ")
      else:
        valid = True
    if (answers[cnt] == user_answer):
      cnt = cnt + 1
      num_correct = num_correct + 1
      if (num_correct == 1):
        q1Answer = user_answer
        q1Correct = True
      elif (num_correct == 2):
        q2Answer = user_answer
        q2Correct = True
      elif (num_correct == 3):
        q3Answer = user_answer
        q3Correct = True
      elif (num_correct == 4):
        q4Answer = user_answer
        q4Correct = True

  # Answer Log
  print(f"You answered {num_correct} questions correctly")
  if(q1Correct == False or q2Correct == False or q3Correct == False or q4Correct == False):
    print("Here is what you got wrong:")
    if (q1Correct == False):
      print(f"    Question 1: You answered {question1} Correct Answer {q1Answer}")
    if (q2Correct == False):
      print(f"    Question 2: You answered {question2} Correct Answer {q2Answer}")
    if (q3Correct == False):
      print(f"    Question 3: You answered {question3} Correct Answer {q3Answer}")
    if (q4Correct == False):
      print(f"    Question 4: You answered {question4} Correct Answer {q4Answer}")
    print("")
    print("Would you like to re-take the quiz? (Enter 'Y' or 'N')")
    take_again_str = input(": ")
    if (take_again_str == "Y" or take_again_str == "N"):
        if (take_again_str == "Y"):
          take_again = True
          print("")
        else:
          take_again = False
          print("Thanks for taking the quiz!")
    else:
        print("Invalid Entry: Enter 'Y' or 'N'")
  else:
    print("Thanks for taking the quiz!")
    take_again = False
