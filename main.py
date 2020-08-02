import randomWordGenerator
import printer

vowels = ('a', 'e', 'i', 'o', 'u')


def getUpdatedVisibleAlphabets(actualWord, visibleAlphabets, guess):
    return ''.join(
        [guess if guess is actualWord[index] else visibleAlphabets[index] for index in range(len(actualWord))]
    )


def updateVisibleAlphabetsWithGuess(actualWord, guess, visibleAlphabets, attemptsRemaining):
    if guess in actualWord:
        visibleAlphabets = getUpdatedVisibleAlphabets(actualWord, visibleAlphabets, guess)
    else:
        attemptsRemaining -= 1
    return visibleAlphabets, attemptsRemaining


def gameHasEnded(actualWord, guessedWord, attemptsRemaining):
    if guessedWord == actualWord:
        return printer.success('You WON! :D')
    elif attemptsRemaining <= 0:
        printer.failure('You Lost :(')
        return printer.information('Word was ' + actualWord)
    return False


def isVowel(character):
    return character in vowels


def createVisibleAlphabets(word):
    return ''.join([character if isVowel(character) else '_' for character in word])


def startGame(attempts=5):
    actualWord = randomWordGenerator.getRandomWord()
    visibleAlphabets = createVisibleAlphabets(actualWord)
    printer.gameStatus(visibleAlphabets, attempts)

    while True:
        guess = input('Guess a character: ')
        print()
        visibleAlphabets, attempts = updateVisibleAlphabetsWithGuess(actualWord, guess, visibleAlphabets, attempts)
        printer.gameStatus(visibleAlphabets, attempts)
        if gameHasEnded(actualWord, visibleAlphabets, attempts):
            break


if __name__ == '__main__':
    startGame(7)
