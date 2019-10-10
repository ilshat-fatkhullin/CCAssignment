from antlr4 import *
from antlr4.tree.Trees import Trees
from gen.ClangLexer import ClangLexer
from gen.ClangParser import ClangParser
import json


def traverse(node: RuleContext, rule_names):
    name = Trees.getNodeText(node, ruleNames=rule_names)

    if node.getChildCount() == 0:
        return name

    children = [traverse(child, rule_names) for child in node.getChildren()]

    if node.getChildCount() == 1:
        return {name: children[0]}

    return {name: children}


def to_json(tree: RuleContext, rule_names, pretty=True):
    repr = traverse(tree, rule_names)

    if pretty:
        return json.dumps(repr, indent=4)

    return json.dumps(repr)


def get_json(filename):
    istream = FileStream(filename)

    lexer = ClangLexer(istream)
    stream = CommonTokenStream(lexer)
    parser = ClangParser(stream)
    tree = parser.compilationUnit()

    return to_json(tree, rule_names=parser.ruleNames)


def main():
    with open('../out.txt', 'w') as output:
        output.write(get_json('../in.txt'))
        output.close()


if __name__ == '__main__':
    main()
