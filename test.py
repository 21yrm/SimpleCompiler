from antlr4 import *

from Cgrammer import Cgrammer

def main():
    # 读取 C 文件
    input = FileStream('input.c')

    # 创建词法分析器
    lexer = Cgrammer(input)

    # 获取词法单元流
    stream = CommonTokenStream(lexer)

    # 打印词法单元序列
    stream.fill()
    for token in stream.tokens:
        print(token.text)

if __name__ == '__main__':
    main()