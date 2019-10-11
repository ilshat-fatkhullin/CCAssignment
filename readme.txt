We used Antlr4 in Python3 for this assignment. (https://www.antlr.org)

Antlr4 format is not EBFN, which is used in YACC, but it is almost the same.

To run, pip package "antlr4-python3-runtime" is required. (https://pypi.org/project/antlr4-python3-runtime)

The parser is also compiled from the grammar.

The grammar can be found in src/Clang.g4

if you run generator.py, it would take input from input.txt
and print the output to the corresponding output.txt.

We also have different C files in examples and corresponding outputs.