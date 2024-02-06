# Readme

## Description
This Python script, `train_grep_python.py`, is designed to search for a given pattern within a text file and return the lines where the pattern is found. It provides a simple and efficient way to extract specific lines from a file based on user-defined patterns.

## Features
- **Pattern Search**: The script efficiently scans through the lines of a text file and identifies lines containing the specified pattern.
- **Customizable**: Users can easily customize the pattern they want to search for, allowing for flexibility in extracting relevant information from text files.
- **Output**: The script returns the lines where the pattern is found, providing users with the relevant information they seek.

## Usage
To use the script, follow these steps:

1. Ensure you have Python installed on your system.
2. Download `train_grep_python.py` and save it in your desired directory.
3. Open a terminal or command prompt and navigate to the directory where `train_grep_python.py` is saved.
4. Run the script using the following command:
   ```
   python train_grep_python.py <file_path> <pattern>
   ```
   Replace `<file_path>` with the path to the text file you want to search, and `<pattern>` with the pattern you want to search for.

   Example:
   ```
   python train_grep_python.py example.txt "search_pattern"
   ```

5. The script will display the lines where the pattern is found in the specified file.

## Example
Suppose we have a text file named `example.txt` with the following content:
```
This is line 1.
Another line with the pattern.
Line containing the search_pattern.
This line does not contain the pattern.
```
Running the script with the command:
```
python train_grep_python.py example.txt "search_pattern"
```
will output:
```
Line containing the search_pattern.
```

## Notes
- If the specified file does not exist or cannot be opened, the script will display an error message.
- If no lines containing the specified pattern are found, the script will indicate that no matches were found.

## Compatibility
This script is compatible with Python 3.10+.
