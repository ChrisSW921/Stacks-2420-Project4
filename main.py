import stack as st


def in2post(exp):
    stack = st.Stack()
    postfix = ""
    for item in exp:
        if item in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            postfix += item
        elif item == '(':
            stack.push(item)
        elif item in ['+', '-', '/', '*']:
            while stack.top():
                if stack.top() in ['+', '-'] and item in ['+', '-']:
                    postfix += stack.top()
                    stack.pop()
                elif stack.top in ['*', '/'] and item in ['+', '-']:
                    postfix += stack.top()
                    stack.pop()
                elif stack.top in ['*', '/'] and item in ['*', '/']:
                    postfix += stack.top()
                    stack.pop()
        elif item == ')':
            while stack.top() != '(':
                postfix += stack.top()
                stack.pop()
            if stack.top() == '(':
                stack.pop()
        while stack.top():
            postfix += stack.top()
            stack.pop()
    return postfix


def main():
    with open("data.txt", "r") as file:
        for line in file:
            print(f"Infix: {line}")
            print(in2post(line))


main()
