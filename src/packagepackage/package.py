import random
from packagepackage.wordbank import wordbank as original_wordbank
import copy


def coin():
    val = random.random()
    if val > 0.5:
        return "heads!"
    else:
        return "tails!"
    
def play_math():
   pass


def play_geo():
   pass


def play_vocab(level, mode, num_questions):
   wordbank = copy.deepcopy(original_wordbank)
   if level not in ['easy', 'medium', 'hard']:
      raise ValueError("Invalid difficulty. Please choose from easy, medium, or difficult")
   if mode not in ['synonyms', 'antonyms', 'both']:
      raise ValueError("Invalid gamemode. Please choose from synonyms, antonyms, or both")
   if not isinstance(num_questions, int) or num_questions != max(min(int(num_questions), 15), 1):
      raise ValueError("Invalid number of questions. Please enter an integer between 1 and 15")

   score = 0

   for i in range(num_questions):
      word = random.choice(wordbank[level])
      wordbank[level].remove(word)
      mode_names = [" synonym", "n antonym"]
      if mode == "synonyms":
         correct = word[1]
         mode_name = mode_names[0]
      elif mode == "antonyms":
         correct = word[2]
         mode_name = mode_names[1]
      elif mode == "both":
         mode_num = random.randint(0, 1)
         correct = word[mode_num + 1]
         mode_name = mode_names[mode_num]


      options = {correct}
      while len(options) < 4:
         options.add(random.choice(wordbank[level])[random.randint(0, 2)])
      options = list(options)
      random.shuffle(options)


      key = {
         "A": options[0],
         "B": options[1],
         "C": options[2],
         "D": options[3]
      }


      print(f"Which word is a{mode_name} for {word[0]}?")
      print(f"A: {options[0]}")
      print(f"B: {options[1]}")
      print(f"C: {options[2]}")
      print(f"D: {options[3]}")
      ans = input("Choose A, B, C, or D: ").upper()
      while ans not in key:
         ans = input("Invalid option. Choose A, B, C, or D: ").upper()


      if key[ans] == correct:
         print("Correct!")
         score += 1
      else:
         print(f"Incorrect. The correct answer was {correct}")
      print()
   
   print(f"Your total score this game was {score}/{num_questions}: {int(score*100/num_questions)}%")

def play_science():
   pass