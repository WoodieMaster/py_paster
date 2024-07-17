# Py Paster
A simple program for easily pasting multiple times with minimal effort

# Overview
## Command Line
run the program using `python main.py <...args>`

### Arguments
- `--help` | `-h` ... print help information (does not need anything else)
- `<file_name>` ... the file to load
- (`--format` | `-f`) `<format>`  ... specify the format of the file (will normally be determined by the file ending)
- (`--timeout` | `-t`) `<timeout>` ... the timeout to wait after pasting before switching to the next value (in seconds as a float) 
- `--no-id` ... prevent the id from being printed
- `--show-value` ... print the value

## Program
- use Ctrl+V to paste -> it will automatically advance to the next item
- the id of the item you currently paste is printed out
- use Esc to exit when not in command mode
- use ':' to execute a command

Commands:
- `$ <id>` ... go to the id
- `< <number>` ... go back number amount of items
- `> <number>` ... go forward number amount of items
- `help` | `h` ... print this help message
- `exit` | `quit` | `q` ... exit the program

# Supported Formats
### Normal Text
Splits the text by a seperator.

Id is the index of the current section

- (`--seperator` | `--sep` ) `<seperator>` ... set the seperator to split the input text by; (default: newline)

### CSV
Every line is 

Uses one section as the id, and another for the value ()

- `--id-idx <id_idx>` ... set the section to use for the id 
- `--value-idx <value_idx>` ... set the section to use for the value
- (`--seperator` | `--sep` ) `<seperator>` ... set the seperator to use for splitting sections of the
- `--header` ... skip the first line for the header of the csv

### JSON
Can handle arrays and objects

#### Arrays
every element is its own value to paste, the index of that element is used for the id

#### Objects
the key is the id and the value at the key is the value to paste

# Requirements
- [Python](https://www.python.org/downloads/) (preferably 3.12 -> was written in that version)

# Install
1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or [download](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives) the repo
2. install the requirements inside `requirements.txt` (preferably with a [pyton virtual environment](https://docs.python.org/3/library/venv.html))
3. run `src/main.py` using [python](https://realpython.com/run-python-scripts/)