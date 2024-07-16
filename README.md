# Py Paster
A simple program for easily pasting multiple times with minimal effort

# Overview
## Command Line

## Program
- use Ctrl+V to paste -> it will automatically advance to the next item
- the id of the item you currently paste is printed out
- use Esc to exit when not in command mode
- use ':' to execute a command

Commands:
- `$` <id> ... go to the id
- `<` <number> ... go back number amount of items
- `>` <number> ... go forward number amount of items
- `help` | `h` ... print this help message
- `exit` | `quit` | `q` ... exit the program

# Requirements
- [Python](https://www.python.org/downloads/) (preferably 3.12 -> was written in that version)

# Install
1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or [download](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives) the repo
2. install the requirements inside `requirements.txt` (preferably with a [pyton virtual environment](https://docs.python.org/3/library/venv.html))
3. run `src/main.py` using [python](https://realpython.com/run-python-scripts/)