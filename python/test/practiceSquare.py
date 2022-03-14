import random

while True:
    a = random.randint(1,30)
    ans = int(input(str(a)+' = '))
    if ans == a*a:
        print('Correct!')
    else:
        print('Wrong!')
        print('Answer is',a*a)
        break