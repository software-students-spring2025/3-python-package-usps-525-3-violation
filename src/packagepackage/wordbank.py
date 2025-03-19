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
      ("Sturdy", "Robust", "Frail"),
      ("Vivid", "Radiant", "Subdued"),
      ("Lazy", "Idle", "Energetic"),
      ("Sharp", "Pointed", "Dull"),
      ("Brisk", "Lively", "Sluggish"),
      ("Famous", "Renowned", "Obscure"),
      ("Shy", "Timid", "Bold"),
      ("Smooth", "Even", "Bumpy"),
      ("Lucky", "Fortunate", "Hapless"),
      ("Heavy", "Weighty", "Light"),
      ("Precise", "Exact", "Vague"),
      ("Curious", "Inquisitive", "Indifferent"),
      ("Deep", "Profound", "Shallow"),
      ("Proud", "Confident", "Ashamed"),
      ("Polite", "Courteous", "Rude"),
      ("Astute", "Intelligent", "Foolish"),
      ("Precise", "Exact", "Vague"),
      ("Tough", "Sturdy", "Fragile"),
      ("Eager", "Keen", "Reluctant")
   ],
   "hard": [
      ("Ephemeral", "Transient", "Perpetual"),
      ("Maelstrom", "Turmoil", "Tranquil"),
      ("Obsequious", "Sycophantic", "Contemptuous"),
      ("Eloquent", "Articulate", "Incoherent"),
      ("Diligent", "Industrious", "Indolent"),
      ("Frugal", "Thrifty", "Wasteful"),
      ("Arrogant", "Haughty", "Humble"),
      ("Elucidate", "Clarify", "Obfuscate"),
      ("Intrepid", "Dauntless", "Pusillanimous"),
      ("Exultant", "Jubilant", "Melancholic"),
      ("Elusive", "Evasive", "Obvious"),
      ("Ostentatious", "Flamboyant", "Austere"),
      ("Meticulous", "Punctilious", "Negligent"),
      ("Gregarious", "Convivial", "Reticent"),
      ("Impartial", "Nonpartisan", "Prejudiced"),
      ("Fickle", "Inconsistent", "Reliable"),
      ("Clandestine", "Surreptitious", "Overt"),
      ("Phlegmatic", "Placid", "Temperamental"),
      ("Lethargic", "Torpid", "Zestful"),
      ("Amicable", "Cordial", "Hostile")
   ]
   }
'''
combined = []

for level in ['easy', 'medium', 'hard']:
    all_in_level = {word[0] for word in wordbank[level]} | {word[1] for word in wordbank[level]} | {word[2] for word in wordbank[level]}
    for word in all_in_level:
        combined.append(word)

for word in combined:
    if combined.count(word) > 1:
        print(word)
'''