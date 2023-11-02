# TITLE
print("QQQQQQQQQQQ       U         U  IIIIIIIIIII   ZZZZZZZZZZZ        TTTTTTTTTT  TTTTTTTTTTTT  M   MM    MM     EEEEEEEEEEE  !!  !!")
print("Q         Q       U         U       I                Z                T          T        M  M  M  M   M   E            !!  !!")
print("Q         Q       U         U       I               Z                 T          T        MM      M     M  E            !!  !!")    
print("Q         Q       U         U       I              Z                  T          T        M             M  E            !!  !!")   
print("Q         Q       U         U       I             Z                   T          T        M             M  E            !!  !!")
print("Q         Q       U         U       I            Z     ASCMI-ART™     T          T        M             M  EEEEEEEEEEE  !!  !!")
print("Q         Q       U         U       I           Z                     T          T        M             M  E            !!  !!")    
print("Q         Q       U         U       I          Z                      T          T        M             M  E            !!  !!")  
print("Q         Q       U         U       I         Z                       T          T        M             M  E            !!  !!")
print("QQQQQQQQQQQ   Q   UU       UU       I        Z                        T          T        M             M  E                  ")
print("         QQ Q Q     UUUUUUU    IIIIIIIIIII   ZZZZZZZZZZZ              T     TTTTTTTTTTT   M             M  EEEEEEEEEEE  !!  !!")
print("")

print("This is a T/F quiz.")
print("For each question, enter 'T' or 'F'")
print("")

# Initialize Variable
questions = ( "True or False, Booleans represent one of two values: True or False", "True or False, The earth is flat", "True or False, There are 53 weeks in a year?", "True or False, Trees get their mass from carbon captured from the air?")
answers = ("T", "F", "F", "T")

q1Correct =q2Correct = q3Correct = q4Correct = False
q1Answer = q2Answer = q3Answer = q4Answer = ""

num_correct = 0

take_again = True
while(take_again == True):

  index = 0
  for x in questions:
    # Print question
    print(x)
    # Input user answer
    user_answer = input(": ")
    print("")
    invalid = True
    # Check for T or F input
    while (invalid):
      if (user_answer == "T" or user_answer == "F"):
        invalid = False
      else:
        print("Invalid Entry: For each question, enter 'T' or 'F'")
        user_answer = input(": ")
    # Answered Correctly
    if (user_answer == answers[index]):
      index = index + 1
      num_correct = num_correct + 1
      if (index == 1):
        q1Correct = True
        q1Answer = user_answer
      if (index == 2):
        q2Correct = True
        q2Answer = user_answer
      if (index == 3):
        q3Correct = True
        q3Answer = user_answer
      else:
        q4Correct = True
        q4Answer = user_answer
    # Answered Incorrectly
    else:
      index = index + 1
      if (index == 1):
        q1Answer = user_answer
      if (index == 2):
        q2Answer = user_answer
      if (index == 3):
        q3Answer = user_answer
      else:
        q4Answer = user_answer

  # Answer Log
  print(f"You answered {num_correct} questions correctly")
  if(q1Correct == False or q2Correct == False or q3Correct == False or q4Correct == False):
    print("Here is what you got wrong:")
    if (q1Correct == False):
      print(f"    Question 1: You answered {q1Answer} Correct Answer {answers[0]}")
    if (q2Correct == False):
      print(f"    Question 2: You answered {q2Answer} Correct Answer {answers[1]}")
    if (q3Correct == False):
      print(f"    Question 3: You answered {q3Answer} Correct Answer {answers[2]}")
    if (q4Correct == False):
      print(f"    Question 4: You answered {q4Answer} Correct Answer {answers[3]}")
    print("")
    print("Would you like to re-take the quiz? (Enter 'Y' or 'N')")

    # Input user answer
    take_again_str = input(": ")
    print("")
    invalid = True
    # Check for T or F input
    while (invalid):
      if (take_again_str == "Y" or take_again_str == "N"):
        invalid = False
        if (take_again_str == "Y"):
          take_again = True
        else:
          take_again = False
      else:
        print("Invalid Entry:  enter 'Y' or 'N'")
        take_again_str = input(": ")
  else:
    print("Thanks for taking the quiz!")
    take_again = False
