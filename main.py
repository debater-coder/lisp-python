"""
An interpreter that implements a subset of lisp for floating point arithmetic.

It has 3 stages:
1. Lexer: Converts program text into a list of 'tokens'. Programs can have things such as spaces and blank lines, a lexer breaks a program into its significant components.
    Example: (+ 10 3) becomes ['(', '+', 10, 3, ')']
2. Parser: Converts list of tokens into an Abstract Syntax Tree (AST). Since lisp source code is a list, the AST is just a list of lists.
    Example:
3. Interpeter: Executes the AST, by recursively evaluating it.

I avoid using more advanced Python like type hinting, enums, or the `match` statement for clarity.
"""


"""Returns a list of tokens."""
from functools import reduce
from re import A


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


"""Parses tokens into an AST"""
def parser(tokens):
    # Since lisp programs are lists, all we need to do is skip the (, and place the elements into a list until we encounter the next )
    # If we encounter a ( inside, we have another list, on which we can recurse
    if tokens[0] != "(":
        raise Exception(f"Syntax error: expected ( but found {tokens[0]}")

    ast = []

    current_index = 1 # since we accounted for the starting ( already

    while current_index < len(tokens):
        if tokens[current_index] == ")":
            current_index += 1
            return ast, current_index # second value tells us how many values to skip
        if tokens[current_index] == "(":
            inner, skip = parser(tokens[current_index:])
            ast.append(inner)
            current_index += skip
        else:
            ast.append(tokens[current_index])
            current_index += 1

    raise Exception("Syntax error: expected ) but found end of file")

"""Executes an AST"""
def interpret(ast):
    # These are the functions/variables available to the program
    # If we wanted to add function/variable definition to the language, it would just involve changing this dynamically

    # lambda is just a compact way to define functions
    variables = {
        "+": lambda *args: sum(args),
        "-": lambda *args: reduce(lambda a, b: a - b, args),
        "*": lambda *args: reduce(lambda a, b: a * b, args),
        "/": lambda *args: reduce(lambda a, b: a / b, args),
    }

    # in real lisp, the quote keyword prevents evaluation of lists
    # we haven't implemented that here

    function = ast[0] # the first item in the list is the function

    args = []

    for arg in ast[1:]:
        if isinstance(arg, list):
            # evaluate the sub-list
            args.append(interpret(arg))
        else:
            args.append(arg)

    return variables[function](*args)



program = "(+ (* 2 3 5) (+ 6 5 3 1))"
tokens = lexer(program)
print("tokens:", tokens)
ast = parser(tokens)[0]
print("ast:", ast)
print("result", interpret(ast))
