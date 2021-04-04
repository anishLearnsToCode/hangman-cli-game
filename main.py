from typing import Tuple

from utils import printer
from utils import randomWordGenerator

VOWELS = ('a', 'e', 'i', 'o', 'u')
EMPTY_STRING = ''


def getUpdatedVisibleAlphabets(actualWord: str, visibleAlphabets: str, guess: str) -> str:
    return EMPTY_STRING.join(
        [guess if guess == actualWord[index] else visibleAlphabets[index] for index in range(len(actualWord))]
    )


def updateVisibleAlphabetsWithGuess(actualWord: str, guess: str, visibleAlphabets: str, attemptsRemaining: int) -> Tuple[str, int]:
    if guess in actualWord:
        visibleAlphabets = getUpdatedVisibleAlphabets(actualWord, visibleAlphabets, guess)
    else:
        attemptsRemaining -= 1
    return visibleAlphabets, attemptsRemaining


def gameHasEnded(actualWord, guessedWord, attemptsRemaining):
    if guessedWord == actualWord:
        printer.success('You WON! :D')
        return True
    elif attemptsRemaining <= 0:
        printer.failure('You Lost :(')
        printer.information(f'Word was {actualWord}')
        return True
    return False


def isVowel(character: str) -> bool:
    return character in VOWELS


def createVisibleAlphabets(word: str) -> str:
    return EMPTY_STRING.join([character if isVowel(character) else '_' for character in word])


def startGame(attempts=5):
    actualWord = randomWordGenerator.getRandomWord()
    visibleAlphabets = createVisibleAlphabets(actualWord)

    while not gameHasEnded(actualWord, visibleAlphabets, attempts):
        printer.gameStatus(visibleAlphabets, attempts)
        guess = input('Guess a character: ')
        print()
        visibleAlphabets, attempts = updateVisibleAlphabetsWithGuess(actualWord, guess, visibleAlphabets, attempts)


if __name__ == '__main__':
    startGame(attempts=6)
