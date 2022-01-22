# hacking using brute force

n = int(input('Enter max length: '))
# str = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+={[]};:'"\|,</?.>0123456789'''
str = 'abcd'
words = list(str)
for word in words:
    print(word)

while len(words[-1]) < n:
    words = [i+j for i in words for j in str]
    for word in words:
        print(word)
