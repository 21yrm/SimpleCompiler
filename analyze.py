import argparse
import os
import json

from antlr4 import *
from CgrammerLexer import CgrammerLexer
from CgrammerParser import CgrammerParser
from CgrammerVisitor import CgrammerVisitor


def print_json_tree(json_data, indent=0):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            print("  " * indent + str(key))
            print_json_tree(value, indent + 1)
    elif isinstance(json_data, list):
        for item in json_data:
            print_json_tree(item, indent)
    else:
        print("  " * indent + str(json_data))


class Visitor(CgrammerVisitor):
    def __init__(self):
        self.tree = {'code': ''}

    def get_children(self, node):
        if node.children is not None:
            return node.children
        else:
            return []

    def visitChildren(self, node):
        current_node = {}
        rule_name = CgrammerParser.ruleNames[node.getRuleIndex()]
        children = self.get_children(node)
        if children:
            # current_node[rule_name] = {}
            for child in children:
                if child.getChildCount() != 0:
                    if current_node.get(CgrammerParser.ruleNames[child.getRuleIndex()]) is None:
                        current_node[CgrammerParser.ruleNames[child.getRuleIndex()]] = []
                    current_node[CgrammerParser.ruleNames[child.getRuleIndex()]].append(self.visit(child))
                else:
                    if hasattr(child.getPayload(), 'type'):
                        current_node[CgrammerLexer.symbolicNames[child.getPayload().type]] = child.getText()
                    else:
                        current_node[CgrammerParser.ruleNames[child.getRuleIndex()]] = []
        else:
            current_node = node.getText()

        self.tree['code'] = current_node
        return current_node


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("--path", type=str, default="./C_code/Calculation.c")
    args = arg_parser.parse_args()

    c_file_path = args.path
    c_file_path: str
    if not c_file_path.endswith(".c") or not os.path.exists(c_file_path):
        raise Exception("Given path is invalid")

    input_stream = FileStream(c_file_path)
    lexer = CgrammerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CgrammerParser(stream)
    visitor = Visitor()

    visitor.visit(parser.code())
    # print(visitor.tree)
    print_json_tree(visitor.tree)
