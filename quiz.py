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
num_correct = 0
q1Correct =q2Correct = q3Correct = q4Correct = False
question1 = question2 = question3 = question4 = ""

take_again = True
while(take_again == True):
  # Question 1
  answered = False
  q1Answer = "T"
  print("Question 1")
  while(answered == False):
    print("True or False, Booleans represent one of two values: True or False")
    question1 = input(": ")
    # Check for correct answer
    if (question1 == "T" or question1 == "t"):
        num_correct = num_correct + 1
        q1Correct = True
    if(question1 == "T" or question1 == "F" or question1 == "t" or question1 == "f"):
      answered = True
    else:
      print("Invalid Entry: For each question, enter 'T' or 'F'")
      print("")
  print("")
  
  # Question 2
  answered = False
  q2Answer = "F"
  print("Question 2")
  while(answered == False):
    print("True or False, The earth if flat")
    question2 = input(": ")
    # Check for correct answer
    if (question2 == "F" or question2 == "f"):
        num_correct = num_correct + 1
        q2Correct = True
    if(question2 == "T" or question2 == "F" or question2 == "t" or question2 == "f"):
      answered = True
    else:
      print("Invalid Entry: For each question, enter 'T' or 'F'")
      print("")
  print("")
  
  # Question 3
  answered = False
  q3Answer = "F"
  print("Question 3")
  while(answered == False):
    print("True or False, There are 53 weeks in a year?")
    question3 = input(": ")
    # Check for correct answer
    if (question3 == "F" or question3 == "f"):
        num_correct = num_correct + 1
        q3Correct = True
    if(question3 == "T" or question3 == "F" or question3 == "t" or question3 == "f"):
      answered = True
    else:
      print("Invalid Entry: For each question, enter 'T' or 'F'")
      print("")
  print("")
  answered = False
  
  # Question 4
  answered = False
  q4Answer = "T"
  print("Question 4")
  while(answered == False):
    print("True or False, Trees get their mass from carbon captured from the air?")
    question4 = input(": ")
    if (question4 == "T" or question4 == "t"):
        num_correct = num_correct + 1
        q4Correct = True
    if(question4 == "T" or question4 == "F" or question4 == "t" or question4 == "f"):
      answered = True
    else:
      print("Invalid Entry: For each question, enter 'T' or 'F'")
      print("")
  print("")
  answered = False
  
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


