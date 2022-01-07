# generate a password from phrase

str = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+={[]};:'"\|,</?.>0123456789'''
# str = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789'''
n = len(str)
length = int(input('Enter the length of the password:'))
phrase = input('Enter the phrase:')
lp = len(phrase)
password = ''
M=2*max(length,lp)+1
m=2*min(length,lp)+1
L=lp+length
temp=2*(L+M+m)+1
for i in range(length//lp+1):
    for x in phrase:
        temp= ((ord(x)+L+i)*temp+ord(x)+L+i)%(10**M+m)
        password += str[temp%n]
print('Password is:')
print(password[:length])