# generate a password from phrase

str = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+={[]};:'"\|,</?.>0123456789'''
# str = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789'''
n = len(str)
length = int(input('Enter the length of the password:'))
phrase = input('Enter the phrase:')
lp = len(phrase)
password = ''
M = 2*max(length, lp)+1
m = 2*min(length, lp)+1
temp = 2*(lp+length+sum([ord(i) for i in phrase]))+1
for i in range(length//lp+1):
    for x in phrase:
        temp = ((ord(x)+m+temp+i)*temp+ord(x)+temp+M+i) % (10**M+m)
        password += str[temp % n]
print('Password is:')
print(password[:length])
