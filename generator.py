from antlr4 import *
from antlr4.tree.Trees import Trees
from gen.ClangLexer import ClangLexer
from gen.ClangParser import ClangParser
import json


def iterate_over_tree(node, rule_names):
    name = Trees.getNodeText(node, ruleNames=rule_names)

    if node.getChildCount() == 0:
        return name

    children = []

    for c in node.getChildren():
        children.append(iterate_over_tree(c, rule_names))

    if node.getChildCount() > 1:
        return {name: children}
    else:
        return {name: children[0]}


def convert_to_json(tree, rule_names, pretty=True):
    if pretty:
        return json.dumps(iterate_over_tree(tree, rule_names), indent=4)
    else:
        return json.dumps(iterate_over_tree(tree, rule_names))


def get_json_from_file(filename):
    lexer = ClangLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser = ClangParser(stream)
    tree = parser.compilationUnit()
    return convert_to_json(tree, rule_names=parser.ruleNames)


def main():
    sw = open('output.txt', 'w')
    sw.write(get_json_from_file('input.txt'))
    sw.close()


if __name__ == '__main__':
    main()
