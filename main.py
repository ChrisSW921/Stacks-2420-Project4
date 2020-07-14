import stack as st


def in2post(expr):
    if not isinstance(expr, str):
        raise ValueError
    temp_st = st.Stack()

    return True


def eval_postfix(expr):
    return True


def main():
    with open("data.txt", "r") as file:
        for line in file:
            print(f"Infix: {line}")
            in2post(line)


main()
