from typing import Never


def error(message: str) -> Never:
    print(f"\033[91m{message}\033[0m")
    exit()
