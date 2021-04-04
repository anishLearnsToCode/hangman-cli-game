import data.color as COLOR


def success(text='', end='\n') -> None:
    print(COLOR.GREEN + COLOR.BOLD + text + COLOR.END, end=end)


def failure(text='', end='\n') -> None:
    print(COLOR.RED + COLOR.BOLD + text + COLOR.END, end=end)


def information(text='', end='\n') -> None:
    print(COLOR.BLUE + COLOR.BOLD + text + COLOR.END, end=end)


def warning(text='', end='\n') -> None:
    print(COLOR.YELLOW + COLOR.BOLD + text + COLOR.END, end=end)


def gameStatus(visibleAlphabets: str, attemptsRemaining: int) -> None:
    information('Current State:  ', end='')
    for character in visibleAlphabets:
        information(character, end=' ')
    warning(f'\tAttempts Remaining : {attemptsRemaining}')
