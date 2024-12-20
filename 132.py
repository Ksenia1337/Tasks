infix_expression = input("Введите математическое выражение в инфиксной форме: ").split()

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

values = []
for token in postfix:
    if token.isdigit():
        values.append(int(token))
    elif token == '~':
        values.append(-values.pop())
    elif token in ['+', '-', '*', '/']:
        right = values.pop()
        left = values.pop()
        if token == '+':
            values.append(left + right)
        elif token == '-':
            values.append(left - right)
        elif token == '*':
            values.append(left * right)
        elif token == '/':
            values.append(left / right)
result = values[0]

print("Постфиксное выражение:", " ".join(postfix))
print("Результат:", result)