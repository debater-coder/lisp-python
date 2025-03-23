"""
An interpreter that implements a subset of lisp for floating point arithmetic.

It has 3 stages:
1. Lexer: Converts program text into a list of 'tokens'. Programs can have things such as spaces and blank lines, a lexer breaks a program into its significant components.
    Example: (+ 10 3) becomes ['(', '+', 10, 3, ')']
2. Parser: Converts list of tokens into an Abstract Syntax Tree (AST). This is a structured tree type to represent the program.
3. Interpeter: Executes the AST, by recursively evaluating it.

I avoid using more advanced Python like type hinting, enums, or the `match` statement for clarity.
"""

def lexer(program):
    current_index = 0
    tokens = []

    # program.split() is not used since there may be two tokens not separated by whitespace eg: (+
    while current_index < len(program):
        if program[current_index] in ['(', ')']:
            tokens.append(program[current_index])  # add these as is
            current_index += 1
        elif program[current_index].isspace():
            # whitespace so ignore
            current_index += 1
        elif program[current_index].isdigit() or program[current_index] == ".":  # notation such as .5 is allowed
            number = ""
            while current_index < len(program) and (program[current_index].isdigit() or program[current_index] == "."):
                number += program[current_index]
                current_index += 1
            try:
                tokens.append(float(number))
            except ValueError as e:
                raise Exception(f"Syntax error while processing number at char {current_index}: {e}")
        else:
            # we have either a keyword or a variable
            # in this language we have + - * / all implemented as functions
            # if we wanted to add if statements or function definition we would make new keywords
            # This would only need changes at the interpreter level
            identifier = ""
            while current_index < len(program) and not program[current_index].isspace():
                identifier += program[current_index]
                current_index += 1
            tokens.append(identifier)

    return tokens

print(lexer("(+ (* 2 3 5) (+ 6 5 3 1))"))
