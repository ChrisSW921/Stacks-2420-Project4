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
            try:
                while stack.top():
                    if stack.top() in ['+', '-'] and item in ['+', '-']:
                        postfix += stack.top()
                        stack.pop()
                    elif stack.top() in ['*', '/'] and item in ['+', '-']:
                        postfix += stack.top()
                        stack.pop()
                    elif stack.top() in ['*', '/'] and item in ['*', '/']:
                        postfix += stack.top()
                        stack.pop()
                    elif stack.top() in ['+', '-'] and item in ['*', "/"]:
                        stack.push(item)
                        break
                    elif stack.top() == '(':
                        stack.push(item)
                        break
            except IndexError:
                stack.push(item)
        elif item == ')':
            try:
                while stack.top() != '(':
                    postfix += stack.top()
                    stack.pop()
                else:
                    stack.pop()
            except IndexError:
                pass
    try:
        while stack.top():
            postfix += stack.top()
            stack.pop()
    except IndexError:
        print("OK")
    return postfix


def main():
    with open("data.txt", "r") as file:
        for line in file:
            print(f"Infix: {line}")
            print(in2post(line))


main()
