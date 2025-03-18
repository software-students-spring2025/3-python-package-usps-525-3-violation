import random
import time

def coin():
    val = random.random()
    if val > 0.5:
        return "heads!"
    else:
        return "tails!"
    
def math_ans(op, num1, num2):
   if op == 1:
      return num1 + num2
   elif op == 2:
      return num1 - num2
   elif op == 3:
      return num1 * num2
   else:
      return num1
    
def play_math(level, num_questions):
   low_num = 1
   level = level.lower()
   num_correct = 0
   if level == "easy":
      high_num = 10
   elif level == "medium":
      high_num = 20
   elif level == "hard":
      high_num = 50
   else:
      print("Please enter a valid difficulty")
      return
   
   start_time = time.time()
   for i in range(num_questions):
      #1: +, 2: -, 3: *, 4: /
      num1 = random.randint(low_num, high_num)
      num2 = random.randint(low_num, high_num)

      if num1 < num2:
         #make sure num1 is not smaller than num2
         temp = num1
         num1 = num2
         num2 = temp
      
      op_num = random.randint(1,4)
      ops = "+-*/"
      correct = math_ans(op_num, num1, num2)
      if op_num == 4:
         num1 = num1 * num2

      print(f"{num1} {ops[op_num-1]} {num2} = ")
      ans = int(input("Input your answer: "))
      if ans == correct:
         num_correct += 1
         print("Correct!")
      else:
         print(f"Incorrect. The correct answer was {correct}")
   end_time = time.time()
   elapsed_time = end_time - start_time
   print(f"Well done! {num_correct}/{num_questions} Correct")
   print(f"Elapsed time: {elapsed_time:.1f} seconds")
   return num_correct


def play_geo():
   pass


def play_vocab(level, type, num_questions):
   wordbank = {
   "easy": [
      ("Love", "Like", "Hate"),
      ("Happy", "Joyful", "Sad"),
      ("Fast", "Quick", "Slow"),
      ("Big", "Large", "Small"),
      ("Easy", "Simple", "Difficult"),
      ("Loud", "Noisy", "Quiet"),
      ("Hot", "Warm", "Cold"),
      ("Dark", "Dim", "Bright"),
      ("Strong", "Powerful", "Weak"),
      ("Clean", "Tidy", "Messy"),
      ("Friendly", "Kind", "Mean"),
      ("Soft", "Gentle", "Rough"),
      ("Smart", "Clever", "Dumb"),
      ("Fun", "Enjoyable", "Boring"),
      ("Shout", "Yell", "Whisper"),
      ("Wet", "Damp", "Dry"),
      ("Brave", "Courageous", "Fearful"),
      ("Thin", "Slim", "Thick"),
      ("New", "Fresh", "Old"),
      ("Safe", "Secure", "Dangerous")
   ],
   "medium": [
      ("Muted", "Faint", "Blaring"),
      ("Strong", "Robust", "Weak"),
      ("Bright", "Radiant", "Dim"),
      ("Lazy", "Idle", "Energetic"),
      ("Sharp", "Pointed", "Dull"),
      ("Brisk", "Lively", "Sluggish"),
      ("Famous", "Renowned", "Obscure"),
      ("Shy", "Timid", "Bold"),
      ("Smooth", "Even", "Rough"),
      ("Lucky", "Fortunate", "Hapless"),
      ("Heavy", "Weighty", "Light"),
      ("Neat", "Orderly", "Messy"),
      ("Curious", "Inquisitive", "Indifferent"),
      ("Deep", "Profound", "Shallow"),
      ("Proud", "Confident", "Ashamed"),
      ("Polite", "Courteous", "Rude"),
      ("Brilliant", "Intelligent", "Foolish"),
      ("Chilly", "Cool", "Warm"),
      ("Tough", "Sturdy", "Fragile"),
      ("Eager", "Keen", "Reluctant")
   ],
   "hard": [
      ("Precise", "Exact", "Vague"),
      ("Maelstrom", "Turmoil", "Tranquil"),
      ("Tedious", "Boring", "Exciting"),
      ("Eloquent", "Articulate", "Incoherent"),
      ("Diligent", "Industrious", "Indolent"),
      ("Frugal", "Thrifty", "Wasteful"),
      ("Arrogant", "Haughty", "Humble"),
      ("Elucidate", "Clarify", "Obfuscate"),
      ("Complex", "Complicated", "Simple"),
      ("Exultant", "Jubilant", "Melancholic"),
      ("Elusive", "Evasive", "Obvious"),
      ("Ostentatious", "Flamboyant", "Modest"),
      ("Meticulous", "Punctilious", "Negligent"),
      ("Gregarious", "Sociable", "Introverted"),
      ("Impartial", "Nonpartisan", "Prejudiced"),
      ("Fickle", "Inconsistent", "Reliable"),
      ("Clandestine", "Secret", "Overt"),
      ("Phlegmatic", "Placid", "Temperamental"),
      ("Lethargic", "Sluggish", "Energetic"),
      ("Amicable", "Cordial", "Hostile")
   ]
   }


   for i in range(max(min(int(num_questions), 15), 0)):
      word = random.choice(wordbank[level])
      wordbank[level].remove(word)
      type_names = ["synonym", "antonym"]
      if type == "synonyms":
         correct = word[1]
         type_name = type_names[0]
      elif type == "antyonyms":
         correct = word[2]
         type_name = type_names[1]
      elif type == "both":
         type_num = random.randint(0, 1)
         correct = word[type_num + 1]
         type_name = type_names[type_num]
      else:
         return


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


      print(f"Which word is a {type_name} for {word[0]}?")
      print(f"A: {options[0]}")
      print(f"B: {options[1]}")
      print(f"C: {options[2]}")
      print(f"D: {options[3]}")
      ans = input("Choose A, B, C, or D: ").upper()
      while ans not in key:
         ans = input("Invalid option. Choose A, B, C, or D: ").upper()


      if key[ans] == correct:
         print("Correct!")
      else:
         print(f"Incorrect. The correct answer was {correct}")
      print()
   pass


def play_science():
   pass