#!/usr/bin/env python3.8
print("Hello World")

x = float(input("What is your x: " ))
y = float(input("What is your y: "))
Ops = input("addition, subtraction, multiplication, division?: ")

def cal(x, y):
    if Ops == "addition":
        return x + y
    if Ops == "subtraction":
        return x - y
    if Ops == "multiplication":
        return x * y
    if Ops == "division":
        return x / y
    else:
        return "Invalid operation selected!"

print(x, y, cal(x,y))