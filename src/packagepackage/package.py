import random

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
   questions = {
      1: "What is the largest planet in our solar system?",
      2: "What is the fastest animal on land?"
   }
   
   options = {
      1: ["Mars", "Saturn", "Jupiter", "Ceres"],
      2: ["Cheetah", "Falcon", "Antelope", "Usain Bolt"]
   }
   
   answers = {
      1: "Jupiter",
      2: "Cheetah"
   }
   
   selected_keys = random.sample(list(questions.keys()), 2)
   selected_questions = {key: questions[key] for key in selected_keys}
   selected_options = {key: options[key] for key in selected_keys}
   selected_answers = {key: answers[key] for key in selected_keys}
   
   correct = 0
   total = 0
   
   for i in selected_keys:
      
      option_map = {
         'A': selected_options[i][0],
         'B': selected_options[i][1],
         'C': selected_options[i][2],
         'D': selected_options[i][3]
      }
      
      print(selected_questions[i])
      print(f"A: {option_map["A"]}")
      print(f"B: {option_map["B"]}")
      print(f"C: {option_map["C"]}")
      print(f"D: {option_map["D"]}")
      
      ans = input("Please enter A, B, C, or D: ").upper()
      
      while ans not in option_map:
         print("Invalid input. Please enter A, B, C, or D.")
      
      if option_map[ans] == selected_answers[i]:
         print("Correct!")
         correct += 1
      else:
         print(f"Incorrect! The correct answer was {selected_answers[i]}.")
      print()
      total += 1
      
   if correct / total == 1:
      result = "Perfect!"
   elif correct / total >= 0.8:
      result = "Great!"
   elif correct / total >= 0.6:
      result = "Not bad!"
   elif correct / total >= 0.4:
      result = "Good effort."
   elif correct / total >= 0:
      result = "You need to study more!"
      
   print(f"{result} Your score was {correct}/{total}.")