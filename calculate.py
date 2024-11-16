import sys
import os
import importlib

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "calculating"))
)

figs = ["circle", "square"]
funcs = ["perimeter", "area"]
sizes = {}


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    # Динамически импортируем модули с использованием importlib
    module = importlib.import_module(fig)
    result = getattr(module, func)(*size)
    print(f"{func} of {fig} is {result}")


if __name__ == "__main__":
    func = ""
    fig = ""
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(
            map(
                int,
                input(
                    "Input figure sizes, 1 for circle and square\n"
                ).split(" "),
            )
        )

    calc(fig, func, size)
