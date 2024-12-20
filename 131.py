infix_expression = input("Введите инфиксное выражение: ").split()

operators = []
postfix = []

for token in infix_expression:
    if token.isdigit():
        postfix.append(token)
    elif token in ['+', '-', '*', '/']:
        while operators and operators[-1] != '(':

            if (token in ['+', '-'] and operators[-1] in ['*', '/'] or
                    token in ['*', '/'] and operators[-1] in ['*', '/']):
                postfix.append(operators.pop())
            else:
                break
        operators.append(token)
    elif token == '(':
        operators.append(token)
    elif token == ')':
        while operators and operators[-1] != '(':
            postfix.append(operators.pop())
        operators.pop()

while operators:
    postfix.append(operators.pop())

print("Постфиксное выражение:", " ".join(postfix))