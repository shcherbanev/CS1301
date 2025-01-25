#!/bin/env python

users_input = input("Expression: ").strip().lower()

x, math_operator, y = users_input.split(" ")

x = int(x)
y = int(y)

if math_operator == "+":
    z = x + y
    z = float(z)
    print(z)
elif math_operator == "-":
    z = x - y
    z = float(z)
    print(z)
elif math_operator == "/":
    z = x / y
    z = float(z)
    print(z)
elif math_operator == "*":
    z = x * y
    z = float(z)
    print(z)