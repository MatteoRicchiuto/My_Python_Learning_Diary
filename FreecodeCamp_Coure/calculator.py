num1 = float(input("Enter first numer: "))
op = input("Enter enter operator: ")
num2 = float(input("Enter second numer: "))

if op == "+":
    print((num1 + num2))
elif op == "-":
    print((num1 - num2))
elif op == "*" or "x":
    print((num1 * num2))
elif op == "/" or ":":
    print((num1 / num2))
else:
    print("invalid operator")