# hacking using brute force
import pikepdf
import time

# str = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+={[]};:'"\|,</?.>0123456789'''
str = 'zapmxlqors'
# n = int(input('Enter max length: '))
n = 8
words = list(str)

print('Please wait a while we are doing our best!')
print('Cracking the password...')
found = False
t0 = time.time()
while not found:
    for word in words:
        try:
            pikepdf.open('python/important/pdf_hack/test.pdf', password=word)
            t1 = time.time()
            print('Password found!')
            print('Password is:', word)
            print('Time:', t1-t0, 'seconds')
            found = True
            break
        except:
            pass
    if len(words[-1]) < n and not found:
        words = [i+j for i in words for j in str]
    else:
        break
