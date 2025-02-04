# Word Count (WC) Utility

This project is a simple command-line utility similar to the Unix `wc` command. It reads a text file and provides statistics such as the number of bytes, lines, words, and characters.

## Features
- Counts bytes, lines, words, and characters in a given text file.
- Allows users to specify which statistics to display using command-line options.
- Handles file reading errors gracefully.

## Installation
Ensure you have Python installed (version 3.x recommended).

Clone the repository:
```sh
git clone <repository_url>
cd <repository_name>
```

## Usage
Run the script with a filename and optional flags:
```sh
python main.py <filename> [-c -l -w -m]
```

### Options:
- `-c` : Display byte count
- `-l` : Display line count
- `-w` : Display word count
- `-m` : Display character count

### Example:
```sh
python main.py sample.txt -c -l -w
```
Output:
```
Bytes: 1024
Lines: 50
Words: 200
```

If no options are provided, it defaults to `-c -l -w`.

## Running Tests
To run the test suite using `unittest`, execute:
```sh
pytest .\tests\test_wc.py
```

