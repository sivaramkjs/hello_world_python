# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Runtime and assumptions

- This repository is a collection of small Python 3 scripts used for learning and experimentation.
- There is no package configuration, dependency file, or test framework configured; scripts are run directly with the Python interpreter.

## Common commands

Use `python3` below; if your environment provides `python` for Python 3, you can substitute it.

### Run example / tutorial scripts (root directory)

- Run the classic "hello world" example:
  - `python3 hello_world.py`
- Run any numbered concept script (variables, strings, loops, etc.):
  - `python3 01_variables.py`
  - `python3 03_numbers.py`
  - `python3 06_conditional_statements.py`
  - ...and similarly for the other `NN_*.py` files in the repository root.

### Run exercise scripts

Scripts under `Exercises/` are standalone programs demonstrating specific problems (even numbers, guessing game, car game, etc.). Run them directly, for example:

- `python3 Exercises/01_even_numbers.py`
- `python3 Exercises/02_guessing_game.py`
- `python3 Exercises/03_car_game.py`

### Run the Fibonacci module examples

The `Modules/` directory demonstrates creating and importing modules.

- Run the Fibonacci module as a script, passing an upper bound for the sequence:
  - `python3 Modules/fibonacci.py 50`
- Run the import-usage examples (shows different import styles for the same module):
  - `python3 Modules/module_usage.py`

### Testing and tooling

- At the time of writing, there is **no automated test suite, linter, or formatter configured** for this project.
- To "test" behavior, run the specific script you are working on (as shown above) and inspect its output.

If you introduce a formal test framework (e.g., `pytest` or `unittest`) or add tooling (formatters/linters), update this section with the exact commands to run them.

## Project structure and architecture

High-level layout:

- **Root scripts (`hello_world.py`, `01_variables.py`, `02_strings.py`, ..., `14_dictionary.py`, `app.py`)**
  - These are small, self-contained scripts illustrating basic Python concepts:
    - Variables, numbers, strings and string formatting
    - Type conversion and operators
    - Conditional statements, `for` and `while` loops
    - Functions, lists (including 2D lists), tuples, sets, and dictionaries
  - There are **no imports between these files**; each can be run independently.
  - `app.py` currently contains a few variable assignments and no executable logic beyond definitions.

- **`Exercises/`**
  - Contains small practice programs that build on the core concepts, e.g.:
    - `01_even_numbers.py` counts and prints even numbers in a range.
    - Other scripts implement small interactive or algorithmic exercises (guessing game, car game, list processing, etc.).
  - Each exercise script is standalone and uses only Python’s standard library and built-in types.

- **`Modules/`**
  - Demonstrates authoring and consuming a simple module:
    - `fibonacci.py`
      - Defines two functions:
        - `fib_nums_up_to(n)`: prints Fibonacci numbers less than `n`.
        - `n_fib_nums(n)`: prints the first `n` Fibonacci numbers.
      - When run directly (`python3 Modules/fibonacci.py 50`), it reads an integer from `sys.argv[1]` and prints Fibonacci numbers up to that bound.
    - `module_usage.py`
      - Shows multiple import patterns for `fibonacci`:
        - `import fibonacci` and calling `fibonacci.fib_nums_up_to` / `fibonacci.n_fib_nums`.
        - `from fibonacci import *` and calling the functions directly.
        - `from fibonacci import fib_nums_up_to, n_fib_nums`.
        - `import fibonacci as fib` and alias-based calls.
        - `from fibonacci import fib_nums_up_to as fib1, n_fib_nums as fib2` with aliases.
      - Running this script sequentially executes all these import styles and prints the resulting Fibonacci sequences.

## Notes for future changes

- There is no existing packaging, dependency management, or test harness; you are free to introduce them as the project grows.
- If you add new modules meant for reuse across scripts, placing them under `Modules/` (or a new package directory) and importing them, as demonstrated in `Modules/module_usage.py`, will keep the structure consistent with the current learning-focused layout.
