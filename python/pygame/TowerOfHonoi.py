# this is a Tower of Hanoi Solver


def honoi(n, f, a, t):
    global c
    if n == 0:
        pass
    else:
        honoi(n-1, f, t, a)
        print("Move a disc from {} to {}".format(f, t))
        c += 1
        honoi(n-1, a, f, t)


c = 0
n = int(input('How many disk you want to move? '))
honoi(n, "A", "B", "C")
print("Done!")
print("Total Moves :", c)
