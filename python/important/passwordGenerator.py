# to generate a password

import random

str = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+={[]};:'"\|,</?.>0123456789'''
# str = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789'''
l = len(str)
n = int(input('length? '))

for i in range(n):
    print(str[random.randint(0,l-1)],end='')
print()