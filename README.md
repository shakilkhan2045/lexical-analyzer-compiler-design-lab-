# lexical-analyzer-compiler-design-lab-

****1. Introduction****
Purpose of the Program
The Lexical Analysis program is designed to analyze the lexical structure of a given code by dividing it into individual tokens. It uses regular expressions to identify various token types, such as identifiers, constants, keywords, and operators.

**Environment Setup**
Programming Language: Python
Integrated Development Environment (IDE): Visual Studio Code, PyCharm, or any Python IDE of your choice.
**2. Code Description**
Regular Expression Patterns
The program uses regular expression patterns to define how different types of tokens are recognized in the input code. These patterns include:

**identifier_pattern:** Matches identifiers while excluding specific keywords.
**constant_pattern:** Matches constants, including integers and floating-point numbers.
***parenthesis_pattern:** Matches parentheses (opening and closing).
***punctuation_pattern: **Matches punctuation symbols (periods, commas, semicolons).
***arithmetic_operator_pattern**: Matches arithmetic operators (+, -, *, /).
***logical_operator_pattern:** Matches logical operators (and, or, not).
***keyword_pattern:** Matches specific keywords (if, else, int, float, double, char, void).
*****Tokenization Process****
The program combines these individual patterns into a single regular expression pattern, token_pattern, to tokenize the input code. It then iterates through the input line, matches tokens based on the patterns, and categorizes them into their respective types. Token counts are maintained for each type.

**3. Example Usage**
Running the Lexical Analysis Program
To use the Lexical Analysis program, follow these steps:

Open your Python Integrated Development Environment (IDE), such as Visual Studio Code or PyCharm.

Copy the provided code into a Python file (e.g., lexical_analysis.py).

Run the program in your IDE.

You will be prompted to enter a line of code.

Enter the code you want to analyze.

The program will tokenize the input and provide counts of different token types.

**4. Key Points**
**Regular Expression Patterns:**
Regular expressions are used to define how tokens are recognized.
Patterns are defined for identifiers, constants, parentheses, punctuation, operators, and keywords.
**Tokenization Logic:**
The program tokenizes the input code into individual tokens.
It categorizes tokens into types (e.g., identifier, constant, keyword).
Token counts are maintained for each type.
**Input and Output:**
The program takes user input in the form of code lines.
It prints the counts of different token types in the input code.
Tokens of the same type are comma-separated in the output.

**5. Conclusion :**
The Lexical Analysis program provides a useful tool for analyzing the structure of code and extracting meaningful information from it. It uses regular expressions and tokenization logic to categorize code elements into various types. By following the provided steps, you can easily use this program to perform lexical analysis on your code.
