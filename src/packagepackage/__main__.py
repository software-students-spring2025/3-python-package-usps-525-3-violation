"""
FROM EXAMPLE PACKAGE:
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

import packagepackage.package as package

def main():
   print("Welcome! Which game would you like to play?")
   print("Press 1 to play math game")
   print("Press 2 to play vocab game")
   print("Press 3 to play geography game")
   print("Press 4 to play science game")
   print("Press 5 to exit")
   game_select = input("Input a number: ")
   while game_select not in [str(i) for i in range(1, 6)]:
      game_select = input("Invalid input, please select an integer from 1 through 5: ")
   if game_select == 1:
      print("Which difficulty would you like to play?")
      print("Press 1 for easy, 2 for medium, and 3 for hard")
      difficulty = input("Input a number: ")
      while difficulty not in [str(i) for i in range(1, 4)]:
         difficulty = input("Invalid input, please select an integer from 1 through 3: ")
      num_select = {1:"easy", 2:"medium", 3:"hard"}
      print("Now choose how many questions you would like: ")
      while True:
        num_qs = input("Input a number: ")
        try:
            num = int(num_qs)
            print("You entered:", num)
            break  
        except ValueError:
            print("That's not a valid integer. Please try again.")
      package.play_math(num_select[difficulty], num_qs)
   elif game_select == 2:
      package.play_vocab('hard', 'both', 5)
   elif game_select == 3:
      pass
   elif game_select == 4:
      pass
   elif game_select == 5:
      return 


if __name__ == "__main__":
    # run the main function
    main()