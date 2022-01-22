# hacking using brute force

n = int(input('Enter max length: '))
str = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+={[]};:'"\|,</?.>0123456789'''
words = list(str)
total = 0

while words:
    temp = words.pop(0)
    print(temp)
    total += 1
    if len(temp) < n:
        for i in str:
            words.append(temp+i)

print('Total:', total)
