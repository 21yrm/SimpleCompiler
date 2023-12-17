import argparse
import os

from antlr4 import *
from Cgrammer import Cgrammer

def generateTokens(c_file_path):        
    # 读取 C 文件
    input = FileStream(c_file_path)

    # 创建词法分析器
    lexer = Cgrammer(input)

    # 获取词法单元流
    stream = CommonTokenStream(lexer)

    # 生成词法单元列表
    stream.fill()
    token_list = []
    for token in stream.tokens:
        token_list.append({
            "type": token.type,
            "text": token.text,
            "line": token.line,
            "column": token.column
        })

    return token_list

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("--path", type=str, default="./C_code/PlalindromeDetection.c")
    args = arg_parser.parse_args()

    c_file_path = args.path
    c_file_path : str
    if not c_file_path.endswith(".c") or not os.path.exists(c_file_path):
        raise Exception("Given path is invalid")
    tokens = generateTokens(c_file_path)
    for token in tokens:
        print(token)
