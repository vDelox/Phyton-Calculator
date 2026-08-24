def add(x, y):
    return x+y

  def remove(x, y):
    return x-y

 def multi(x, y):
    return x*y

def subs(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x/y

def square(x, y):
    return x**y

def mod(x, y):
    if y == 0:
        return "Error: Cannot calculate modulo by zero!"
    return x%y

while True:
    x = int(input("Type first number : "))
    y = int(input("Type second number : "))


    command = input("Tell me what operation to use : ")

    if command == "+":
        print(add(x, y))

    elif command == "-":
        print(remove(x, y))

    elif command == "*" or command == ".":
        print(multi(x, y))

    elif command == "/" or command == "÷":
        print(subs(x, y))

    elif command == "**":
        print(square(x, y))

    elif command == "%":
        print(mod(x, y))
