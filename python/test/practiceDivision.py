import random

while True:
    a = random.randint(1,1000)
    b = random.randint(1,100)
    ans = int(input(str(a*b)+' / '+str(a)+' = '))
    if ans != b:
        print('Wrong!')
        print('Answer is',b)
        break
    else:
        print('Correct!')