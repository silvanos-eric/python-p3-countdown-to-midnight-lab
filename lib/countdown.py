# your code goes here!
import time


def countdown(limit: int) -> None:
    """Counts down from limit and prints "HAPPY NEW YEAR!"."""
    counter = limit
    while counter > 0:
        print(f"{counter} SECOND(S)!")
        counter -= 1
    print("HAPPY NEW YEAR!")


def countdown_with_sleep(limit: int) -> None:
    counter = limit
    while counter > 0:
        print(f"{counter} SECOND(S)!")
        counter -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
