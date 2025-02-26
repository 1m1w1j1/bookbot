# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# Code Summary: Text Analysis Script

This Python script performs basic text analysis on a provided text file (e.g., a book). Here's a breakdown of its functionality:

## Overview

The script takes a file path as a command-line argument. It then:

1.  **Reads the File:** Extracts the entire text content from the specified file.
2.  **Counts Words:** Determines the total number of words in the text.
3.  **Counts Characters:** Calculates the frequency of each character within the text.
4.  **Sorts Character Counts:** Sorts the character frequencies in descending order.
5.  **Prints Results:** Displays the word count and character frequencies in a formatted output.

## Script Structure

* **`get_book_text(path_to_file)`:**
    * Reads the content of the file specified by `path_to_file`.
    * Returns the file content as a string.
* **`main()`:**
    * Handles command-line arguments.
    * Checks if a file path is provided.
    * Calls `get_book_text()` to read the file.
    * Calls `get_words_number()` (from `stats.py`) to count words.
    * Calls `character_count()` (from `stats.py`) to count characters.
    * Calls `dict_sort()` (from `stats.py`) to sort the character count dictionary.
    * Prints the word count and character frequencies to the console.
* **`stats.py`**
    * Contains the functions `get_words_number`, `character_count`, and `dict_sort`. These functions are used for counting words, characters, and sorting dictionaries.

## Usage

To run the script, use the following command in your terminal:

```bash
python3 main.py <path_to_book>
