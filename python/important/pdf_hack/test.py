# hacking using brute force
import pikepdf
import time

# str = 'abchirsxyz'
str = '123456789'
# n = len(str)
n = 5
words = list(str)

print('decrypting...')
t0 = time.time()
while words:
    temp = words.pop(0)
    try:
        # print('trying...', temp)
        pikepdf.open('python/important/pdf_hack/test.pdf', password=temp)
        t1 = time.time()
        print('Password found!')
        print('Password is:', temp)
        print('Time:', t1-t0)
        break
    except:
        pass
    if len(temp) < n:
        for i in str:
            words.append(temp+i)
