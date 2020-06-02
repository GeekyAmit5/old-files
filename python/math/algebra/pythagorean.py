n = int(input("Enter the value of n : "))+1
triplets = [(x, y, z) for x in range(1, n) for y in range(x, n)
            for z in range(y, n) if x*x + y*y == z*z]
for i in triplets:
    print(i)
