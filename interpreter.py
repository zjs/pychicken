import sys
from collections import defaultdict

def interpret(text, input):
    lines = text.split("\n")
    line_contents = [[val.strip() for val in line.split("chicken")] for line in lines]
    if any([line.count('') != len(line) for line in line_contents]):
        return "invalid input"
    op_codes = [len(line_content)-1 for line_content in line_contents]
    return interpret_codes(op_codes, input)

def interpret_codes(op_codes, input):
    codes = [
        '', #axe
        lambda stack: stack.append('chicken'),
        lambda stack: stack.append(stack.pop() + stack.pop()),
        lambda stack: stack.append(-(stack.pop() - stack.pop())),
        lambda stack: stack.append(stack.pop() * stack.pop()),
        lambda stack: stack.append(stack.pop() == stack.pop()),
        '', #pick
        '', #peck
        '', #fr
        '', #bbq
        lambda stack, value: stack.append(value - 10)
    ]
    stack = []
    for op in op_codes:
        if op < 10:
            codes[op](stack)
        else:
            codes[10](stack, op)
    return stack[-1]

if __name__ == "__main__":
    print interpret(sys.argv[1], sys.argv[2])

