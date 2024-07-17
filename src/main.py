import sys

from pynput import keyboard as kb
from clipboard import copy as copy2clip
import time
from typing import Any, Self
from iter_util import DoubleIter, StrListIter, IterItem


def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def copy_item(item: IterItem):
    print(f"id: {item[0]}")
    copy2clip(item[1])


def on_press(key: kb.Key | kb.KeyCode | None) -> None:
    global copy_iter, continue_after_exit

    if key is None:
        return

    if key == kb.Key.esc:
        print("Aborted!")
        sys.exit()

    if key == kb.KeyCode(char="\x16"):
        time.sleep(0.1)
        try:
            copy_item(next(copy_iter))
        except StopIteration:
            print("Complete!")
            sys.exit()

    if key == kb.KeyCode(char=":"):
        continue_after_exit = True
        sys.exit()


def handle_cmd(cmd: str) -> bool:
    global copy_iter

    cmd = cmd.lstrip(":").strip().lower()
    if cmd == "":
        return False

    if cmd == "exit" or cmd == "quit" or cmd == "q":
        print("Aborted!")
        exit()

    if cmd == "help" or cmd == "h":
        print("""
Here is help:
- use Ctrl+V to paste -> it will automatically advance to the next item
- the id of the item you currently paste is printed out
- use Esc to exit when not in command mode
- use ':' to execute a command

Commands:
`$` <id> ... go to the id
`<` <number> ... go back number amount of items
`>` <number> ... go forward number amount of items
`help` | `h` ... print this help message
`exit` | `quit` | `q` ... exit the program
        """)

        return False

    if cmd.startswith(">") or cmd.startswith("<"):
        skip: int
        try:
            skip = int(cmd[1:].lstrip())
        except ValueError:
            print("Invalid number")
            return False
        try:
            item = copy_iter.next(skip) if cmd.startswith(">") else copy_iter.previous(skip)
            copy_item(item)
            return True
        except StopIteration:
            print("Exceeded range")
            return False

    if cmd.startswith("$"):
        id = cmd[1:].lstrip()

        try:
            item = copy_iter.find(id)
            copy_item(item)
            return True
        except ValueError:
            print("Value could not be found")
            return False


def main() -> None:
    global continue_after_exit

    copy_item(copy_iter.next())
    while True:
        continue_after_exit = False
        listener = kb.Listener(on_press=on_press)
        listener.start()
        listener.join()

        if continue_after_exit:
            flush_input()
            if not handle_cmd(input(":")):
                copy_item(copy_iter.current())
            continue
        break


copy_iter: DoubleIter = StrListIter(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
continue_after_exit: bool = False
FILE_NAME = "input/data.txt"

if __name__ == '__main__':
    main()
