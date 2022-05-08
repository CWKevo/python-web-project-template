from typing import Generator

from pathlib import Path
from random import random as rand

# Overwrite __doc__ with README, so that pdoc can render it:
README_PATH = Path(__file__).parent.parent.absolute() / Path('README.md')
try:
    with open(README_PATH, 'r', encoding="UTF-8") as readme:
        __readme__ = readme.read()
except Exception:
    __readme__ = "Failed to read README.md!" # fallback message, for example when there's no README

__doc__ = __readme__



def infinitum(multiplier: int = 314) -> Generator[int, None, None]:
    """
        Generates an infinite sequence of random numbers.
    """
        
    while True:
        yield round(((rand() + 1) ** multiplier) % 21768543)



if __name__ == "__main__":
    count = 0
    max_count = 10

    for random in infinitum():
        print(random)
        count += 1

        if count >= max_count:
            break
