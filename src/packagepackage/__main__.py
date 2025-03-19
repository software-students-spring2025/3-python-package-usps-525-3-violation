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

   game_select = int(game_select)
   print()

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
      print("Which difficulty would you like to play?")
      level = input("Press 1 for easy, 2 for medium, and 3 for hard: ")
      level_select = {"1":"easy", "2":"medium", "3":"hard"}
      while level not in level_select.keys():
         print("Invalid input, please select an integer from 1 through 3.")
         level = input("Press 1 for easy, 2 for medium, and 3 for hard: ")
      
      print("Which gamemode would you like to play?")
      mode = input("Press 1 for synonyms only, 2 for antonyms only, and 3 for both synonyms and antonyms: ")
      mode_select = {"1":"synonyms", "2":"antonyms", "3":"both"}
      while mode not in mode_select.keys():
         print("Invalid input, please select an integer from 1 through 3.")
         mode = input("Press 1 for synonyms only, 2 for antonyms only, and 3 for both synonyms and antonyms: ")

      print("How many questions would you like to answer?")
      num_questions = input("Please enter an integer between 1 to 15 (inclusive): ")
      while num_questions not in [str(i) for i in range(1, 16)]:
         num_questions = input("Invalid input. Please enter an integer between 1 to 15 (inclusive): ")

      package.play_vocab(level_select[level], mode_select[mode], int(num_questions))
      
   elif game_select == 3:
      pass
   elif game_select == 4:
      pass
   elif game_select == 5:
      return 


if __name__ == "__main__":
    # run the main function
    main()