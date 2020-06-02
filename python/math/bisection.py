# Bisection method

def f(x):
    return x ** 3 - 1


def exist(f, a, b):
    if f(a) * f(b) > 0:
        return False
    return True


def root(f, a, b, p):
    print(f((a + b / 2)))

    if abs(f((a+b)/2) )< p:
        exit()

    if exist(f, (a + b) / 2, b):
        print( (a + b) / 2, b)
        root(f, (a + b) / 2, b, p)
    else:
        print( (a + b) / 2, b)
        root(f, a, (a + b) / 2, p)


a = float(input("a = "))
b = float(input("b = "))
p = float(input("Accuracy = "))
if exist(f, a, b):
    root(f, a, b, p)
else:
    print("Invalid Input")
