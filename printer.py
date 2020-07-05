class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    YELLOW = "\033[1;33m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


def success(text='', end='\n'):
    print(Colors.GREEN + Colors.BOLD + text + Colors.END, end=end)
    return True


def failure(text='', end='\n'):
    print(Colors.RED + Colors.BOLD + text + Colors.END, end=end)


def information(text='', end='\n'):
    print(Colors.BLUE + Colors.BOLD + text + Colors.END, end=end)
    return True


def warning(text='', end='\n'):
    print(Colors.YELLOW + Colors.BOLD + text + Colors.END, end=end)


def gameStatus(visibleAlphabets, attemptsRemaining):
    information('Current State: ', end=' ')
    for character in visibleAlphabets:
        information(character, end=' ')
    warning('\tAttempts Remaining : ' + str(attemptsRemaining))
