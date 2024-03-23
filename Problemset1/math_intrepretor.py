def calculate_expression(expression):
    x, operator, z = expression.split()
    x = int(x)
    z = int(z)

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        result = x / z
    return "{:.1f}".format(result)

def main():
    expression = input("Enter an arithmetic expression (e.g., 'x + z'): ")
    result = calculate_expression(expression)
    print("Result:", result)

if __name__ == "__main__":
    main()
