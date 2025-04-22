import os
import json
import random


current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "words.json")

# Debug print
print("Looking for words.json at:", json_path)
print("File exists?", os.path.exists(json_path))

# Try loading the file
try:
    with open(json_path, "r") as f:
        data = json.load(f)
        words = data["words"]
    print("✅ JSON loaded successfully!")
except Exception as e:
    print("❌ Failed to load JSON:", e)
    exit()

# Confirm loaded data
print("Loaded words (first ten words):", words[:10])
print("                                   ")

#Game Data:

target = random.choice(words)
MAX_ATTEMPTS = 6

def get_feedback(guess, target):
    feedback = ["⬛️"] * 5
    target_chars = list(target)

    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = "🟩"
            target_chars[i]= None

    for i in range(5):
        if feedback[i] == "⬛️" and guess[i] in target_chars[i]:
            feedback[i] = "🟨"
            target_chars[target_chars.index(guess[i])] = None

        return feedback


#Game Imprint
print("Welcome to Wordle (recreated in Python!)")
print("The rules are simple. Guess the five letter word in six attempts.")

attempts = 0
max_uses_per_word = 1
word_usage = {}    

while attempts < MAX_ATTEMPTS:
    guess = input(f"Attempt {attempts+1}/6: ").lower()

    if len(guess) > 5:
            print("❌ Your word cannot be more than five letters.")
            continue
    
    if len(guess) < 5:
         print("❌ Your word cannot be less than five letters.")
         continue
    
    if not guess.isalpha():
         print("❌ Your word cannot be accepted as it doesn't contain letters.")
         continue
    
    if word_usage.get(guess,0) >= max_uses_per_word:
         print(f"You've already guessed that word. Try a different one!")
         continue
    
    word_usage[guess] = word_usage.get(guess,0) + 1

    if guess not in words:
            print("🤔 Unable to find your word.")
            continue

         
    feedback = get_feedback(guess, target)
    print(" ".join(feedback) + "\n")

    if guess == target:
            print(f"🎉 You nailed it! The word was: {target}")
            break

    attempts += 1

    if attempts == MAX_ATTEMPTS:
        print(f"❌ Sorry man, you are out of attempts! The correct word was: {target}")
        break

