import randomWordGenerator
import printer

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


def gameHasEnded(actualWord, guessedWord, attemptsRemaining):
    if guessedWord == actualWord:
        return printer.success("You WON! :D")
    elif attemptsRemaining <= 0:
        printer.failure("You Lost :(")
        return printer.information("Word was %s" % actualWord)
    return False


def isVowel(character):
    return character in vowels


def createVisibleAlphabets(word):
    return ''.join([word[i] if isVowel(word[i]) else '_' for i in range(len(word))])


def startGame(attempts=5):
    actualWord = randomWordGenerator.getRandomWord()
    visibleAlphabets = createVisibleAlphabets(actualWord)
    attemptsRemaining = attempts
    printer.gameStatus(visibleAlphabets, attemptsRemaining)

    while True:
        guess = input("Guess a character: ")
        print()

        visibleAlphabets, attemptsRemaining = updateVisibleAlphabetsWithGuess(actualWord, guess, visibleAlphabets,
                                                                              attemptsRemaining)
        printer.gameStatus(visibleAlphabets, attemptsRemaining)
        if gameHasEnded(actualWord, visibleAlphabets, attemptsRemaining):
            break


if __name__ == "__main__":
    startGame()
