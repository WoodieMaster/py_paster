import sys
from typing import Iterable
from util import error

_NORMAL_ARGS: set[str] = {
    "-h", "--help", "--no-id", "--show-value", "--header"
}
_VALUE_ARGS: set[str] = {
    "--format", "-f", "--timeout", "-t", "--seperator", "--sep", "--id-idx", "--value-idx"
}

normal_args: set[str] = set()
value_args: dict[str, str] = dict()
text_params: list[str] = []


def duplicate_assert(iterable: Iterable, arg1: str, arg2: str) -> None:
    global normal_args, value_args

    if arg1 in iterable and arg2 in iterable:
        error(f"Duplicate arguments: '{arg1}' and '{arg2}' do the same thing")


def load_args(args: list[str]) -> None:
    global normal_args, value_args, text_params

    arg_iter = iter(args)
    for arg in arg_iter:
        if arg.startswith("-"):
            if arg in _NORMAL_ARGS:
                if arg in normal_args:
                    error(f"Duplicate argument '{arg}'")

                normal_args.add(arg)
            elif arg in _VALUE_ARGS:
                if arg in value_args:
                    error(f"Duplicate argument '{arg}'")

                try:
                    value_args[arg] = next(arg_iter)
                except StopIteration:
                    error(f"No value for argument '{arg}'")
            else:
                error(f"Unknown argument '{arg}'")
        else:
            text_params.append(arg)

    duplicate_assert(value_args, "--format", "-f")
    duplicate_assert(value_args, "--timeout", "-t")
    duplicate_assert(value_args, "--seperator", "--sep")
    duplicate_assert(normal_args, "--help", "-h")


load_args(sys.argv[1:])

print(normal_args)
print(value_args)
print(text_params)

exit()
