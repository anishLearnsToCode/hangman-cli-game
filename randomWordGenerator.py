import random
from data.words import words


# Picks a random word from a predefined list of Words
def getRandomWord():
    randomIndex = random.randint(0, len(words))
    return words[randomIndex]
