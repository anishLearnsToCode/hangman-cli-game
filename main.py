import random_word_generator
import colord

vowels = ('a', 'e', 'i', 'o', 'u')


def getUpdatedVisibleAlphabets(actualWord, visibleAlphabets, guess):
    guessedAlphabets = ''

    for i in range(len(actualWord)):
        # If character is missing and actual character is equal to guessed character
        guessedAlphabets += guess if visibleAlphabets[i] == '_' and actualWord[i] == guess else visibleAlphabets[i]

    return guessedAlphabets


def updateVisibleAlphabetsWithGuess(actualWord, guess, visibleAlphabets, attemptsRemaining):
    if guess in actualWord:
        visibleAlphabets = getUpdatedVisibleAlphabets(actualWord, visibleAlphabets, guess)
    else:
        attemptsRemaining -= 1
    return visibleAlphabets, attemptsRemaining


def printVisibleAlphabets(visibleAlphabets, attemptsRemaining):
    colord.print_information("Current State: ", end=" ")
    for i in visibleAlphabets:
        colord.print_information(i, end=" ")
    colord.print_warning("\tAttempts Remaining : %d" % attemptsRemaining)


def gameHasEnded(actualWord, guessedWord, attemptsRemaining):
    if guessedWord == actualWord:
        colord.print_sucess("You WON! :D")
        return True
    elif attemptsRemaining <= 0:
        colord.print_failure("You Lost :(")
        colord.print_information("Word was %s" % actualWord)
        return True
    return False


def isVowel(character):
    return character in vowels


def createVisibleAlphabets(actualWord):
    visibleAlphabets = ''
    for i in range(len(actualWord)):
        visibleAlphabets += actualWord[i] if isVowel(actualWord[i]) else '_'

    return visibleAlphabets


def startGame(attempts=5):
    actualWord = random_word_generator.getRandomWord()
    visibleAlphabets = createVisibleAlphabets(actualWord)
    attemptsRemaining = attempts
    printVisibleAlphabets(visibleAlphabets, attemptsRemaining)

    while True:
        guess = input("Guess a character: ")
        print()

        visibleAlphabets, attemptsRemaining = updateVisibleAlphabetsWithGuess(actualWord, guess, visibleAlphabets,
                                                                              attemptsRemaining)
        printVisibleAlphabets(visibleAlphabets, attemptsRemaining)
        if gameHasEnded(actualWord, visibleAlphabets, attemptsRemaining):
            break


if __name__ == "__main__":
    startGame()
