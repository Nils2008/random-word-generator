import random 
from replit import db
random_letter = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0") 
times = 0 
random_word = ("")
secret_password = "XUJUQA"
how_long = random.randint(5, 20)

for _ in range(how_long):
  random_letter_generator = random.choice(random_letter)
  times = 1
  if times == 0:
    random_word = random_letter_generator 
  elif times == 1:
    random_word = random_word + random_letter_generator
  db["Password"] = random_word
print(random_word)
