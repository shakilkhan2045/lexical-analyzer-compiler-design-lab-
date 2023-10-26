import re   # Import the regular expression module

# Define regular expression patterns for various token types
# These patterns define how different types of tokens are recognized in the input code
identifier_pattern = r'\b(?!int\b|double\b|float\b|char\b|void\b|if\b|else\b|elseif\b|or\b|and\b|not\b)[a-zA-Z]\w*\b'
constant_pattern = r'\d+|\d*\.\d+'
parenthesis_pattern = r'[\(\)]'
punctuation_pattern = r'[.,;]'
arithmetic_operator_pattern = r'[+\-*/]'
logical_operator_pattern = r'(and|or|not)'
keyword_pattern = r'\b(if|else|int|float|double|char|void)\b'

# Combine all the individual patterns into a single regex pattern
token_pattern = re.compile(f'({identifier_pattern}|{constant_pattern}|{parenthesis_pattern}|{punctuation_pattern}|{arithmetic_operator_pattern}|{logical_operator_pattern}|{keyword_pattern})')

def tokenize_line(line):
    tokens = []  # Initialize an empty list to store tokens
    token_counts = {  # Initialize a dictionary to store token counts
        "identifier": 0,
        "constant": 0,
        "parenthesis": 0,
        "punctuation": 0,
        "arithmetic operator": 0,
        "logical operator": 0,
        "keyword": 0
    }
    
    for match in token_pattern.finditer(line):  # Loop through matches in the input line
        token = match.group(1)  # Get the matched token
        
        # Determine the type of the token using regular expressions
        if re.match(identifier_pattern, token):
            token_type = "identifier"
        elif re.match(constant_pattern, token):
            token_type = "constant"
        elif re.match(parenthesis_pattern, token):
            token_type = "parenthesis"
        elif re.match(punctuation_pattern, token):
            token_type = "punctuation"
        elif re.match(arithmetic_operator_pattern, token):
            token_type = "arithmetic operator"
        elif re.match(logical_operator_pattern, token):
            token_type = "logical operator"
        elif re.match(keyword_pattern, token):
            token_type = "keyword"

        tokens.append((token, token_type))  # Append the token and its type to the list of tokens
        
        # Update the token counts
        token_counts[token_type] += 1

    return tokens, token_counts  # Return the list of tokens and token counts

# Example usage:
input_line = input("Enter a line: ")  # Prompt the user to input a line of code
tokens, token_counts = tokenize_line(input_line)  # Tokenize the input line and get token counts

# Print token counts for each token type
for token, count in token_counts.items():
    if count > 0:
        print(f"{token}({count}) = ", end='')

        # Print the tokens of the current type
        tokens_of_type = [tok for tok, tok_type in tokens if tok_type == token]
        print(', '.join(tokens_of_type))  # Join tokens with commas and print them

