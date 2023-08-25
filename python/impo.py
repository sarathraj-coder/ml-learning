import importlib

a=input("Enter a number ")
b=input("Enter a number ")

try:
    c=int(a)/int(b)
except TypeError as e:
    print("Type error")
    c=None
except ZeroDivisionError as e:
    print("Division by 0 is not possible")
    c=None

print(c)
