from typing import NoReturn


def error(message: str) -> NoReturn:
    print(f"\033[91m{message}\033[0m")
    exit()
