# BookBot

BookBot is a command-line Python application that analyzes text files and generates a report containing word counts and character frequencies.

This project was completed as part of the [Boot.dev](https://www.boot.dev) Python curriculum.

## Features

- Reads text files from a supplied file path.
- Counts the total number of words.
- Counts how frequently each character appears, ignoring case.
- Sorts characters by frequency, from highest to lowest.
- Displays an organized report containing alphabetic characters and their counts.
- Uses Python type hints and separates statistics functions into a module.

## Requirements

- Python 3.9 or newer
- No third-party dependencies

## Getting Started

Clone the repository:

```bash
git clone https://github.com/1m1w1j1/bookbot.git
cd bookbot
```

Create a directory for your books:

```bash
mkdir -p books
```

Place a plain-text book inside the `books/` directory. You can obtain public-domain books from [Project Gutenberg](https://www.gutenberg.org/).

For example, save a book as `books/frankenstein.txt`.

Run BookBot:

```bash
python3 main.py books/frankenstein.txt
```

## Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: ...
t: ...
a: ...
...
============= END ===============
```

Character counts depend on the text being analyzed.

## Project Structure

```text
bookbot/
├── .gitignore
├── README.md
├── main.py
├── stats.py
└── books/          # Local book files (ignored by Git)
```

**main.py** — Handles command-line arguments, reads the book, and displays the report.

**stats.py** — Contains functions for counting words, counting characters, and sorting character frequencies.

## Notes

The `books/` directory is excluded from Git using `.gitignore`. Book text files must be supplied locally.

This project uses only Python's standard library.
