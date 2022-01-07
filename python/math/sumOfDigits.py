# to find sum of digits of a number

def sumOfDigits(x):
    if x//10:
        return x % 10+sumOfDigits(x//10)
    return x


x = int(input('Enter a number: '))
print('Sum of digits of', x, 'is', sumOfDigits(x))
