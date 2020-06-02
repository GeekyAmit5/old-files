# single digit representation of a number
# e.g. 8734 = 8+7+3+4 = 22 = 2+2 = 4
# assuming input is always non zero


def sumDigit(n):
    if not n//10:
        return n
    else:
        return n % 10 + sumDigit(n//10)


def singleDigit(n):
    if not n//10:
        return n
    else:
        return singleDigit(sumDigit(n))


n = int(input("Enter the value of n : "))
print("Single Digit Resprentation of {} is {}".format(n, singleDigit(n)))
