import random
import time

while True:
    a = random.randint(1,100)
    b = 5*(2*random.randint(1,12)+1)
    op = random.randint(0,1)
    answer = a/b if op else a*b
    t0 = time.time()
    if op:
        ans = int(input(str(a)+' / '+str(b)+' = '))
    else:
        ans = int(input(str(a)+' * '+str(b)+' = '))
    t1 = time.time()
    if ans == answer:
        print('Correct!')
    else:
        print('Wrong!')
        print('Answer is',answer)
    print('Time:',t1-t0)