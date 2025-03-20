![PackagePackage](https://github.com/software-students-spring2025/3-python-package-usps-525-3-violation/actions/workflows/build.yaml/badge.svg)

# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Team members
- [Tim Xu](https://github.com/timxu23)
- [Anna Ye](https://github.com/AnnaTheYe)
- [Jack Wang](https://github.com/JackInTheBox314)
- [Joylyn Gong](https://github.com/joylyngong)

## Description

This is an educational quiz game package. Users can choose between playing a math game, vocab game, geography game, or science game to test their skills and knowledge.

## PyPI Link

## Steps necessary to run program

### Importing into your project
# TODO

### Running example usages

1. First, clone the respository:

```
git clone https://github.com/software-students-spring2025/3-python-package-usps-525-3-violation.git
```
2. Then change directories into the repository:

```
cd 3-python-package-usps-525-3-violation
```

3. Create `pipenv` virtual environment and install package:

```
something to do with PyPI will go here, refer to example
```
4. Activate virtual environment:

```
pipenv shell
```

5. Run example script:

```
PYTHONPATH=src python3 -m packagepackage
```

6. Follow instructions and enjoy!

### Running Pytest

1. First, clone the respository:

```
git clone https://github.com/software-students-spring2025/3-python-package-usps-525-3-violation.git
```
2. Then change directories into the repository:

```
cd 3-python-package-usps-525-3-violation
```

3. Create `pipenv` virtual environment and install package:

```
something to do with PyPI will go here, refer to example
```
4. Activate virtual environment:

```
pipenv shell
```

5. Run pytest with coverage reports:

```
PYTHONPATH=src pipenv run pytest --cov=packagepackage --cov-report=term-missing
```


- how a developer who wants to import your project into their own code can do so - include documentation and code examples for all functions in your package and a link to an example Python program that uses each of them.
- how a developer who wants to contribute to your project can set up the virtual environment, install dependencies, and build and test your package for themselves.
- the names of all teammates as links to their GitHub profiles in the `README.md` file.
- instructions for how to configure and run all parts of your project for any developer on any platform - these instructions must work!
- instructions for how to set up any environment variables and import any starter data into the database, as necessary, for the system to operate correctly when run.
- if there are any "secret" configuration files, such as `.env` or similar files, that are not included in the version control repository, examples of these files, such as `env.example`, with dummy data must be included in the repository and exact instructions for how to create the proper configuration files and what their contents should be must be supplied to the course admins by the due date.

## Function usages and examples:

### play_math
what does the code do
exceptions thrown:

| Argument    | Type | Description |
|------------|------|-------------|
| `arg1`  | `datatype`  | wordwords. |
| `arg2` | `datatype`  | yadayada |

```
example input output
```

### play_geo
what does the code do
exceptions thrown:

| Argument    | Type | Description |
|------------|------|-------------|
| `arg1`  | `datatype`  | wordwords. |
| `arg2` | `datatype`  | yadayada |

```
example input output
```

### play_vocab
what does the code do
exceptions thrown:

| Argument    | Type | Description |
|------------|------|-------------|
| `arg1`  | `datatype`  | wordwords. |
| `arg2` | `datatype`  | yadayada |

```
example input output
```

### play_science
This function starts a science quiz game. Users can choose number of questions, ranging from 1 to 10, and choose the difficulty of the questions to be easy, hard, or a mix of both. Users interact with the function via `input()`.

| Argument    | Type | Description |
|------------|------|-------------|
| `num_questions`  | `Integer`  | Number of questions you will be given, has to be between 1 and 10. |
| `difficulty` | `string`  | Difficulty of the questions, must be `easy`, `hard`, or `mix` for a mix of questions of both difficulties. |

```
>>> package.play_science(num_questions=10, difficulty='easy')

What do you call the study of weather, climate and the atmosphere?
A: Climatology
B: Aerology
C: Atmospheric Science
D: Meteorology
Please enter A, B, C, or D: a
Incorrect! The correct answer was Meteorology.
Press ENTER to continue

Who is credited with coming up with the theory of evolution?
A: Robert Oppenheimer
B: Galileo Galilei
C: Charles Darwin
D: Gregor Mendel
Please enter A, B, C, or D: a
Incorrect! The correct answer was Charles Darwin.
Press ENTER to continue

What are the three layers of the Earth
A: Outer shell, inner shell, and center
B: Land, water, and atmosphere
C: Rock layer, magma layer, and deep core
D: Crust, mantle and core
Please enter A, B, C, or D: d
Correct!
Press ENTER to continue

You need to study more! Your score was 1/3.
```
