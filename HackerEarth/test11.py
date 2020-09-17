s = input()

sum, j = 0, 1
for i in s:
    sum += j*int(i)
    j += 1

if sum % 11:
    print('Illegal ISBN')
else:
    print('Legal ISBN')
