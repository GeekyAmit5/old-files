import random
import time

score = 0
Time = 0
letters = list('abcdefghijklmnopqrstuvwxyz'.upper())

while score<50:
    letter = random.choice(letters)
    t0 = time.time()
    guess = int(input('What is rank of '+letter+' ?\n'))
    Time += time.time() - t0
    if guess == ord(letter) - 64:
        print('Correct!\n')
        score+=1
    else:
        print('\nWrong!')
        print('Rank of',letter,'is',ord(letter)-64,'\n')
        break
else:
    print('You Know Everything!')

if score:
    print('Your Average time is: ',Time/score,'seconds')
print('Your Score is',2*score)