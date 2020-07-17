import stack as st


def in2post(expr):
    if not isinstance(expr, str):
        raise ValueError
    stack = st.Stack()
    postfix = ""
    for item in expr:
        if item in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            postfix += f"{item} "
        elif item == '(':
            stack.push(item)
        elif item in ['+', '-', '/', '*']:
            try:
                while stack.top():
                    if stack.top() in ['+', '-'] and item in ['+', '-']:
                        postfix += f"{stack.top()} "
                        stack.pop()
                    elif stack.top() in ['*', '/'] and item in ['+', '-']:
                        postfix += f"{stack.top()} "
                        stack.pop()
                    elif stack.top() in ['*', '/'] and item in ['*', '/']:
                        postfix += f"{stack.top()} "
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
                    postfix += f"{stack.top()} "
                    stack.pop()
                else:
                    stack.pop()
            except IndexError:
                pass
    try:
        while stack.top():
            postfix += f"{stack.top()} "
            stack.pop()
    except IndexError:
        pass
    return postfix


def eval_postfix(expr):
    stacky_boi = st.Stack()
    operands = ['+', '-', '/', '*']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for thing in expr:
        if thing in numbers:
            stacky_boi.push(thing)
        elif thing in operands:
            num2 = int(stacky_boi.pop())
            num1 = int(stacky_boi.pop())
            if thing == '+':
                result = num1 + num2
                stacky_boi.push(result)
            elif thing == '-':
                result = num1 - num2
                stacky_boi.push(result)
            elif thing == '*':
                result = num1 * num2
                stacky_boi.push(result)
            elif thing == '/':
                result = num1 / num2
                stacky_boi.push(result)
    return stacky_boi.pop()


def main():
    with open("data.txt", "r") as file:
        for line in file:
            print(f"Infix: {line}", end="")
            print(f"postfix: {in2post(line)}")
            raw_post = in2post(line)
            raw_post.replace(" ", "")
            print(f"answer: {float(eval_postfix(raw_post))}")
            print("")


main()
